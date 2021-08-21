from rest_framework import permissions

class IsPostWriter(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.writer == request.user
        return False