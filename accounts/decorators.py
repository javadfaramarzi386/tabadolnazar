from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps


def verified_member_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        profile = request.user.profile

        if profile.membership_status == "verified":
            return view_func(request, *args, **kwargs)

        if profile.membership_status == "blocked":
            messages.error(
                request,
                "حساب شما مسدود شده است. برای پیگیری با مدیریت تماس بگیرید."
            )

        else:
            messages.warning(
                request,
                "حساب شما هنوز تأیید نشده است. پس از بررسی عضویت، امکان مشارکت فعال خواهد شد."
            )

        return redirect("forum:post_list")

    return wrapper