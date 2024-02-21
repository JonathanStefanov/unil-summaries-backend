from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    """
    Custom permission to only allow superusers to create a course or faculty.
    """

    def has_permission(self, request, view):
        # Write logic is to allow POST (create) requests only if the user is a superuser
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser

class IsAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to upload a summary.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
