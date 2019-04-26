from rest_framework import serializers
from userManagement.models import Lead

#userManagementSerializer
class UserManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
