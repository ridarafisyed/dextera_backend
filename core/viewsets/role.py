from rest_framework import  viewsets, permissions
from ..serializers.role import RoleSerializer, GroupSerializer, GetRoleListSerializer

from ..models.role import UserRole, UserGroup 



class RoleViewset(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoleSerializer

class GetRoleListViewset(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GetRoleListSerializer

class GroupViewset(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer
