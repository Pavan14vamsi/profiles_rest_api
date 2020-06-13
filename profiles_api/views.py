from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
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
        serializer = self.serializer_class(data=request.data) #the argument is added to the function definition by django
        #print(type(serializer)) #serializer is a class type of HelloSerializer
        if serializer.is_valid(): #inbuilt method
            name = serializer.validated_data.get('name') #inbuilt method
            message = f'Hello {name}'
            return Response({'Message': message})
        else:
            return response(serializer.errors,  #inbuilt dictionary maybe
            status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        """Handles the updating of an object"""
        return Response({"Method":"PUT"})

    def patch(self, request, pk=None):
        """Handles the partial updating of an object"""
        return Response({"Method":"PATCH"})

    def delete(self, request, pk=None):
        """Handles the deletion of an object"""
        return Response({"Method":"Delete"})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewsets"""
    serializer_class = serializers.HelloSerializer #This luckily also works here, i guess it's because only one field is used
    def list(self, request):
        """Return a hello msg"""

        a_viewset = [
        "Uses actions (list, create, retrieve , update, partial_update )",
        "Automatically maps to urls based on routers",
        "Provides certain functionality quickly"
        ]

        return Response({"Message":"list()", "a_viewset":a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data) #even though i didn't make a parameter data in the definition it exists

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """Retrieve a particular object"""
        return Response({"Message":"Get"})

    def update(self,request,pk=None ):
        """Update a particular object"""
        return Response({"Message": "PUT"})

    def partial_update(self,request, pk=None):
        """Update a particular object"""
        return Response({"Message": "PATCH"})

    def destroy(self,request, pk=None):
        """Update a particular object"""
        return Response({"Message": "DELETE"})
