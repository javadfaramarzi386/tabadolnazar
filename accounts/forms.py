# =============================================================================
# accounts/forms.py
# =============================================================================
"""
فرم‌های اپلیکیشن accounts

این فایل شامل فرم‌های ثبت‌نام کاربر جدید و ویرایش پروفایل است.
تمام اعتبارسنجی‌ها، فشرده‌سازی عکس و منطق ذخیره‌سازی در این فایل مدیریت می‌شود.
"""

from django import forms
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Profile


# =============================================================================
# توابع اعتبارسنجی و پردازش عکس پروفایل
# =============================================================================

def validate_avatar_size(image):
    """
    اعتبارسنجی حجم عکس پروفایل.

    حداکثر حجم مجاز: ۵ مگابایت
    """
    max_size = 5 * 1024 * 1024  # 5 MB

    if image.size > max_size:
        raise ValidationError(
            "حجم عکس زیاد است. حداکثر حجم مجاز ۵ مگابایت است."
        )


def compress_avatar(image):
    """
    فشرده‌سازی و بهینه‌سازی عکس پروفایل قبل از ذخیره در دیتابیس.

    عملیات انجام شده:
        - تبدیل فرمت‌های RGBA به RGB
        - کاهش ابعاد به حداکثر 300×300 پیکسل
        - کاهش کیفیت به 75%
        - تبدیل به فرمت JPEG
    """
    img = Image.open(image)

    # تبدیل عکس‌های شفاف به RGB
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # تغییر اندازه
    img.thumbnail((300, 300))

    output = BytesIO()
    img.save(
        output,
        format='JPEG',
        quality=75,
        optimize=True
    )

    output.seek(0)

    return InMemoryUploadedFile(
        output,
        'ImageField',
        f"{image.name.rsplit('.', 1)[0]}.jpg",
        'image/jpeg',
        output.getbuffer().nbytes,
        None
    )


# =============================================================================
# فرم ثبت‌نام کاربر جدید
# =============================================================================

class UserRegistrationForm(forms.ModelForm):
    """
    فرم ثبت‌نام کاربر جدید.
    شامل ایجاد کاربر در مدل User و پروفایل مربوطه در مدل Profile.
    """

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور'
        }),
        label='رمز عبور',
        help_text='رمز عبور حداقل ۸ کاراکتر باشد.'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تکرار رمز عبور'
        }),
        label='تکرار رمز عبور'
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }),
        label='ایمیل'
    )

    avatar = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label='عکس پروفایل (اختیاری)',
        help_text='حداکثر ۵ مگابایت - فرمت‌های مجاز: jpg, jpeg, png',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_avatar_size
        ]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام کاربری'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام'
            }),
        }

        help_texts = {
            'username': 'فقط حروف انگلیسی، اعداد و @/./+/-/_ مجاز است.',
        }

    def clean_email(self):
        """جلوگیری از ثبت ایمیل تکراری"""
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلاً ثبت شده است.")
        return email

    def clean_avatar(self):
        """فشرده‌سازی عکس در صورت آپلود"""
        image = self.cleaned_data.get('avatar')
        if image:
            return compress_avatar(image)
        return image

    def clean_password2(self):
        """بررسی تطابق دو رمز عبور"""
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError("رمزهای عبور مطابقت ندارند.")
        return cd.get('password2')

    def save(self, commit=True):
        """
        ذخیره کاربر + ایجاد پروفایل اتوماتیک
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

            # ایجاد پروفایل برای کاربر جدید
            profile, _ = Profile.objects.get_or_create(user=user)

            if self.cleaned_data.get('avatar'):
                profile.avatar = self.cleaned_data['avatar']
                profile.save()

        return user


# =============================================================================
# فرم ویرایش پروفایل
# =============================================================================

class ProfileForm(forms.ModelForm):
    """
    فرم ویرایش اطلاعات پروفایل کاربر.
    """

    avatar = forms.ImageField(
        required=False,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_avatar_size
        ],
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label='عکس پروفایل',
        help_text='حداکثر حجم ۵ مگابایت'
    )

    class Meta:
        model = Profile
        fields = [
            'avatar',
            'nickname',
            'bio',
            'child_age',
            'condition_type',
            'location',
            'show_bio',
            'show_child_age',
            'show_condition_type',
            'show_location'
        ]

        widgets = {
            'nickname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام مستعار (اختیاری)'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'درباره خودتان و فرزندتان بنویسید...'
            }),
            'child_age': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 18
            }),
            'condition_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'مثال: اوتیسم، فلج مغزی، سندرم داون و ...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'شهر محل سکونت'
            }),
        }

        labels = {
            'nickname': 'نام مستعار',
            'bio': 'درباره من',
            'child_age': 'سن فرزند (سال)',
            'condition_type': 'نوع معلولیت / شرایط فرزند',
            'location': 'شهر',
            'show_bio': 'نمایش "درباره من" به دیگران',
            'show_child_age': 'نمایش سن فرزند',
            'show_condition_type': 'نمایش نوع شرایط',
            'show_location': 'نمایش شهر',
        }

    def clean_avatar(self):
        """فشرده‌سازی عکس در صورت تغییر"""
        image = self.cleaned_data.get('avatar')
        if image:
            return compress_avatar(image)
        return image

    def clean_child_age(self):
        """اعتبارسنجی سن فرزند"""
        age = self.cleaned_data.get('child_age')

        if age is None:
            return None

        try:
            age = int(age)
        except (ValueError, TypeError):
            raise forms.ValidationError("سن فرزند باید یک عدد صحیح باشد.")

        if age < 0 or age > 18:
            raise forms.ValidationError("سن فرزند باید بین ۰ تا ۱۸ سال باشد.")

        return age