"""Users Serializers"""

# Django
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from cride.users.models import User, Profile

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer
    
    Handle signup data validation and profile/user creation
    """

    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format +123456789. Up to 15 digits"
    )
    phone_number = serializers.CharField(
        validators=[phone_regex]
    )
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verify passwords match"""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user/profile creation"""
        data.pop('password_confirmation')
        user=User.objects.create_user(**data)
        profile: Profile = Profile.objects.create(user=user)
        return user

class UserLoginSerializer(serializers.Serializer):
    """User login serializer
    
    Handle login request data
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verify credentials"""
        user = authenticate(
            username=data['email'], 
            password=data['password']
        )
        self.context['user'] = user
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        return data

    def create(self, data):
        """Generate or retrieve new token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key