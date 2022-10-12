from django.urls import path

from .views import CreateTagView, CreatePostView, EditPostView

urlpatterns = [
    path("create_tag/", CreateTagView.as_view(), name="create_tag"),
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("edit_post/<str:pk>/", EditPostView.as_view(), name="edit_post"),
]
