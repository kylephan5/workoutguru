from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, time, left, right, current, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not time:
            raise ValueError('User must have time')

        user = self.model(email=self.normalize_email(
            email), time=time, left=left, right=right, current=current)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, time, left, right, current, password):
        user = self.create_user(email=self.normalize_email(email), time=time, left=left, right=right, current=current,
                                password=password)
        user.time = time
        user.left = left
        user.right = right
        user.current = current
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",
                              max_length=60, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date-joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    time = models.IntegerField()
    left = models.IntegerField()
    right = models.IntegerField()
    current = models.IntegerField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['time', 'left', 'right', 'current']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
