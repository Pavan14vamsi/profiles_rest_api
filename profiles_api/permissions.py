from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is only changing their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id