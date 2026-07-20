from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Profile, Report, validate_image_size


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        self.profile, created = Profile.objects.get_or_create(
            user=self.user
        )

        self.profile.nickname = "کاربر تست"
        self.profile.bio = "متن درباره کاربر"
        self.profile.child_age = 10
        self.profile.condition_type = "شرایط تست"
        self.profile.location = "تهران"
        self.profile.save()

    def test_profile_creation(self):
        """بررسی ایجاد صحیح پروفایل."""

        self.assertEqual(
            self.profile.user,
            self.user,
        )

        self.assertEqual(
            self.profile.nickname,
            "کاربر تست",
        )

        self.assertEqual(
            str(self.profile),
            "کاربر تست",
        )

    def test_profile_str_without_nickname(self):
        """بررسی نمایش نام کاربری در صورت نبود نام مستعار."""

        self.profile.nickname = ""
        self.profile.save()

        self.assertEqual(
            str(self.profile),
            "testuser",
        )

    def test_profile_default_privacy_settings(self):
        """بررسی تنظیمات پیش‌فرض حریم خصوصی پروفایل."""

        another_user = User.objects.create_user(
            username="anotheruser",
            password="password123",
        )

        profile, created = Profile.objects.get_or_create(
            user=another_user
        )

        self.assertTrue(profile.show_bio)
        self.assertTrue(profile.show_child_age)
        self.assertTrue(profile.show_condition_type)
        self.assertTrue(profile.show_location)

    def test_profile_one_to_one_relationship(self):
        """بررسی رابطه یک‌به‌یک پروفایل با کاربر."""

        self.assertEqual(
            self.user.profile,
            self.profile,
        )


class ReportModelTest(TestCase):

    def setUp(self):
        self.reporter = User.objects.create_user(
            username="reporter",
            password="password123",
        )

        self.reported_user = User.objects.create_user(
            username="reported",
            password="password123",
        )

        self.report = Report.objects.create(
            reporter=self.reporter,
            reported_user=self.reported_user,
            reason="این یک دلیل تستی برای گزارش کاربر است.",
        )

    def test_report_creation(self):
        """بررسی ایجاد صحیح گزارش."""

        self.assertEqual(
            self.report.reporter,
            self.reporter,
        )

        self.assertEqual(
            self.report.reported_user,
            self.reported_user,
        )

        self.assertEqual(
            self.report.reason,
            "این یک دلیل تستی برای گزارش کاربر است.",
        )

    def test_report_str(self):
        """بررسی متن نمایشی گزارش."""

        self.assertEqual(
            str(self.report),
            "گزارش علیه reported توسط reporter",
        )

    def test_report_ordering(self):
        """بررسی مرتب‌سازی گزارش‌ها بر اساس تاریخ نزولی."""

        reports = Report.objects.all()

        self.assertEqual(
            reports.first(),
            self.report,
        )


class ImageValidationTest(TestCase):

    def test_valid_image_size(self):
        """بررسی پذیرش عکس با حجم مجاز."""

        image = SimpleUploadedFile(
            "test.jpg",
            b"0" * (1024 * 1024),
            content_type="image/jpeg",
        )

        validate_image_size(image)

    def test_invalid_image_size(self):
        """بررسی رد عکس بزرگ‌تر از ۵ مگابایت."""

        image = SimpleUploadedFile(
            "large.jpg",
            b"0" * (6 * 1024 * 1024),
            content_type="image/jpeg",
        )

        with self.assertRaises(ValidationError):
            validate_image_size(image)


