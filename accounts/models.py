# =============================================================================
# accounts/models.py
# =============================================================================
"""
مدل‌های اپلیکیشن accounts

این فایل شامل دو مدل اصلی است:
    1. Profile     → اطلاعات تکمیلی هر کاربر
    2. Report      → سیستم گزارش‌دهی کاربران
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# =============================================================================
# اعتبارسنجی‌های سفارشی
# =============================================================================

def validate_image_size(image):
    """
    اعتبارسنجی حجم عکس پروفایل قبل از ذخیره در دیتابیس.

    نکته: فشرده‌سازی واقعی عکس در forms.py انجام می‌شود.
    این تابع فقط محدودیت اولیه حجم فایل آپلود شده را بررسی می‌کند.
    """
    max_size_mb = 5
    max_size_bytes = max_size_mb * 1024 * 1024

    if image.size > max_size_bytes:
        raise ValidationError(
            f"حجم عکس زیاد است. حداکثر حجم مجاز {max_size_mb} مگابایت است."
        )


# =============================================================================
# مدل Profile - اطلاعات تکمیلی کاربر
# =============================================================================

class Profile(models.Model):
    """
    مدل پروفایل کاربر.
    هر کاربر فقط یک پروفایل دارد (رابطه OneToOne).
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name="کاربر"
    )

    # تصویر پروفایل
    avatar = models.ImageField(
        upload_to='avatars/',
        validators=[validate_image_size],
        blank=True,
        null=True,
        verbose_name="عکس پروفایل"
    )

    # اطلاعات شخصی
    nickname = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="نام مستعار"
    )

    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="درباره من"
    )

    # اطلاعات فرزند
    child_age = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="سن فرزند (سال)"
    )

    condition_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نوع معلولیت / شرایط فرزند"
    )

    location = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شهر محل سکونت"
    )

    # تنظیمات نمایش اطلاعات (حریم خصوصی)
    show_bio = models.BooleanField(
        default=True,
        verbose_name="نمایش 'درباره من' به دیگران"
    )

    show_child_age = models.BooleanField(
        default=True,
        verbose_name="نمایش سن فرزند"
    )

    show_condition_type = models.BooleanField(
        default=True,
        verbose_name="نمایش نوع شرایط"
    )

    show_location = models.BooleanField(
        default=True,
        verbose_name="نمایش شهر"
    )

    class Meta:
        verbose_name = "پروفایل کاربر"
        verbose_name_plural = "پروفایل‌های کاربران"

    def __str__(self):
        """نمایش نام نمایشی یا نام کاربری"""
        return self.nickname if self.nickname else self.user.username


# =============================================================================
# مدل Report - سیستم گزارش‌دهی
# =============================================================================

class Report(models.Model):
    """
    مدل گزارش تخلف کاربران.
    برای حفظ امنیت و مدیریت جامعه استفاده می‌شود.
    """

    reporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports_made',
        verbose_name="گزارش دهنده"
    )

    reported_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports_received',
        verbose_name="کاربر گزارش شده"
    )

    reason = models.TextField(
        max_length=500,
        verbose_name="علت گزارش"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ گزارش"
    )

    class Meta:
        verbose_name = "گزارش"
        verbose_name_plural = "گزارش‌ها"
        ordering = ['-created_at']  # جدیدترین گزارش‌ها اول

    def __str__(self):
        return f"گزارش علیه {self.reported_user.username} توسط {self.reporter.username}"