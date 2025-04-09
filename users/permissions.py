from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """Admin Permissions."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admins').exists()


class IsAuthor(BasePermission):
    """Author Permissions."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
