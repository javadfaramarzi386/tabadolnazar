# forum/models.py

from django.contrib.auth.models import User
from django.db import models
from django.db.models import F
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="نام دسته‌بندی",
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        verbose_name="آدرس اینترنتی (Slug)",
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    short_description = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="توضیح کوتاه برای انتخاب دسته",
    )

    usage_guide = models.TextField(
        blank=True,
        verbose_name="راهنمای استفاده از این دسته",
    )

    writing_help = models.TextField(
        blank=True,
        verbose_name="راهنمای نوشتن مطلب",
    )

    important_notice = models.TextField(
        blank=True,
        verbose_name="نکات مهم",
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="دسته والد",
    )

    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    is_visible = models.BooleanField(
        default=True,
        verbose_name="نمایش داده شود",
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="آیکون FontAwesome",
    )

    color = models.CharField(
        max_length=20,
        default="#0d6efd",
        verbose_name="رنگ",
    )

    image = models.ImageField(
        upload_to="category_images/",
        blank=True,
        null=True,
        verbose_name="تصویر دسته‌بندی",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)

        super().save(*args, **kwargs)

    def get_post_count(self):
        return self.posts.filter(is_approved=True).count()

    def children_count(self):
        return self.children.count()

    def has_children(self):
        return self.children.exists()

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} ← {self.name}"

        return self.name

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="عنوان موضوع",
    )

    content = models.TextField(
        verbose_name="متن موضوع",
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="نویسنده",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name="دسته‌بندی",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین ویرایش",
    )

    is_approved = models.BooleanField(
        default=True,
        verbose_name="تأیید شده",
    )

    is_pinned = models.BooleanField(
        default=False,
        verbose_name="سنجاق شده",
    )

    is_locked = models.BooleanField(
        default=False,
        verbose_name="قفل شده",
    )

    views = models.PositiveIntegerField(
        default=0,
        verbose_name="تعداد بازدید",
    )

    likes = models.ManyToManyField(
        User,
        blank=True,
        related_name="liked_posts",
        verbose_name="لایک‌ها",
    )

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_comments(self):
        return self.comments.filter(is_approved=True).count()

    @property
    def is_popular(self):
        return self.total_likes >= 10

    def increase_views(self):
        type(self).objects.filter(pk=self.pk).update(
            views=F("views") + 1
        )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-is_pinned", "-created_at"]
        verbose_name = "موضوع"
        verbose_name_plural = "موضوعات"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="موضوع",
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="نویسنده",
    )

    content = models.TextField(
        verbose_name="متن نظر",
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name="پاسخ به",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین ویرایش",
    )

    is_approved = models.BooleanField(
        default=True,
        verbose_name="تأیید شده",
    )

    is_edited = models.BooleanField(
        default=False,
        verbose_name="ویرایش شده",
    )

    @property
    def has_replies(self):
        return self.replies.exists()

    @property
    def replies_count(self):
        return self.replies.filter(is_approved=True).count()

    def short_content(self):
        if len(self.content) > 50:
            return f"{self.content[:50]}..."

        return self.content

    def __str__(self):
        return f"{self.author.username} | {self.post.title[:30]}"

    class Meta:
        ordering = ["created_at"]
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"