# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    """
    فرم ثبت‌نام کاربران جدید
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

    avatar = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label='عکس پروفایل (اختیاری)',
        help_text='حداکثر حجم ۲ مگابایت - فرمت‌های مجاز: jpg, jpeg, png',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام کاربری'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام'
            }),
        }

        help_texts = {
            'username': 'فقط حروف انگلیسی، اعداد و @/./+/-/_ مجاز است.',
        }

    def clean_password2(self):
        """بررسی تطابق دو رمز عبور"""
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError("رمزهای عبور مطابقت ندارند.")
        return cd.get('password2')

    def save(self, commit=True):
        """ذخیره کاربر + پروفایل"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

            # ایجاد یا دریافت پروفایل کاربر
            profile, created = Profile.objects.get_or_create(user=user)

            # ذخیره عکس پروفایل در صورت وجود
            if self.cleaned_data.get('avatar'):
                profile.avatar = self.cleaned_data['avatar']
                profile.save()

        return user


# --------------------------------------------------
# فرم ویرایش پروفایل
# --------------------------------------------------
class ProfileForm(forms.ModelForm):
    """
    فرم ویرایش اطلاعات پروفایل کاربر
    """

    class Meta:
        model = Profile
        fields = [
            'avatar', 'nickname', 'bio', 'child_age',
            'condition_type', 'location',
            'show_bio', 'show_child_age',
            'show_condition_type', 'show_location'
        ]

        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
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
            'avatar': 'عکس پروفایل',
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