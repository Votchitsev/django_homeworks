from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.creator:
            return True
        elif request.user.is_staff is True:
            return True
        else:
            return False
