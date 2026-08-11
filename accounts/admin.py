from django.contrib import admin
from django.utils.html import format_html

from .models import Profile, Report


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "avatar_preview",
        "nickname",
        "membership_status",
        "verification_requested",
        "relationship_to_child",
        "child_age",
        "condition_type",
        "location",
        "created_at",
    )

    list_filter = (
        "membership_status",
        "verification_requested",
        "condition_type",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "nickname",
        "location",
        "condition_type",
        "relationship_to_child",
    )

    ordering = ("-created_at",)

    actions = [
        "approve_members",
        "block_members",
        "pending_members",
    ]

    @admin.display(description="تصویر پروفایل")
    def avatar_preview(self, obj):
        if not obj.avatar:
            return "بدون تصویر"

        try:
            if not obj.avatar.storage.exists(obj.avatar.name):
                return "فایل تصویر پیدا نشد"

            return format_html(
                '<img src="{}" width="45" height="45" '
                'style="object-fit: cover; border-radius: 6px;" />',
                obj.avatar.url,
            )

        except (FileNotFoundError, OSError):
            return "فایل تصویر پیدا نشد"

    @admin.action(description="تأیید اعضای انتخاب شده")
    def approve_members(self, request, queryset):
        queryset.update(
            membership_status="verified",
            verification_requested=False,
        )

    @admin.action(description="مسدود کردن اعضای انتخاب شده")
    def block_members(self, request, queryset):
        queryset.update(
            membership_status="blocked",
            verification_requested=False,
        )

    @admin.action(description="بازگرداندن به انتظار بررسی")
    def pending_members(self, request, queryset):
        queryset.update(
            membership_status="pending",
            verification_requested=True,
        )


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    list_display = (
        "reporter",
        "reported_user",
        "created_at",
    )

    search_fields = (
        "reporter__username",
        "reported_user__username",
        "reason",
    )

    list_filter = (
        "created_at",
    )

    ordering = ("-created_at",)