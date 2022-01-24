"""Rides Serializer"""

# DRF
from rest_framework import serializers

# Models
from cride.rides.models import Ride
from cride.circles.models import Membership, Circle
from cride.users.models import User

# Utils
from datetime import timedelta
from django.utils import timezone


class CreateRideSerializer(serializers.ModelSerializer):
    """Create ride serializer"""

    offered_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    available_seats = serializers.IntegerField(min_value=1, max_value=15)
    
    class Meta:
        model = Ride
        exclude = ('offered_in', 'passengers', 'rating', 'is_active')

    def validate_daparture_date(self, data):
        """Verify date is not in the past nor in this exact moment"""
        min_date = timezone.now() + timedelta(minutes=10)
        if data < min_date:
            raise serializers.ValidationError(
                'Departure time must be at least pass the next 20 minutes window'
            )
        return data

    def validate(self, data):
        """Validate
        
        Verify that person who offers the ride is a member
        and also the same user making the request
        """
        if self.context['request'].user != data['offered_by']:
            raise serializers.ValidationError('Rides offered on behalf of other are not allowed')
        
        user = data['offered_by']
        circle = self.context['circle']
        breakpoint()
        try:
            membership = Membership.objects.get(
                user=user,
                circle=circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            raise serializers.ValidationError('User is not an active member of the circle')
        
        if data['arrival_date'] <= data['departure_date']:
            raise serializers.ValidationError('Departure must be before arrival date')

        self.context['membership'] = membership
        return data

    def create(self, data):
        """Create ride and update stats"""
        
        circle: Circle = self.context['circle']
        ride = Ride.objects.create(**data, offered_in=circle)

        # Circle
        circle.rides_offered += 1
        circle.save()

        # Membership
        membership: Membership = self.context['membership']
        membership.rides_offered += 1
        membership.save()

        # Profile
        profile = data['offered_by'].profile
        profile.rides_offered += 1
        profile.save()

        return ride