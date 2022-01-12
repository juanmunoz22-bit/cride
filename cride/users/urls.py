"""Users urls"""

# Django
from django.urls import path

# Views
from cride.users.views import UserLoginApiView

urlpatterns = [
    path(
        route='users/login', 
        view=UserLoginApiView.as_view(),
        name='login'
    ),
    
]