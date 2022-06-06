from rest_framework import serializers
from django.contrib.auth import authenticate
from core.serializers.profile import CreateMemberSerializer

from core.models.profile import Member
from .models import  Role,  UserRole, Permissions

from django.contrib.auth.models import Group 

from django.contrib.auth import get_user_model

User = get_user_model()

PERMISSIONS = ['Contact', 'Matter', 'Calender', 'Flat Fee', 'Expenses','Trust','Task(s)',
    'Invoice', 'Payments','Full DOB','Full SSN', 'Partial DOB', 'Partial SSN',
    'Roles', 'Reports', 'Discounts', 'Bank Acounts']

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'is_client', 'is_firm_employee', 'last_login', 'is_active')

class CreateUserSerializer(serializers.ModelSerializer):
  member = CreateMemberSerializer(many=False)
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name','last_name', 'email', 'password', "member")
  def create(self, validated_data):
        member_data = validated_data.pop('member')
        user = User.objects.create(**validated_data)
        Member.objects.create(user=user, **member_data)
        return user


class UserListSerializer(serializers.ModelSerializer):
  # member = serializers.RelatedField(read_only=True)
  class Meta:
    model = User
    fields = ('id', 'first_name','last_name',  'email', 'is_client', 'is_firm_employee', 'last_login', 'is_active')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id',  'username', 'first_name', 'last_name',  'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], validated_data['first_name'],validated_data['last_name'], validated_data['email'], validated_data['password'])
    # group = "firm",
    # role="Jr. Atterney"
    member  = Member.objects.create(user = user, first_name= validated_data['first_name'],last_name =validated_data['last_name'], email=validated_data['email'])
    member.save()
    return user

class CreateFirmEmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id',  'username', 'first_name', 'last_name',  'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_firm_employee(validated_data['username'], validated_data['first_name'],validated_data['last_name'], validated_data['email'], validated_data['password'])
    group = "firm",
    role="Jr. Atterney"
    member  = Member.objects.create(user = user, first_name= validated_data['first_name'],last_name =validated_data['last_name'], email=validated_data['email'], role=role, group=group)
    member.save()

    return user

class CreateClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id',  'username', 'first_name', 'last_name',  'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_client(validated_data['username'], validated_data['first_name'],validated_data['last_name'], validated_data['email'], validated_data['password'])
    group = "client",
    role=""
    member  = Member.objects.create(user = user, first_name= validated_data['first_name'],last_name =validated_data['last_name'], email=validated_data['email'], role=role, group=group)
    member.save()
    return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")
    
  
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields=(
            "id",
            "name"
        )
        
class PermissionsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Permissions
      fields = ('id', 'name', 'role', "is_view","is_edit","is_create","is_delete","is_contacts","is_team","is_office","is_region")

class UserRoleSerializer(serializers.ModelSerializer):
   class Meta:
      model = UserRole
      fields = ('user', 'role')

class RolePermissionsSerializer(serializers.ModelSerializer):
  permissions = PermissionsSerializer(many=True)
  class Meta:
      model = Role
      fields = ['id', 'name', 'permissions']

class RolePermissionsSerializer(serializers.ModelSerializer):
  permissions = PermissionsSerializer(many=True)
  class Meta:
      model = Role
      fields = ['id', 'name', 'permissions']

class GroupsSerializer(serializers.ModelSerializer):
  class Meta:
      model = Group
      fields = ['id', 'name']

class IsActiveUser(serializers.ModelSerializer):
  class Meta:
    model= User
    fields = ['id', 'is_active']

