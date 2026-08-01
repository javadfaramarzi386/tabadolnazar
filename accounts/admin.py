# accounts/admin.py
from django.contrib import admin

from .models import Profile, Report


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
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


    @admin.action(description="تأیید اعضای انتخاب شده")
    def approve_members(self, request, queryset):

        queryset.update(
            membership_status="verified"
        )


    @admin.action(description="مسدود کردن اعضای انتخاب شده")
    def block_members(self, request, queryset):

        queryset.update(
            membership_status="blocked"
        )


    @admin.action(description="بازگرداندن به انتظار بررسی")
    def pending_members(self, request, queryset):

        queryset.update(
            membership_status="pending"
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

    list_filter = ("created_at",)

    ordering = ("-created_at",)