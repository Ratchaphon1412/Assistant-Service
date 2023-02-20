from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # email is unique and required field for user model in django auth system
    email = models.EmailField(unique=True, verbose_name='Email Address')
    USERNAME_FIELD = 'email'  # email is used as username field in django auth system
    REQUIRED_FIELDS = ['username']
