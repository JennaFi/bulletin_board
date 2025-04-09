from django.db import models

from config.settings import AUTH_USER_MODEL
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Product Name')
    description = models.TextField(blank=True, null=True, verbose_name='Product Description')
    price = models.PositiveIntegerField(verbose_name='Product Price')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='Owner')
    slug = models.SlugField(max_length=250, unique_for_date='created_at')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='reviews',
                                verbose_name='Product')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Author',
                              related_name='reviews')
    text = models.TextField(verbose_name='Review Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return f'{self.owner}: {self.text[:50]}...'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']
