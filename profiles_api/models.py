from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, pwd = None):
        """Creates a new user profile"""
        if not email:
            raise ValueError("Users must have email")

        email = self.normalize_email(email)
        user = self.model(email = email, name = name) #self.model is UserProfileManager
        user.set_password(pwd) #inbuit function in BaseUserManager class, same as self.model i guess
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, pwd):
        """creates a new superuser with the given details"""
        user = self.create_user(email, name, pwd)
        user.is_superuser = True
        user.is_staff = True  #These is_* vars are within the PermissionsMixin class
        return user

    pass #Class over


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the systems """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELD = ['name']   #I think these are django inbuilt names for these arrays
    def get_full_name(self):
        """Returns the name"""
        return self.name

    def get_short_name(self):
        """"Returns the short name"""
        return self.name

    def __str__(self):
        """Return string representation"""
        return self.email
