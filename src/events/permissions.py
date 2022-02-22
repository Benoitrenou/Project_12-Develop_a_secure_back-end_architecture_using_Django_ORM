from rest_framework.permissions import BasePermission, SAFE_METHODS
from authentification.models import User


class HasEventPermissions(BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS:
            return True
        if request.user.role == User.MANAGEMENT:
            return True
        if request.user == obj.contract__company__sales_contact:
            return True
        return request.user == obj.support_contact