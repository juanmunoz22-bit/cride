"""Circles views"""

# Django
from django.http import JsonResponse

# Models
from cride.circles.models import Circle

def list_circles(request):
    #circles = Circle.objects.all().filter(is_public=True)
    #data = [circle.name for circle in circles]
    data = list(
        Circle.objects.filter(
            is_public=False
        ).values(
            'name', 
            'slug_name', 
            'rides_taken',
            'rides_offered',
            'members_limit'
        )
    )

    return JsonResponse(data, safe=False)