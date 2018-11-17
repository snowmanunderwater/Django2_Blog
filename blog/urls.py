from django.urls import path

from .views import (
    PostCreate,
    PostDelete,
    PostDetail,
    PostUpdate,
    TagCreate,
    TagDelete,
    TagDetail,
    TagUpdate,
    posts_list,
    tags_list,
)

urlpatterns = [
    path("", posts_list, name="posts_list_url"),
    path("post/create/", PostCreate.as_view(), name="post_create_url"),
    path("posts/<str:slug>/", PostDetail.as_view(), name="post_detail_url"),
    path("posts/<str:slug>/update/", PostUpdate.as_view(), name="post_update_url"),
    path("posts/<str:slug>/delete/", PostDelete.as_view(), name="post_delete_url"),
    path("tags/", tags_list, name="tags_list_url"),
    path("tag/create/", TagCreate.as_view(), name="tag_create_url"),
    path("tag/<str:slug>/", TagDetail.as_view(), name="tag_detail_url"),
    path("tag/<str:slug>/update/", TagUpdate.as_view(), name="tag_update_url"),
    path("tag/<str:slug>/delete/", TagDelete.as_view(), name="tag_delete_url"),
]
