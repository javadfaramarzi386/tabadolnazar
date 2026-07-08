# =============================================================================
# accounts/urls.py
# =============================================================================
"""
مسیرهای URL اپلیکیشن accounts

این فایل تمام آدرس‌های مربوط به احراز هویت، پروفایل و گزارش‌دهی را مدیریت می‌کند.
"""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

# نام‌گذاری فضای URL برای جلوگیری از تداخل با اپ‌های دیگر
app_name = 'accounts'


urlpatterns = [
    # =====================================================================
    # احراز هویت (Authentication)
    # =====================================================================

    # ثبت‌نام کاربر جدید
    path('register/', views.register, name='register'),

    # ورود کاربر (استفاده از ویو آماده جنگو)
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            redirect_authenticated_user=True,      # اگر قبلاً وارد شده، ریدایرکت شود
            extra_context={'title': 'ورود به حساب کاربری'}
        ),
        name='login'
    ),

    # خروج کاربر
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='home'),  # بعد از خروج به صفحه اصلی برود
        name='logout'
    ),

    # =====================================================================
    # بازیابی رمز عبور (Password Reset)
    # =====================================================================

    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html',
            subject_template_name='registration/password_reset_subject.txt',
            email_template_name='registration/password_reset_email.html',
            success_url='/accounts/password-reset/done/'
        ),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

    # =====================================================================
    # پروفایل کاربران
    # =====================================================================

    # پروفایل کاربر فعلی (خودم)
    path('profile/', views.profile_view, name='profile'),

    # ویرایش پروفایل کاربر فعلی
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    # مشاهده پروفایل سایر کاربران
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),

    # =====================================================================
    # گزارش‌دهی
    # =====================================================================

    # گزارش دادن به کاربر خاص
    path('profile/<str:username>/report/', views.report_user, name='report_user'),
]