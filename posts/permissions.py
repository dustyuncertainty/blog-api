from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #authenticated users only can see list view

        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        #read permissions are allowed to any request so we'll always
        # allow GTE, HEAD , or OPTIONS requests

        if request.method in permissions.SAFE_METHODS:
            return True
        
        #write permissions are only allowed to the author of the post
        return obj.author == request.user