from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Administration of User"""

    list_display = ('id', 'username', 'email')
