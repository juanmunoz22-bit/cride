"""User's app"""

# Django
from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    """Users app Config"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cride.users'
    verbose_name = 'Users'
