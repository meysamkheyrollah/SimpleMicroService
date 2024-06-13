from rest_framework.views import APIView
from user.serializers import CreateUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime 

class UserTokenLogin(TokenObtainPairView):
    """
    API view for obtaining a new JWT token pair (access and refresh).
    """
    pass

class UserTokenRefresh(TokenRefreshView):
    """
    API view for refreshing an existing JWT token.
    """
    pass

class UserSignUp(APIView):
    """
    API view for user registration.

    Allows any user to create a new account.
    """
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        """
        Create a new user account.

        Accepts user registration data and creates a new user.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


