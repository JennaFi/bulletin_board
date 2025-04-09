from django.contrib import admin

from board.models import Product, Review


@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    """Administration of Product"""

    list_display = ('id', 'name', 'price', 'owner', 'created_at', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class UserAdmin(admin.ModelAdmin):
    """Administration of Review"""

    list_display = ('product', 'text', 'owner', 'created_at')
