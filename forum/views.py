# forum/views.py

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm, PostForm
from .models import Category, Post
from accounts.decorators import verified_member_required


def post_list(request):
    search = request.GET.get("q", "").strip()

    posts = (
        Post.objects.filter(is_approved=True)
        .select_related("author", "author__profile", "category")
        .prefetch_related("likes", "comments")
        .order_by("-is_pinned", "-created_at")
    )

    if search:
        posts = posts.filter(
            Q(title__icontains=search)
            | Q(content__icontains=search)
            | Q(author__username__icontains=search)
        )

    categories = (
        Category.objects.filter(is_visible=True)
        .annotate(post_count=Count("posts"))
        .order_by("display_order", "name")
    )

    return render(
        request,
        "forum/post_list.html",
        {
            "posts": posts,
            "categories": categories,
            "search": search,
            "title": "فروم تبادل نظر",
        },
    )


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    search = request.GET.get("q", "").strip()

    posts = (
        Post.objects.filter(category=category, is_approved=True)
        .select_related("author", "author__profile", "category")
        .prefetch_related("likes", "comments")
        .order_by("-is_pinned", "-created_at")
    )

    if search:
        posts = posts.filter(
            Q(title__icontains=search)
            | Q(content__icontains=search)
            | Q(author__username__icontains=search)
        )

    categories = (
        Category.objects.filter(is_visible=True)
        .annotate(post_count=Count("posts"))
        .order_by("display_order", "name")
    )

    return render(
        request,
        "forum/post_list.html",
        {
            "posts": posts,
            "categories": categories,
            "category": category,
            "search": search,
            "title": f"دسته‌بندی: {category.name}",
        },
    )


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.select_related(
            "author",
            "author__profile",
            "category",
        ).prefetch_related("likes"),
        pk=pk,
        is_approved=True,
    )

    post.increase_views()

    comments = (
        post.comments.filter(is_approved=True)
        .select_related("author", "author__profile")
        .order_by("created_at")
    )

    if request.method == "POST":
        if request.user.profile.membership_status != "verified":
            messages.warning(
                request,
                "برای ارسال نظر باید عضویت شما تأیید شده باشد."
            )

            return redirect(
                "forum:post_detail",
                pk=post.pk
            )

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            messages.success(request, "نظر شما با موفقیت ثبت شد.")
            return redirect("forum:post_detail", pk=post.pk)
    else:
        form = CommentForm()

    return render(
        request,
        "forum/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": form,
            "title": post.title,
        },
    )


@login_required
@verified_member_required
def create_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            messages.success(
                request,
                "موضوع شما با موفقیت ایجاد شد."
            )

            return redirect(
                "forum:post_detail",
                pk=post.pk
            )

    else:
        form = PostForm()

    return render(
        request,
        "forum/create_post.html",
        {
            "form": form,
            "title": "ایجاد موضوع جدید",
        },
    )


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()

            messages.success(request, "پست با موفقیت ویرایش شد.")
            return redirect("forum:post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "forum/create_post.html",
        {
            "form": form,
            "title": "ویرایش موضوع",
        },
    )


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        post.delete()

        messages.success(request, "پست با موفقیت حذف شد.")
        return redirect("forum:post_list")

    return redirect("forum:post_detail", pk=pk)


@login_required
@require_POST
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.likes.filter(pk=request.user.pk).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect("forum:post_detail", pk=pk)