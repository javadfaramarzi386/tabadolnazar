# accounts/forms.py

from io import BytesIO

from PIL import Image

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator

from .models import Profile


def validate_avatar_size(image):
    max_size = 5 * 1024 * 1024

    if image.size > max_size:
        raise ValidationError(
            "حجم عکس زیاد است. حداکثر حجم مجاز ۵ مگابایت است."
        )


def compress_avatar(image):
    img = Image.open(image)

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.thumbnail((300, 300))

    output = BytesIO()

    img.save(
        output,
        format="JPEG",
        quality=75,
        optimize=True,
    )

    output.seek(0)

    return InMemoryUploadedFile(
        output,
        "ImageField",
        f"{image.name.rsplit('.', 1)[0]}.jpg",
        "image/jpeg",
        output.getbuffer().nbytes,
        None,
    )


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "رمز عبور",
            }
        ),
        label="رمز عبور",
        help_text="رمز عبور حداقل ۸ کاراکتر باشد.",
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "تکرار رمز عبور",
            }
        ),
        label="تکرار رمز عبور",
    )

    accept_charter = forms.BooleanField(
        required=True,
        label="منشور انجمن را مطالعه کرده‌ام و با آن موافقم.",
        error_messages={
            "required": "برای ثبت‌نام باید منشور انجمن را بپذیرید."
        },
    )


    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "ایمیل",
            }
        ),
        label="ایمیل",
    )


    avatar = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="عکس پروفایل (اختیاری)",
        help_text="حداکثر ۵ مگابایت - فرمت‌های مجاز: jpg, jpeg, png",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png"]
            ),
            validate_avatar_size,
        ],
    )


    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "first_name",
        ]


        widgets = {

            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نام کاربری",
                }
            ),

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نام",
                }
            ),
        }


        help_texts = {

            "username":
                "فقط حروف انگلیسی، اعداد و @/./+/-/_ مجاز است.",

        }



    def clean_username(self):

        username = self.cleaned_data.get(
            "username",
            ""
        ).strip()


        reserved = {
            "admin",
            "administrator",
            "root",
            "support",
            "system",
            "manager",
            "moderator",
            "superuser",
        }


        if username.lower() in reserved:

            raise forms.ValidationError(
                "انتخاب این نام کاربری مجاز نیست."
            )


        if User.objects.filter(
            username__iexact=username
        ).exists():

            raise forms.ValidationError(
                "این نام کاربری قبلاً ثبت شده است."
            )


        return username



    def clean_email(self):

        email = self.cleaned_data.get(
            "email",
            ""
        ).strip().lower()


        if User.objects.filter(
            email__iexact=email
        ).exists():

            raise forms.ValidationError(
                "این ایمیل قبلاً برای یک حساب کاربری استفاده شده است."
            )


        return email



    def clean_avatar(self):

        image = self.cleaned_data.get(
            "avatar"
        )


        if image:

            return compress_avatar(image)


        return image



    def clean_password(self):

        password = self.cleaned_data.get(
            "password"
        )


        if password:

            validate_password(password)


        return password



    def clean_password2(self):

        password = self.cleaned_data.get(
            "password"
        )

        password2 = self.cleaned_data.get(
            "password2"
        )


        if password and password2:

            if password != password2:

                raise forms.ValidationError(
                    "رمزهای عبور مطابقت ندارند."
                )


        return password2



    def save(self, commit=True):

        user = super().save(
            commit=False
        )


        user.set_password(
            self.cleaned_data["password"]
        )


        if commit:

            user.save()


            profile, _ = Profile.objects.get_or_create(
                user=user
            )


            if self.cleaned_data.get("avatar"):

                profile.avatar = self.cleaned_data["avatar"]

                profile.save()


        return user

class MembershipVerificationForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = [
            "relationship_to_child",
            "child_age",
            "condition_type",
            "location",
            "verification_note",
        ]

        widgets = {

            "relationship_to_child": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "مثلاً مادر، پدر، سرپرست",
                }
            ),

            "child_age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "سن کودک",
                }
            ),

            "condition_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نوع شرایط یا نیاز ویژه",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "شهر محل سکونت",
                }
            ),

            "verification_note": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "توضیحی برای مدیر انجمن",
                }
            ),
        }
class ProfileForm(forms.ModelForm):

    avatar = forms.ImageField(
        required=False,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png"]
            ),
            validate_avatar_size,
        ],
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control"}
        ),
        label="عکس پروفایل",
        help_text="حداکثر حجم ۵ مگابایت",
    )

    class Meta:
        model = Profile

        fields = [
            "avatar",
            "nickname",
            "bio",
            "child_age",
            "condition_type",
            "location",
            "show_bio",
            "show_child_age",
            "show_condition_type",
            "show_location",
        ]

        widgets = {
            "nickname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نام مستعار (اختیاری)",
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "درباره خودتان و فرزندتان بنویسید...",
                }
            ),
            "child_age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                    "max": 18,
                }
            ),
            "condition_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "مثال: اوتیسم، فلج مغزی، سندرم داون و ...",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "شهر محل سکونت",
                }
            ),
        }

        labels = {
            "nickname": "نام مستعار",
            "bio": "درباره من",
            "child_age": "سن فرزند (سال)",
            "condition_type": "نوع معلولیت / شرایط فرزند",
            "location": "شهر",
            "show_bio": 'نمایش "درباره من" به دیگران',
            "show_child_age": "نمایش سن فرزند",
            "show_condition_type": "نمایش نوع شرایط",
            "show_location": "نمایش شهر",
        }

    def clean_avatar(self):
        image = self.cleaned_data.get("avatar")

        if image:
            return compress_avatar(image)

        return image

    def clean_child_age(self):
        age = self.cleaned_data.get("child_age")

        if age is None:
            return None

        if age < 0 or age > 18:
            raise forms.ValidationError(
                "سن فرزند باید بین ۰ تا ۱۸ سال باشد."
            )

        return age