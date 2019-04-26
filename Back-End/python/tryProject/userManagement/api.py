from userManagement.models import Lead
from rest_framework import viewsets, permissions
from .serializers import UserManagementSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = UserManagementSerializer

    