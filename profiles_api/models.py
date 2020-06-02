from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """ Create user manager for managing user profiles """
    def create_user(self, email, name, password=None):
        """ Create new user profile"""
        if not email:
            raise ValueError("The user must have an email")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, name, password):
        """ Create super user for admin priviledges """
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user
        

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    This model is used to overwrite the django built
    in user model to our own custom needs
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """ Retrieves the full name for the user """
        return self.name
    
    def get_short_name(self):
        """ Retrieves the short name for the user """
        return self.name
    
    def __str__(self):
        """ String representation of the user model """
        return self.email
