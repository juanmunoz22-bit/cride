"""Circles urls"""

# Django
from django.urls import path

# Views
from cride.circles.views import list_circles, create_circle

urlpatterns = [
    path(
        route='circles/', 
        view=list_circles
    ),
    path(
        route='circles/create/',
        view=create_circle
    )
    
]
