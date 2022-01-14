"""Circle views"""

#DRF
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

# Permissions
from cride.circles.permissions import IsCircleAdmin

# Serializers
from cride.circles.serializers import CircleModelSerializer

# Models
from cride.circles.models import Circle, Membership

class CircleViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    """Create view set for circles"""

    serializer_class = CircleModelSerializer

    def get_queryset(self):
        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset

    def get_permissions(self):
        """Assign permissions based in actions"""
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial-update']:
            permissions.append(IsCircleAdmin)
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        """Assign circle admin"""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10
        )
