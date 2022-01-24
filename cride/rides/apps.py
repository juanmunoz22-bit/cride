
"""Rides app."""

from django.apps import AppConfig


class RidesAppConfig(AppConfig):
    """Rides app config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cride.rides'
    verbose_name = 'Rides'
