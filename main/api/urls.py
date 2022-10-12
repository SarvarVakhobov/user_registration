from django.urls import path

from .views import CreateTagView, TagListView, CreatePostView, PostView, PostListView, EditPostView

urlpatterns = [
    path("create_tag/", CreateTagView.as_view(), name="create_tag"),
    path("tag_list/", TagListView.as_view(), name="tag_list"),

    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("post/<str:pk>/", PostView.as_view(), name="post"),
    path("post_list/", PostListView.as_view(), name="post_list"),
    path("edit_post/<str:pk>/", EditPostView.as_view(), name="edit_post"),

    
]
