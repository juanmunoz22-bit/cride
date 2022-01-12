"""Users urls"""

# Django
from django.urls import path

# Views
from cride.users.views import UserLoginApiView, UserSignUpApiView

urlpatterns = [
    path(
        route='users/login', 
        view=UserLoginApiView.as_view(),
        name='login'
    ),
    path(
        route='users/signup', 
        view=UserSignUpApiView.as_view(),
        name='signup'
    ),
    
]