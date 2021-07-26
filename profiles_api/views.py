from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
# Internals

from profiles_api import serializers


class HelloApiView(APIView):
    ''' Test API View. '''
    serializer_class = serializers.HelloSerializer

    def get(self, request,format=None, *args, **kwargs):
        ''' Returns a list of APIVew features. '''
        # Format is used to add a full mass sufix to the api 
        an_apiview = [
            'Uses Https methids as funcs (get, post, path,put,delete)',
            'Is similar to a traditional django View',
            'gives you the most control over your app logic',
            'Is mapped manually to Urls.', 
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    
    def post(self, request,format=None, *args, **kwargs):
        '''Create a hello messagee with our name.!'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !!!!!!!!!!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST, )
        

    def put(self, request,pk=None, *args, **kwargs):
        '''Handles Updating the object.'''
        kiss_my_ass = 'OK!'
        return Response({'method':'PUT'})


    def patch(self, request,pk=None, *args, **kwargs):
        '''Handel a partial update of an object'''
        return Response({'method':'PATCH'})


    def delete(self, request,pk=None):
        '''Deletes an object'''
        return Response({'method':'DELETE'})








'''The main difference between the PUT and PATCH method
 is that the PUT method uses the request URI to supply a modified version of the requested resource
  which replaces the original version of the resource, 
whereas the PATCH method supplies a set of instructions to modify the resource.
Put Entirely 
Patch partially

'''
    