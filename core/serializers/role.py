from rest_framework import serializers
from ..models.role import UserRole, UserGroup

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields =  (
            "id",
            "name"
        )
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields =  (
            "id",
            "name"
        )
