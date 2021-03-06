from rest_framework.permissions import BasePermission, SAFE_METHODS
from authentification.models import User


class HasContractPermissions(BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS:
            return True
        if request.user.role == User.MANAGEMENT:
            return True
        return request.user == obj.company__sales_contact
