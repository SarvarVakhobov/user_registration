from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response

from accounts.api.serializers import UserSerializer
from main.models import Tag, Comments, Blog, Post, Category
from accounts.models import CustomUser

class TagSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Tag.objects.all())]
    )
    user = serializers.CharField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Tag
        fields = ('tag', 'user')
        

    def create(self, validated_data):

        try:
            if user.user_group <3:
                tag = Tag.objects.create(
                    tag=validated_data['tag'],
                )
                tag.save()
                return tag
        except:
            return Response({"message":"You can not create a tag..."})


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        post = Post.objects.create(
            author=validated_data['author'],
            title=validated_data['title'],
            text=validated_data['text'],
            image=validated_data['image'],
            # date_time=validated_data['date_time'],
            tag=validated_data['tag'],
        )
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.image = validated_data.get('image', instance.image)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.save()
        return instance

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category',)

    def create(self, validated_data):
        category = Category.objects.create(
            category=validated_data['category'],
        )
        category.save()

        return category

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        blog = Blog.objects.create(
            author=validated_data['author'],
            title=validated_data['title'],
            text=validated_data['text'],
            image=validated_data['image'],
            date_time=validated_data['date_time'],
            category=validated_data['category'],
        )

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        return instance


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comments
        fields = '__all__'

    def create(self, validated_data):
        comment = Comments.objects.create(
            message = validated_data['message'],
            author = validated_data['author'],
            blog = validated_data['blog'],
            time = validated_data['time'],
            parent = validated_data['parent'],
        )
        
    