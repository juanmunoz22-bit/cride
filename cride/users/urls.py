"""Users urls"""

# Django
from django.urls import path

# Views
from cride.users.views import (
    UserLoginApiView, 
    UserSignUpApiView,
    AccountVerificationAPIView
)

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
    path(
        route='users/verify', 
        view=AccountVerificationAPIView.as_view(),
        name='verify'
    ),
    
]