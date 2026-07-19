# forum/urls.py

from django.urls import path

from . import views


app_name = "forum"


urlpatterns = [
    path("", views.post_list, name="post_list"),

    path(
        "category/<slug:slug>/",
        views.category_posts,
        name="category_posts",
    ),

    path(
        "post/<int:pk>/",
        views.post_detail,
        name="post_detail",
    ),

    path(
        "post/create/",
        views.create_post,
        name="create_post",
    ),

    path(
        "post/<int:pk>/edit/",
        views.edit_post,
        name="edit_post",
    ),

    path(
        "post/<int:pk>/delete/",
        views.delete_post,
        name="delete_post",
    ),

    path(
        "post/<int:pk>/like/",
        views.like_post,
        name="like_post",
    ),
]