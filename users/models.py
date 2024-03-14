from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', null=True, blank=True, verbose_name='Avatar')
    phone = models.CharField(max_length=20,blank=True, null=True, verbose_name='Phone')


class Meta:
    db_table = 'users'
    verbose_name = 'User'
    verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
