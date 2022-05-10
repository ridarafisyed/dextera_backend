
from rest_framework import serializers
from ..models.role import UserRole, UserGroup

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields =  (
            "id",
            "name",
            "contacts",
            "matter",
            "calendar",
            "flat_fee",
            "expenses",
            "trust",
            "tasks",
            "invoice",
            "payments",
            "full_dob",
            "full_ssn",
            "partial_ssn",
            "partial_dob",
            "roles",
            "reports",
            "discounts",
            "bank_accounts",
        )

class GetRoleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields=(
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


