from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'super_admin'

class IsCounsellor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'counsellor'

class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'client'
