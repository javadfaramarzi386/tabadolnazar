# forum/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count

from .models import Post, Category, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    """صفحه اصلی فروم"""
    posts = Post.objects.filter(
        is_approved=True
    ).select_related('author', 'category').order_by('-created_at')

    # دسته‌بندی‌ها بدون annotate (برای جلوگیری از تداخل با property)
    categories = Category.objects.filter(is_visible=True).order_by('display_order')

    return render(request, 'forum/post_list.html', {
        'posts': posts,
        'categories': categories,
        'title': 'فروم تبادل نظر'
    })


def category_posts(request, slug):
    """پست‌های یک دسته‌بندی خاص"""
    category = get_object_or_404(Category, slug=slug)

    posts = Post.objects.filter(
        category=category,
        is_approved=True
    ).select_related('author').order_by('-created_at')

    categories = Category.objects.filter(is_visible=True).order_by('display_order')

    return render(request, 'forum/post_list.html', {
        'posts': posts,
        'category': category,
        'categories': categories,
        'title': f'دسته‌بندی: {category.name}'
    })


def post_detail(request, pk):
    """جزئیات پست + ارسال کامنت"""
    post = get_object_or_404(Post, pk=pk, is_approved=True)

    comments = post.comments.filter(is_approved=True).select_related('author').order_by('created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "برای ارسال نظر باید وارد حساب کاربری شوید.")
            return redirect('accounts:login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            messages.success(request, "نظر شما با موفقیت ثبت شد.")
            return redirect('forum:post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'forum/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': form,
        'title': post.title
    })


@login_required
def create_post(request):
    """ایجاد پست جدید"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            messages.success(request, "موضوع شما با موفقیت ایجاد شد.")
            return redirect('forum:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'forum/create_post.html', {
        'form': form,
        'title': 'ایجاد موضوع جدید'
    })


@login_required
def edit_post(request, pk):
    """ویرایش پست"""
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "پست با موفقیت ویرایش شد.")
            return redirect('forum:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'forum/create_post.html', {
        'form': form,
        'title': 'ویرایش پست'
    })


@login_required
def delete_post(request, pk):
    """حذف پست"""
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "پست با موفقیت حذف شد.")
        return redirect('forum:post_list')

    return redirect('forum:post_detail', pk=pk)


@login_required
def like_post(request, pk):
    """لایک / آنلایک"""
    post = get_object_or_404(Post, pk=pk)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('forum:post_detail', pk=pk)