from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets , filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Internals
from .permissions import UpdateOwnProfile, UpdateOwnStatus
from profiles_api import serializers
from .models import UserProfile, ProfileFeedItem






'''The main difference between the PUT and PATCH method
 is that the PUT method uses the request URI to supply a modified version of the requested resource
  which replaces the original version of the resource, 
whereas the PATCH method supplies a set of instructions to modify the resource.
Put Entirely 
Patch partially
'''

######################### USER PROFILE API ##############################

class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles.'''
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    
class UserLoginApiView(ObtainAuthToken):
    '''Handle creating user authentication tokens!'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating and reading profile feed update'''
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (UpdateOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        '''Sets the user profile to the logged in user.'''
        serializer.save(user_profile=self.request.user)
























