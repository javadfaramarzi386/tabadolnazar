# forum/forms.py

from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "content", "category"]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "عنوان موضوع را وارد کنید",
                    "autofocus": True,
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                    "placeholder": "متن خود را اینجا بنویسید...",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }

        labels = {
            "title": "عنوان موضوع",
            "content": "متن پست",
            "category": "دسته‌بندی",
        }

        help_texts = {
            "content": "متن پست باید حداقل ۲۰ کاراکتر باشد.",
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "نظر خود را بنویسید...",
                }
            ),
        }

        labels = {
            "content": "متن نظر",
        }