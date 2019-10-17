from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            print("Request in safe method")
            return True
        print("Even though request is not in safe method ...")
        print(f"id is : {request.user.id}")
        return obj.id == request.user.id
