# api/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Safe methods (GET, HEAD, OPTIONS) allowed to anyone.
    Unsafe methods (POST, PUT, PATCH, DELETE) allowed only to admin users.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to allow only owners of an object (assuming object has `.owner`)
    or admin users to edit it. Read-only access is allowed to authenticated users.
    """

    def has_permission(self, request, view):
        # require authentication for non-safe methods
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS already allowed in has_permission but double-check
        if request.method in permissions.SAFE_METHODS:
            return True

        # allow admin
        if request.user and request.user.is_staff:
            return True

        # object-level ownership check (adjust attribute name if needed)
        owner = getattr(obj, 'owner', None)
        if owner is None:
            # fallback: if there's no owner field, deny write access to non-admins
            return False
        return owner == request.user
