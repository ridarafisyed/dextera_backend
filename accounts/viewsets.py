
from rest_framework import generics, permissions, viewsets
from rest_framework import status
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth.models import Group 
from .serializers import CreateUserSerializer, CreateFirmEmployeeSerializer, IsActiveUser, GroupsSerializer, UserListSerializer,CreateClientSerializer, UserSerializer, RegisterSerializer, LoginSerializer, RoleSerializer,  UserRoleSerializer , PermissionsSerializer, RolePermissionsSerializer
from .models import Role,  UserRole, Permissions
from rest_framework import generics, permissions 
from rest_framework.views import APIView

from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ListPermissionsView(generics.ListAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UpdatePermissionView(generics.RetrieveUpdateAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ListRolesView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RolePermissionsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class GetRoleView(generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RolePermissionsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UpdateRoleView(generics.RetrieveUpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RolePermissionsSerializer



PERMISSIONS = ['Contact', 'Matter', 'Calender', 'Flat Fee', 'Expenses','Trust','Task(s)',
    'Invoice', 'Payments','Full DOB','Full SSN', 'Partial DOB', 'Partial SSN',
    'Roles', 'Reports', 'Discounts', 'Bank Acounts']

# Registeration Api view for registering user 
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1],
      "status": status.HTTP_200_OK,
    })

# Register client 
class CreateClientAPI(viewsets.ModelViewSet):
  serializer_class = CreateClientSerializer

  queryset = User.objects.all()

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    obj = Member.objects.create(role = role, name = permission)
    obj.save()
    return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "status": status.HTTP_200_OK})

# registering firm employee 
class CreateFirmEmployeeAPI(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = CreateFirmEmployeeSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "status": status.HTTP_200_OK})

# login user 
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    _, token = AuthToken.objects.create(user)
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token,
      "status": status.HTTP_200_OK
    })

# for accessing user data 
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

class UserListAPI(viewsets.ModelViewSet):
  queryset = User.objects.all()
  permission_classes = [
        permissions.AllowAny
    ]
  serializer_class = UserListSerializer


class CreateUserViewset(viewsets.ModelViewSet):
  queryset = User.objects.all()
  permission_classes =[permissions.AllowAny]
  serializer_class= CreateUserSerializer


class RoleAPI(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('pk')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      role = serializer.save()
      for permission in PERMISSIONS:
        obj = Permissions.objects.create(role = role, name = permission)
        obj.save()
      return Response({
        "role": RoleSerializer(role, context=self.get_serializer_context()).data,
        
        "status": status.HTTP_200_OK
      })

class PermissionsAPI(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PermissionsSerializer


class UserRoleAPI(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserRoleSerializer

class RolePermissionAPI(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('pk')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RolePermissionsSerializer
    # lookup_field = 'role'

class GroupAPI(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupsSerializer

class IsActiveUserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IsActiveUser



