from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True, default='update')
    last_name = models.CharField(max_length=30, blank=True, null=True, default='update')
    avatar = models.ImageField(upload_to='avatars', default='images/logo.png')
    date_joined = models.DateTimeField(auto_now_add=True)
    regimen = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_profile_absolute_url(self):
        return reverse('accounts:profile', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.user.username))
        super(Profile, self).save(*args, **kwargs)
