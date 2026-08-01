# accounts/admin.py
from django.contrib import admin

from .models import Profile, Report


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "membership_status",
        "nickname",
        "child_age",
        "condition_type",
        "location",
        "show_bio",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "nickname",
        "location",
        "condition_type",
    )

    list_filter = (
        "membership_status",
        "show_bio",
        "show_child_age",
        "show_condition_type",
        "show_location",
        "created_at",
    )

    ordering = ("-created_at",)


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