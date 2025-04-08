from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """User model"""

    CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.EmailField(unique=True, verbose_name='Email Address')
    phone = models.CharField(max_length=30, verbose_name='Phone Number', blank=True, null=True)
    role = models.CharField(max_length=10, choices=CHOICES, default='user', verbose_name='Role')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'




