from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission: only owners can edit/delete.
    Read is allowed to everyone if they have permission.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for owner
        return getattr(obj, 'owner', None) == request.user