from rest_framework.permissions import BasePermission

class IsBiologistOrOwner(BasePermission):
    """
    Custom permission to only allow biologists to view all requests or
    citizens to view their own requests.
    """
    
    def has_permission(self, request, view):
        # Allow biologists to list all requests
        if request.user and request.user.is_authenticated and request.user.groups.filter(name='Biologists').exists():
            return True
        # Allow citizens to view their own requests
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Allow biologists to view all requests
        if request.user and request.user.is_authenticated and request.user.groups.filter(name='Biologists').exists():
            return True
        # Allow citizens to view their own requests
        return obj.user == request.user