from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'date_of_birth', 'primary_contact_number', 'secondary_contact_number', 'currency']
        read_only_fields = ['id', 'currency ']