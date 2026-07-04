# forum/admin.py

# =====================================================
# پنل مدیریت جنگو (Django Admin)
# =====================================================

from django.contrib import admin

from .models import Category, Post, Comment


# =====================================================
# مدیریت دسته‌بندی‌ها
# =====================================================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    تنظیمات نمایش دسته‌بندی‌ها در پنل مدیریت
    """

    # ستون‌های نمایش
    list_display = (
        "name",
        "parent",
        "display_order",
        "is_active",
        "slug",
    )

    # فیلترها
    list_filter = (
        "is_active",
        "parent",
    )

    # جستجو
    search_fields = (
        "name",
        "description",
    )

    # تولید خودکار slug
    prepopulated_fields = {
        "slug": ("name",)
    }

    # مرتب‌سازی
    ordering = (
        "display_order",
        "name",
    )


# =====================================================
# مدیریت پست‌ها
# =====================================================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    تنظیمات مدیریت پست‌ها
    """

    # ستون‌های جدول
    list_display = (
        "title",
        "author",
        "category",
        "created_at",
        "is_approved",
        "total_likes",
        "total_comments",
    )

    # فیلترها
    list_filter = (
        "category",
        "is_approved",
        "created_at",
    )

    # جستجو
    search_fields = (
        "title",
        "content",
        "author__username",
    )

    # فقط خواندنی
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # مرتب‌سازی
    ordering = (
        "-created_at",
    )


# =====================================================
# مدیریت نظرات
# =====================================================
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    تنظیمات مدیریت نظرات
    """

    list_display = (
        "author",
        "post",
        "created_at",
        "is_approved",
    )

    list_filter = (
        "is_approved",
        "created_at",
    )

    search_fields = (
        "content",
        "author__username",
        "post__title",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )