from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
import random 
import string
from provider.tasks import EmailInterface, MobileInterface, TelegramInterface
from rest_framework import status
from rest_framework.response import Response
from provider.grpc_client import run
class UserTokenValidation(BasePermission):
    """
    Custom permission class to authenticate user token via a GRPC service.
    
    The token is extracted from the `Authorization` header and validated using 
    an external authentication service.
    """
    def has_permission(self, request, view):
        token = request.META.get('HTTP_AUTHORIZATION')
        resp = run(payload=token.split()[1])
        has_perm = True if resp else False
        return has_perm
    

class OTP: 
    @classmethod
    def generate_code(cls):
        return ''.join(random.choices(string.digits, k=5))



class MobileOTP(APIView):
    """
    API view to send OTP via Mobile.
    
    Requires a valid user token for authentication.
    """
    permission_classes = [UserTokenValidation]
    def post(self, request):
        """
        Generate and send an OTP to the user's mobile number.

        Response:
            200 OK: OTP has been sent to user.
        """
        code = OTP.generate_code()
        MobileInterface.execute(code=code)
        return Response(data={'message': 'OTP has been sent to user'}, status=status.HTTP_200_OK)

class TelegramOTP(APIView):
    """
    API view to send OTP via Telegram.
    
    Requires a valid user token for authentication.
    """
    permission_classes = [UserTokenValidation]
    def post(self, request):
        """
        Generate and send an OTP to the user's Telegram account.

        Response:
            200 OK: Telegram code has been sent to user.
        """
        code = OTP.generate_code()
        TelegramInterface.execute(code=code)
        return Response(data={'message': 'Telegram code has been sent to user'}, status=status.HTTP_200_OK)

class EmailOTP(APIView):
    """
    API view to send OTP via Email.
    
    Requires a valid user token for authentication.
    """
    permission_classes = [UserTokenValidation]
    def post(self, request):
        """
        Generate and send an OTP to the user's email address.

        Response:
            200 OK: Email has been sent to user.
        """
        code = OTP.generate_code()
        EmailInterface.execute(code=code)
        return Response(data={'message': 'Email has been sent to user'}, status=status.HTTP_200_OK)

