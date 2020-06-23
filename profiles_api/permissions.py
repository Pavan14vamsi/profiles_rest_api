from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit only their own profile"""

    def has_object_permission(self, request, view, obj):#the function is inbuilt
        """Check if the user is only changing their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id #So we'll give a user id

class UpdateOwnStatus(permissions.BasePermission):
    """Ensures only their own statuses are changeable"""
    def has_object_permission(self, request, view, obj):
        """Checks if it's their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
