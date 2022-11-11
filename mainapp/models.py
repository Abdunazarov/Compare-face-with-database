from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        email = self.normalize_email(email=email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **other_fields)


class MyUser(AbstractBaseUser):
    email = models.CharField(max_length=100, unique=True)
    old_image = models.ImageField(blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



