# =============================================================================
# forum/views.py
# =============================================================================
"""
ویوهای اپلیکیشن forum

این فایل شامل تمام منطق صفحات فروم شامل لیست پست‌ها، جزئیات پست، ایجاد، ویرایش، کامنت و لایک است.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count

from .models import Post, Category
from .forms import PostForm, CommentForm


# =============================================================================
# لیست پست‌ها
# =============================================================================

def post_list(request):
    """
    صفحه اصلی فروم - نمایش لیست تمام پست‌های تأیید شده.
    پشتیبانی از جستجوی全文.
    """
    search = request.GET.get("q", "").strip()

    posts = (
        Post.objects.filter(is_approved=True)
        .select_related("author", "author__profile", "category")
        .prefetch_related("likes", "comments")
        .order_by("-is_pinned", "-created_at")
    )

    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search) |
            Q(author__username__icontains=search)
        )

    categories = (
        Category.objects.filter(is_visible=True)
        .annotate(post_count=Count("posts"))
        .order_by("display_order", "name")
    )

    return render(request, "forum/post_list.html", {
        "posts": posts,
        "categories": categories,
        "search": search,
        "title": "فروم تبادل نظر",
    })


# =============================================================================
# پست‌های یک دسته‌بندی خاص
# =============================================================================

def category_posts(request, slug):
    """
    نمایش پست‌های مربوط به یک دسته‌بندی خاص.
    """
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
            Q(title__icontains=search) |
            Q(content__icontains=search) |
            Q(author__username__icontains=search)
        )

    categories = (
        Category.objects.filter(is_visible=True)
        .annotate(post_count=Count("posts"))
        .order_by("display_order", "name")
    )

    return render(request, "forum/post_list.html", {
        "posts": posts,
        "categories": categories,
        "category": category,
        "search": search,
        "title": f"دسته‌بندی: {category.name}",
    })


# =============================================================================
# جزئیات پست + ارسال کامنت
# =============================================================================

def post_detail(request, pk):
    """
    نمایش جزئیات یک پست + امکان ارسال کامنت.
    """
    post = get_object_or_404(
        Post.objects.select_related("author", "author__profile", "category")
                    .prefetch_related("likes"),
        pk=pk,
        is_approved=True,
    )

    # افزایش تعداد بازدید
    post.increase_views()

    # دریافت کامنت‌های تأیید شده
    comments = (
        post.comments.filter(is_approved=True)
        .select_related("author", "author__profile")
        .order_by("created_at")
    )

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "برای ارسال نظر باید وارد حساب کاربری خود شوید.")
            return redirect("accounts:login")

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

    return render(request, "forum/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_form": form,
        "title": post.title,
    })


# =============================================================================
# ایجاد پست جدید
# =============================================================================

@login_required
def create_post(request):
    """
    ایجاد موضوع (پست) جدید توسط کاربر.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            messages.success(request, "موضوع شما با موفقیت ایجاد شد.")
            return redirect("forum:post_detail", pk=post.pk)
    else:
        form = PostForm()

    return render(request, "forum/create_post.html", {
        "form": form,
        "title": "ایجاد موضوع جدید",
    })


# =============================================================================
# ویرایش پست
# =============================================================================

@login_required
def edit_post(request, pk):
    """
    ویرایش پست توسط نویسنده آن.
    فقط نویسنده پست می‌تواند آن را ویرایش کند.
    """
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "پست با موفقیت ویرایش شد.")
            return redirect("forum:post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, "forum/create_post.html", {
        "form": form,
        "title": "ویرایش موضوع",
    })


# =============================================================================
# حذف پست
# =============================================================================

@login_required
def delete_post(request, pk):
    """
    حذف پست توسط نویسنده آن.
    """
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "پست با موفقیت حذف شد.")
        return redirect("forum:post_list")

    # GET request → تأیید حذف
    return redirect("forum:post_detail", pk=pk)


# =============================================================================
# لایک پست (Toggle)
# =============================================================================

@login_required
def like_post(request, pk):
    """
    لایک یا لغو لایک یک پست.
    """
    post = get_object_or_404(Post, pk=pk)

    if request.user in post.likes.all():  # اگر قبلاً لایک کرده بود
        post.likes.remove(request.user)  # ← لایک را لغو کن
    else:
        post.likes.add(request.user)  # ← لایک کن

    return redirect("forum:post_detail", pk=pk)