from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    ''' Test API View. '''
    
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

        