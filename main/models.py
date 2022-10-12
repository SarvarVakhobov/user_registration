from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField


class Tag(models.Model):
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return self.tag

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=300, blank=True)
    text = models.TextField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to="post/")
    date_time = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    category = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return self.category

    def get_count(self):
        return self.blog.count()


class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=300, blank=True)
    text = RichTextField(blank=True,null=True)
    image = models.ImageField(upload_to="blog/")
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='blog', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def get_comment_count(self):
        return self.comments.count()


class Comments(models.Model):
    message = models.TextField(max_length=2000, blank=True, null=True)
    author = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)


    def __str__(self):
        return '%s - %s' % (self.author.first_name, self.blog.title)