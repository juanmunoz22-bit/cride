"""Circle model"""

# Django
from django.db import models

# Utils
from cride.utils.models import CRideModel

class Circle(CRideModel):
    """Circle model

    A circle is a private group where rides are offered and taken
    by its members. To join a circle a user must receive an unique
    invitation code from an existing circle member.
    """

    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures/', blank=True, null=True)

    members = models.ManyToManyField(
        'users.User', 
        through='circles.Membership',
        through_fields=('circle', 'user',)
    )

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles are also known as official communities'
    )

    is_public = models.BooleanField(
        'public cicle',
        default=True,
        help_text='To concrete if a circle is public and everyone can see it and to ask for join'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members'
    )
    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited. This number will be the fixed limit the users select'
    )

    def __str__(self):
        """Return name"""
        return self.name
    
    class Meta(CRideModel.Meta):
        """Meta class"""

        ordering = ['-rides_taken', '-rides_offered']
