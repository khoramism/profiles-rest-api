from rest_framework import serializers
from .models import UserProfile 


class HelloSerializer(serializers.Serializer):
    ''' Serializes a name field for testing our apiview.'''
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializes a user profile object''' 
    class Meta:
        model = UserProfile
        fields = ('id','email', 'name', 'password')
        # we need to make password write only in order for nobody to see  
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {'input_type':'password'},
            }
        }
    def create(self,validated_data):
        '''Create and return a new user profile'''
        user = UserProfile.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )
        # it will override the creation of user in order to hash the password.
        return user
