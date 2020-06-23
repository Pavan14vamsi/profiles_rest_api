from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """This class is serializers a name field for testing our API view to test the post function"""
    name = serializers.CharField(max_length=10)

class UserSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile #this sets our serializer up to point to the correct model
        fields = ('id', 'email', 'name','password')
        """specify a list of fields in the model that we wanna manage thru the serializer
           all these fields are made accessible in the model, but we wanna make password read only
           as we want them to use it only when creating it"""
        extra_kwargs = {
            'password':{
                'write_only':True,  #This means you can use this only to create passwords, won't be available when using the GET requests
                'style':{
                    'input_type':'password'
                }
            }
        }
    #overriding create function so that password is sent as a hash




    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
            )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes the profile feed"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only':True}}
