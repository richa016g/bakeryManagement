import rest_framework
from rest_framework import permissions

class AdminAuthenticationPermission(permissions.BasePermission):
    ADMIN_ONLY_AUTH_CLASSES = [rest_framework.authentication.BasicAuthentication, rest_framework.authentication.SessionAuthentication]

    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated:
            return user.is_superuser or \
                not any(isinstance(request._authenticator, x) for x in self.ADMIN_ONLY_AUTH_CLASSES) 
        return False