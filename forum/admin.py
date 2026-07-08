# =============================================================================
# forum/admin.py
# =============================================================================
"""
پنل مدیریت جنگو - اپلیکیشن forum

این فایل تنظیمات نمایش، جستجو، فیلتر و مدیریت مدل‌های
Category, Post و Comment را در پنل ادمین مشخص می‌کند.
"""

from django.contrib import admin
from .models import Category, Post, Comment


# =============================================================================
# مدیریت دسته‌بندی‌ها (Category)
# =============================================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    تنظیمات نمایش و مدیریت دسته‌بندی‌های论坛 در پنل ادمین.
    """
    # ستون‌های نمایش داده شده در لیست
    list_display = (
        'name',
        'parent',
        'display_order',
        'is_active',
        'slug',
    )

    # فیلترهای سمت راست پنل
    list_filter = (
        'is_active',
        'parent',
    )

    # فیلدهای قابل جستجو
    search_fields = (
        'name',
        'description',
    )

    # تولید خودکار slug بر اساس نام
    prepopulated_fields = {
        'slug': ('name',)
    }

    # ترتیب نمایش
    ordering = ('display_order', 'name')

    # فیلدهای فقط خواندنی (اختیاری)
    # readonly_fields = ('slug',)


# =============================================================================
# مدیریت پست‌ها (Post)
# =============================================================================

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    تنظیمات نمایش و مدیریت پست‌های فروم در پنل ادمین.
    """
    # ستون‌های جدول لیست پست‌ها
    list_display = (
        'title',
        'author',
        'category',
        'created_at',
        'is_approved',
        'total_likes',
        'total_comments',
    )

    # فیلترهای سمت راست
    list_filter = (
        'category',
        'is_approved',
        'created_at',
    )

    # فیلدهای جستجو
    search_fields = (
        'title',
        'content',
        'author__username',
    )

    # فیلدهایی که فقط قابل مشاهده هستند (قابل ویرایش نیستند)
    readonly_fields = (
        'created_at',
        'updated_at',
        'total_likes',      # اگر متد محاسبه‌ای باشد
        'total_comments',
    )

    # ترتیب نمایش (جدیدترین پست‌ها اول)
    ordering = ('-created_at',)

    # امکان ویرایش سریع برخی فیلدها در لیست
    # list_editable = ('is_approved',)


# =============================================================================
# مدیریت نظرات (Comment)
# =============================================================================

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    تنظیمات نمایش و مدیریت کامنت‌های کاربران در پنل ادمین.
    """
    # ستون‌های نمایش
    list_display = (
        'author',
        'post',
        'created_at',
        'is_approved',
    )

    # فیلترها
    list_filter = (
        'is_approved',
        'created_at',
    )

    # جستجو
    search_fields = (
        'content',
        'author__username',
        'post__title',
    )

    # فیلدهای فقط خواندنی
    readonly_fields = (
        'created_at',
    )

    # ترتیب نمایش
    ordering = ('-created_at',)


# =============================================================================
# نکات آموزشی و بهترین شیوه‌ها
# =============================================================================
"""
نکات مهم برای توسعه‌دهندگان:

1. list_display: فقط فیلدهای مهم و پراستفاده را نمایش دهید.
2. search_fields: از ارتباط با مدل‌های دیگر با "__" استفاده کنید (author__username).
3. readonly_fields: برای فیلدهای محاسباتی یا تاریخ‌ها استفاده شود.
4. prepopulated_fields: برای تولید خودکار slug بسیار مفید است.
5. actions: می‌توانید اقدامات گروهی (مثل تأیید دسته‌ای پست‌ها) اضافه کنید.

در آینده می‌توانید:
- list_editable اضافه کنید
- action سفارشی برای تأیید/رد پست و کامنت بسازید
- Inline برای نمایش کامنت‌ها داخل پست تعریف کنید
"""