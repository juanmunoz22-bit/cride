"""Circle's app"""

# Django
from django.apps import AppConfig


class CirclesAppConfig(AppConfig):
    """Circles app Config"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cride.circles'
    verbose_name = 'Circles'