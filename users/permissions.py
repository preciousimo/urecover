from rest_framework import permissions

class RolePermission(permissions.BasePermission):
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def has_permission(self, request, view):
        return request.user and request.user.role in self.allowed_roles

class IsSuperAdmin(RolePermission):
    def __init__(self):
        super().__init__(['super_admin'])

class IsCounsellor(RolePermission):
    def __init__(self):
        super().__init__(['counsellor'])

class IsClient(RolePermission):
    def __init__(self):
        super().__init__(['client'])