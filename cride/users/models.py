"""User model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utils
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """User model
    
    Extends from Django's abstract user, change the username field
    to email and add some extra fields
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_number = models.CharField(
        max_length=17,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text={
            'Help easiñy distinguish users and perform queries.'
            'Clients are the main type of user'
        }
    )

    is_verified = models.BooleanField(
        'verified',
        default = False,
        help_text= {
            'Set to true when users have verified their email address'
        }
    )
    