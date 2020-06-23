from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password = None): #so i initially wrote pwd instead of password, turns out pwd = None implies the definition of the function has a parameter called pwd, that's what was breaking it before
        """Creates a new user profile"""
        if not email:
            raise ValueError("Users must have email")

        email = self.normalize_email(email)
        user = self.model(email = email, name = name) #self.model is UserProfileManager

        user.set_password(password) #inbuit function in BaseUserManager class, same as self.model i guess
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """creates a new superuser with the given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True  #These is_* vars are within the PermissionsMixin class
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the systems """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']   #I think these are django inbuilt names for these arrays
    def get_full_name(self):
        """Returns the name"""
        return self.name

    def get_short_name(self):
        """"Returns the short name"""
        return self.name

    def __str__(self):
        """Return string representation"""
        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a status text"""
        return self.status_text
