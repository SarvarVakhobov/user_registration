from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from accounts.models import CustomUser, Specialty


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('id', 'name',)


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        read_only_fields = ('email',)

    def create(self, validated_data):
        specialty = Specialty.objects.create(
            name = validated_data['name']
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'specialty', 'profile_pic', 'bio', 'user_group', 'is_active',]



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('password', 'password2', 'email', 'first_name', 'last_name', 'phone_number')
        extra_kwargs = {
            # 'first_name': {'required': True},
            # 'last_name': {'required': True},
            # 'phone_number':{'required':True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user



class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'password2')


    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({'password':'Passwords didn\'t macht.'})
        return super().validate(attrs)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'old_password':"Old password isn\'t correct."})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance

class ChangeUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'specialty', 'profile_pic', 'bio', 'user_group', 'is_active')

    def update(self, instance, validated_data):
        instance.specialty = validated_data.get('specialty', instance.specialty)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.user_group = validated_data.get('user_group', instance.user_group)
        instance.is_active =  True
        instance.save()
        return instance