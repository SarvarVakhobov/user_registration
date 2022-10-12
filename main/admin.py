from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post, Blog, Tag, Comments, Category


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comments)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_time']
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = '__all__'