class RegisterViewTest(TestCase):

    def test_anonymous_user_can_access_register_page(self):
        """کاربر مهمان می‌تواند صفحه ثبت‌نام را ببیند."""

        response = self.client.get(
            reverse("accounts:register")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_authenticated_user_is_redirected_from_register(self):
        """کاربر واردشده نمی‌تواند دوباره ثبت‌نام کند."""

        user = User.objects.create_user(
            username="testuser",
            password="password123",
        )

        self.client.force_login(user)

        response = self.client.get(
            reverse("accounts:register")
        )

        self.assertRedirects(
            response,
            reverse("home"),
        )


class ProfileViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )

    def test_profile_view_is_accessible(self):
        """بررسی دسترسی به صفحه پروفایل."""

        response = self.client.get(
            reverse(
                "accounts:profile_detail",
                args=["testuser"],
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_profile_detail_creates_profile_if_not_exists(self):
        """بررسی وجود پروفایل کاربر."""

        response = self.client.get(
            reverse(
                "accounts:profile_detail",
                args=["testuser"],
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTrue(
            Profile.objects.filter(
                user=self.user
            ).exists()
        )


class EditProfileViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )

        self.client.force_login(self.user)

    def test_edit_profile_page_is_accessible(self):
        """صفحه ویرایش پروفایل برای کاربر واردشده قابل دسترسی است."""

        response = self.client.get(
            reverse("accounts:edit_profile")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_edit_profile_updates_profile(self):
        """بررسی به‌روزرسانی اطلاعات پروفایل."""

        response = self.client.post(
            reverse("accounts:edit_profile"),
            {
                "nickname": "نام جدید",
                "bio": "بیوگرافی جدید",
                "child_age": 12,
                "condition_type": "شرایط جدید",
                "location": "اصفهان",
                "show_bio": True,
                "show_child_age": True,
                "show_condition_type": True,
                "show_location": True,
            },
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        profile = Profile.objects.get(
            user=self.user
        )

        self.assertEqual(
            profile.nickname,
            "نام جدید",
        )

        self.assertEqual(
            profile.location,
            "اصفهان",
        )


class ReportViewTest(TestCase):

    def setUp(self):
        self.reporter = User.objects.create_user(
            username="reporter",
            password="password123",
        )

        self.reported_user = User.objects.create_user(
            username="reported",
            password="password123",
        )

        self.client.force_login(
            self.reporter
        )

    def test_report_page_is_accessible(self):
        """کاربر واردشده می‌تواند صفحه گزارش را ببیند."""

        response = self.client.get(
            reverse(
                "accounts:report_user",
                args=["reported"],
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_user_cannot_report_themselves(self):
        """کاربر نمی‌تواند خودش را گزارش کند."""

        response = self.client.post(
            reverse(
                "accounts:report_user",
                args=["reporter"],
            ),
            {
                "reason": "این یک دلیل تستی برای گزارش کاربر است.",
            },
        )

        self.assertRedirects(
            response,
            reverse(
                "accounts:profile_detail",
                args=["reporter"],
            ),
        )

        self.assertEqual(
            Report.objects.count(),
            0,
        )

    def test_empty_reason_is_rejected(self):
        """گزارش بدون دلیل پذیرفته نمی‌شود."""

        response = self.client.post(
            reverse(
                "accounts:report_user",
                args=["reported"],
            ),
            {
                "reason": "",
            },
        )

        self.assertRedirects(
            response,
            reverse(
                "accounts:profile_detail",
                args=["reported"],
            ),
        )

        self.assertEqual(
            Report.objects.count(),
            0,
        )

    def test_short_reason_is_rejected(self):
        """دلیل کمتر از ۱۰ کاراکتر پذیرفته نمی‌شود."""

        response = self.client.post(
            reverse(
                "accounts:report_user",
                args=["reported"],
            ),
            {
                "reason": "کوتاه",
            },
        )

        self.assertRedirects(
            response,
            reverse(
                "accounts:profile_detail",
                args=["reported"],
            ),
        )

        self.assertEqual(
            Report.objects.count(),
            0,
        )

    def test_valid_report_is_created(self):
        """گزارش معتبر با موفقیت ثبت می‌شود."""

        reason = "این یک دلیل معتبر برای گزارش کاربر است."

        response = self.client.post(
            reverse(
                "accounts:report_user",
                args=["reported"],
            ),
            {
                "reason": reason,
            },
        )

        self.assertRedirects(
            response,
            reverse(
                "accounts:profile_detail",
                args=["reported"],
            ),
        )

        self.assertTrue(
            Report.objects.filter(
                reporter=self.reporter,
                reported_user=self.reported_user,
                reason=reason,
            ).exists()
        )

    def test_duplicate_report_is_not_created(self):
        """گزارش تکراری با همان دلیل دوباره ثبت نمی‌شود."""

        reason = "این یک دلیل معتبر برای گزارش کاربر است."

        Report.objects.create(
            reporter=self.reporter,
            reported_user=self.reported_user,
            reason=reason,
        )

        self.client.post(
            reverse(
                "accounts:report_user",
                args=["reported"],
            ),
            {
                "reason": reason,
            },
        )

        self.assertEqual(
            Report.objects.count(),
            1,
        )


class HomePageTest(TestCase):

    def test_home_page_is_accessible(self):
        """بررسی دسترسی به صفحه اصلی."""

        response = self.client.get(
            reverse("home")
        )

        self.assertEqual(
            response.status_code,
            200,
        )