from django.contrib import admin
from .models import CustomUser, Specialty

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Specialty)