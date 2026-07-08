# =============================================================================
# forum/urls.py
# =============================================================================
"""
مسیرهای URL اپلیکیشن forum

این فایل تمام آدرس‌های مربوط به فروم (دسته‌بندی‌ها، پست‌ها، ایجاد، ویرایش و تعاملات) را مدیریت می‌کند.
"""

from django.urls import path
from . import views

# Namespace برای جلوگیری از تداخل با اپ‌های دیگر
# بسیار مهم برای استفاده از {% url 'forum:post_detail' %} در قالب‌ها
app_name = 'forum'


urlpatterns = [
    # =====================================================================
    # صفحات اصلی فروم
    # =====================================================================

    # صفحه اصلی فروم - لیست همه پست‌ها
    path('', views.post_list, name='post_list'),

    # نمایش پست‌های یک دسته‌بندی خاص (SEO Friendly)
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),

    # =====================================================================
    # مدیریت پست‌ها
    # =====================================================================

    # جزئیات یک پست خاص
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # ایجاد پست جدید
    path('post/create/', views.create_post, name='create_post'),

    # ویرایش پست موجود
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),

    # حذف پست
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),

    # =====================================================================
    # تعاملات کاربر (Interactions)
    # =====================================================================

    # لایک کردن /取消 لایک پست (Toggle)
    path('post/<int:pk>/like/', views.like_post, name='like_post'),

    # =====================================================================
    # مسیرهای آینده (برای کامنت‌ها)
    # =====================================================================
    # path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    # path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]