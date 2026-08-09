# forum/admin.py

from django.contrib import admin

from .models import Category, Comment, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "parent",
        "display_order",
        "is_active",
        "is_visible",
        "slug",
    )

    list_filter = (
        "is_active",
        "is_visible",
        "parent",
    )

    search_fields = (
        "name",
        "description",
        "short_description",
        "usage_guide",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    ordering = (
        "display_order",
        "name",
    )

    fieldsets = (
        (
            "اطلاعات اصلی دسته",
            {
                "fields": (
                    "name",
                    "slug",
                    "parent",
                    "description",
                )
            },
        ),

        (
            "راهنمای انتخاب دسته توسط کاربران",
            {
                "fields": (
                    "short_description",
                    "usage_guide",
                    "writing_help",
                    "important_notice",
                )
            },
        ),

        (
            "تنظیمات نمایش",
            {
                "fields": (
                    "display_order",
                    "is_active",
                    "is_visible",
                    "icon",
                    "color",
                    "image",
                )
            },
        ),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "category",
        "created_at",
        "is_approved",
        "total_likes",
        "total_comments",
    )

    list_filter = (
        "category",
        "is_approved",
        "created_at",
    )

    search_fields = (
        "title",
        "content",
        "author__username",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "total_likes",
        "total_comments",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

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