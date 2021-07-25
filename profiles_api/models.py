from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    ''' Manager for user profiles.'''

    def create_user(self, email, name, password=None):
        # A none password won't work so bascially if you don't have a password you've got no user 

        if not email:
            raise ValueError('شما باید یک ایمیل داشته باشید! :/ ')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user 

    def create_superuser(self, email, name, password):
        '''Create and Save a new Superuser with given detailes man.'''
        user = self.create_user(email, name, password)
        user.is_superuser = True 
        user.is_staff = True 
        user.save(using = self._db)

        return user 






class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Database Model for users in the system.'''
    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects  = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']
    
    def get_full_name(self):
        ''' Retrieve full name of the user '''
        return self.name
        
    def get_short_name(self):
        '''Retrieve short name of the user '''
        return self.name

    def __str__(self):
        '''Return String representation of user '''
        return self.email 
