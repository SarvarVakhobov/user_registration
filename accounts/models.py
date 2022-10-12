from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from .manager import CustomUserManager


class Specialty(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class CustomUser(AbstractBaseUser):

    USER_CHOICES = (
        (1, 'ADMIN'),
        (2, 'MODERATOR'),
        (3, 'EDITOR'),
        (4, 'USER'),
    )
    email = models.EmailField(verbose_name='email', max_length=80, unique=True)
    phone_number = PhoneNumberField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True, max_length=2000)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null=True)
    user_group = models.PositiveSmallIntegerField(default=4, choices=USER_CHOICES)
    
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    
