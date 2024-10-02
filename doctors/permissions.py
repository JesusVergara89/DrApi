from rest_framework import permissions

class IsDoctor(permissions.BasePermission):
    def has_permissions(self, request, view):
        return request.user.groups.filter(name="doctors").exists()