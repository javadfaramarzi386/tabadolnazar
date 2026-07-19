from django.contrib.auth.models import User
from django.test import TestCase

from .models import Category, Post

from django.urls import reverse


class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

        self.category = Category.objects.create(
            name="برنامه‌نویسی"
        )

        self.post = Post.objects.create(
            title="عنوان تست",
            content="متن تست پست",
            author=self.user,
            category=self.category,
        )

    def test_post_creation(self):
        """بررسی ایجاد صحیح یک پست."""
        self.assertEqual(self.post.title, "عنوان تست")
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.category, self.category)

    def test_increase_views(self):
        """بررسی افزایش تعداد بازدید."""
        self.assertEqual(self.post.views, 0)

        self.post.increase_views()

        self.post.refresh_from_db()

        self.assertEqual(self.post.views, 1)

    def test_total_likes(self):
        """بررسی تعداد لایک‌ها."""
        self.assertEqual(self.post.total_likes, 0)

        self.post.likes.add(self.user)

        self.assertEqual(self.post.total_likes, 1)

    def test_total_comments_without_comments(self):
        """بررسی تعداد کامنت‌ها در صورت نبود کامنت تأییدشده."""
        self.assertEqual(self.post.total_comments, 0)

    def test_authenticated_user_can_like_post(self):
        """کاربر واردشده می‌تواند پست را لایک کند."""
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("forum:like_post", args=[self.post.pk])
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            self.post.likes.filter(pk=self.user.pk).exists()
        )

    def test_authenticated_user_can_unlike_post(self):
        """کاربر می‌تواند لایک خود را لغو کند."""
        self.post.likes.add(self.user)

        self.client.force_login(self.user)

        self.client.post(
            reverse("forum:like_post", args=[self.post.pk])
        )

        self.assertFalse(
            self.post.likes.filter(pk=self.user.pk).exists()
        )

    def test_get_request_is_not_allowed_for_like(self):
        """لایک کردن با GET مجاز نیست."""
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("forum:like_post", args=[self.post.pk])
        )

        self.assertEqual(response.status_code, 405)
