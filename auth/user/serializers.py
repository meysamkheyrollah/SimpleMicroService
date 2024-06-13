from rest_framework import serializers
from user.models import User
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'national_id', 'email', 'username', 'password']

