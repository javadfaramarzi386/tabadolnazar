# accounts/models.py

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def validate_image_size(image):
    max_size_mb = 5
    max_size_bytes = max_size_mb * 1024 * 1024

    if image.size > max_size_bytes:
        raise ValidationError(
            f"حجم عکس زیاد است. حداکثر حجم مجاز {max_size_mb} مگابایت است."
        )


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="کاربر",
    )
    MEMBERSHIP_STATUS = [
        ("pending", "در انتظار بررسی"),
        ("verified", "عضو تأیید شده"),
        ("blocked", "مسدود شده"),
    ]

    membership_status = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_STATUS,
        default="pending",
        verbose_name="وضعیت عضویت",
    )

    avatar = models.ImageField(
        upload_to="avatars/",
        validators=[validate_image_size],
        blank=True,
        null=True,
        verbose_name="عکس پروفایل",
    )

    nickname = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="نام مستعار",
    )

    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="درباره من",
    )

    child_age = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="سن فرزند (سال)",
    )

    condition_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نوع معلولیت / شرایط فرزند",
    )

    location = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شهر محل سکونت",
    )

    show_bio = models.BooleanField(
        default=True,
        verbose_name="نمایش 'درباره من' به دیگران",
    )

    show_child_age = models.BooleanField(
        default=True,
        verbose_name="نمایش سن فرزند",
    )

    show_condition_type = models.BooleanField(
        default=True,
        verbose_name="نمایش نوع شرایط",
    )

    show_location = models.BooleanField(
        default=True,
        verbose_name="نمایش شهر",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین ویرایش",
    )

    class Meta:
        verbose_name = "پروفایل کاربر"
        verbose_name_plural = "پروفایل‌های کاربران"

    def __str__(self):
        return self.nickname or self.user.username


class Report(models.Model):

    reporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reports_made",
        verbose_name="گزارش دهنده",
    )

    reported_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reports_received",
        verbose_name="کاربر گزارش شده",
    )

    reason = models.TextField(
        max_length=500,
        verbose_name="علت گزارش",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ گزارش",
    )

    class Meta:
        verbose_name = "گزارش"
        verbose_name_plural = "گزارش‌ها"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"گزارش علیه {self.reported_user.username} "
            f"توسط {self.reporter.username}"
        )