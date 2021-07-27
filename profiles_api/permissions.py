from rest_framework import permissions




class UpdateOwnProfile(permissions.BasePermission):
    '''Allo users to edit their own profiles!'''
    
    def has_object_permission(self, request, view, obj):
        '''Check user is trying to edit own profile'''
        if request.method in permissions.SAFE_METHODS:
            # this means the users can see each others profile but they can't modify it.
            return True
        # if the user is trying to edit its own profile we will return True otherwise False
        return obj.id == request.user.id
