from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import UserSerializer
from users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom token obtain pair serializer to add user_id claim to the token.
    """

    @classmethod
    def get_token(cls, user):
        """
        Generate a token with user_id claim.
        
        Args:
            user (User): The user object.

        Returns:
            Token: The generated token with user_id claim.
        """
        token = super().get_token(user)
        token['user_id'] = user.id  # Add the user_id claim
        return token

    def validate(self, attrs):
        """
        Validate the input data and add the user object to the response.
        
        Args:
            attrs (dict): The input data.

        Returns:
            dict: The validated data with the user object.
        """
        data = super().validate(attrs)
        user = self.user  # Get the user object
        data['user'] = UserSerializer(user).data
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    """
    Custom token refresh serializer to add user object to the response.
    """

    def validate(self, attrs):
        """
        Validate the input data and add the user object to the response.
        
        Args:
            attrs (dict): The input data.

        Returns:
            dict: The validated data with the user object.
        """
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])
        user = User.objects.get(id=refresh['user_id'])  # Retrieve user using the user_id claim
        data['user'] = UserSerializer(user).data
        return data