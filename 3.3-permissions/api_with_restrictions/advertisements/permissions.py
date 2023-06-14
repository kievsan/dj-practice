from rest_framework.permissions import BasePermission


class IsOwnerOrReader(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.creator
