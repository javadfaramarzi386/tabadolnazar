# accounts/views.py

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileForm, UserRegistrationForm
from .models import Profile, Report


def register(request):
    """Register a new user."""

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserRegistrationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            user = form.save()

            messages.success(
                request,
                "ثبت‌نام با موفقیت انجام شد. خوش آمدید!"
            )

            login(
                request,
                user,
                backend="django.contrib.auth.backends.ModelBackend"
            )

            return redirect("home")

    else:
        form = UserRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
            "title": "ثبت‌نام در سایت",
        }
    )


@login_required
def profile_view(request):
    """Redirect the user to their own profile."""

    return redirect(
        "accounts:profile_detail",
        username=request.user.username
    )


def profile_detail(request, username):
    """Display a user's profile."""

    target_user = get_object_or_404(
        User,
        username=username
    )

    profile, _ = Profile.objects.get_or_create(
        user=target_user
    )

    is_own_profile = request.user == target_user

    return render(
        request,
        "accounts/profile_detail.html",
        {
            "target_profile": profile,
            "target_user": target_user,
            "is_own_profile": is_own_profile,
            "title": (
                f"پروفایل "
                f"{target_user.get_full_name() or target_user.username}"
            ),
        }
    )


@login_required
def edit_profile(request):
    """Edit the current user's profile."""

    profile, _ = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "پروفایل شما با موفقیت بروزرسانی شد."
            )

            return redirect(
                "accounts:profile_detail",
                username=request.user.username
            )

    else:
        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        "accounts/edit_profile.html",
        {
            "form": form,
            "title": "ویرایش پروفایل",
        }
    )


@login_required
def report_user(request, username):
    """Create a report against another user."""

    reported_user = get_object_or_404(
        User,
        username=username
    )

    if reported_user == request.user:
        messages.error(
            request,
            "نمی‌توانید خودتان را گزارش دهید."
        )

        return redirect(
            "accounts:profile_detail",
            username=username
        )

    if request.method == "POST":
        reason = request.POST.get(
            "reason",
            ""
        ).strip()

        if not reason:
            messages.error(
                request,
                "لطفاً دلیل گزارش را وارد کنید."
            )

            return redirect(
                "accounts:profile_detail",
                username=username
            )

        if len(reason) < 10:
            messages.error(
                request,
                "دلیل گزارش باید حداقل ۱۰ کاراکتر باشد."
            )

            return redirect(
                "accounts:profile_detail",
                username=username
            )

        if Report.objects.filter(
            reporter=request.user,
            reported_user=reported_user,
            reason=reason
        ).exists():

            messages.warning(
                request,
                "شما قبلاً این گزارش را ثبت کرده‌اید."
            )

            return redirect(
                "accounts:profile_detail",
                username=username
            )

        Report.objects.create(
            reporter=request.user,
            reported_user=reported_user,
            reason=reason
        )

        messages.success(
            request,
            "گزارش شما با موفقیت ثبت شد. بررسی خواهد شد."
        )

        return redirect(
            "accounts:profile_detail",
            username=username
        )

    return render(
        request,
        "accounts/report_user.html",
        {
            "reported_user": reported_user,
            "title": f"گزارش کاربر {reported_user.username}",
        }
    )

def password_reset_success(request):
    messages.success(
        request,
        "رمز عبور شما با موفقیت تغییر کرد. اکنون می‌توانید وارد حساب کاربری شوید."
    )
    return redirect("home")

def home_page(request):
    """Render the home page."""

    return render(
        request,
        "accounts/home.html",
        {
            "title": "خانه",
        }
    )