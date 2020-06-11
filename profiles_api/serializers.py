from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """This class is serializers a name field for testing our API view to test the post function"""
    name = serializers.CharField(max_length=10)
    
