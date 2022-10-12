from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **others):
        if not email:
            raise ValueError(_("Email mast be required!"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **others)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, password, **others):
        others.setdefault('is_staff', True)
        others.setdefault('is_admin', True)
        others.setdefault('is_superuser', True)

        if others.get('is_staff') is not True:
            raise  ValueError(_('SuperUser mast have is_staff = True'))

        if others.get('is_superuser') is not True:
            raise  ValueError(_('SuperUser mast have is_superuser = True'))

        return self.create_user(email, password, **others)

