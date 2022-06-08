from rest_framework import serializers
from accounts.models import  FunctionPermissions, Role,  UserRole, Permissions
from core.serializers.profile import CreateMemberSerializer
from django.contrib.auth.models import Group 
from django.contrib.auth import get_user_model

User = get_user_model()

# PERMISSIONS = ['Contact', 'Matter', 'Calender', 'Flat Fee', 'Expenses','Trust','Task(s)',
#     'Invoice', 'Payments','Full DOB','Full SSN', 'Partial DOB', 'Partial SSN',
#     'Roles', 'Reports', 'Discounts', 'Bank Acounts']




class FunctionPermissionsSerializer(serializers.ModelSerializer):   
    class Meta:
        model= FunctionPermissions
        fields=(
            'id',
            'role',
            'func',
            'name',
            'is_set',
            
        )
class RoleFunctionsSerializer(serializers.ModelSerializer):
    function_permission = FunctionPermissionsSerializer(many=True)
    class Meta:
        model= FunctionPermissions
        fields=(
            'id',
            'role',
            'func',
            'name',
            'function_permission',
        )
class RoleSerializer(serializers.ModelSerializer):
    role_functions = RoleFunctionsSerializer(many=True)
    class Meta:
        model = Role
        fields=(
            "id",
            "name",
            "role_functions"
        )
        

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields=(
            "id",
            "name",
        )
        
