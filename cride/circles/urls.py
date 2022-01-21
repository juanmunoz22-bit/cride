"""Circles urls"""

# Django
from django.urls import path
from django.urls.conf import include

# DRF
from rest_framework.routers import DefaultRouter

# Views
from .views import circles as circles_views
from.views import memberships as memberships_views

router = DefaultRouter()
router.register(r'circles', circles_views.CircleViewSet, basename='circle')
router.register(
    r'circles/(?P<slug_name>[-a-zA-z0-0_]+)/members',
    memberships_views.MembershipViewSet,
    basename='membership'
)

urlpatterns = [
    path('', include(router.urls))
]
