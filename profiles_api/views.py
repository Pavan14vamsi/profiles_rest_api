from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
# Create your views here.

class HelloApiView(APIView):
    """Testing Api View """
    serializer_class =serializers.HelloSerializer # it's a class but you don't add brackets WTF!?
    def get(self, request, format = None):
        """Returns a list of API views"""
        an_apiview = [
        "Uses HTTP methods as functions (GET, POST, PATCH, PUT, DELETE)",
        "Is similar to a traditional django view but specifically intended to use as API",
        "Gives most control over logic",
        "Is manually mapped to URLs"
        ]

        return Response({"Message":"hello", "the api": an_apiview, "yourimage":"https://www.pixel4k.com/wp-content/uploads/2018/10/small-memory-4k_1540749683.jpg"})


    def post(self, request):# format = None):
        """Checks the post function"""
        serializer = self.serializer_class(data=request.data)\

        if serializer.is_valid(): #inbuilt method
            name = serializer.validated_data.get('name') #inbuilt method
            message = f'Hello {name}'
            return Response({'Message': message})
        else:
            return response(serializer.errors,  #inbuilt dictionary maybe
            status = status.HTTP_404_NOT_FOUND)
