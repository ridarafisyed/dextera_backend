from rest_framework import generics, permissions, viewsets
from rest_framework import status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import CreateFirmEmployeeSerializer, CreateClientSerializer, UserSerializer, RegisterSerializer, LoginSerializer, RoleSerializer,  UserRoleSerializer , PermissionsSerializer
from .models import Role,  UserRole, Permissions
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.

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
class CreateClientAPI(generics.GenericAPIView):
  serializer_class = CreateClientSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "status": status.HTTP_200_OK})

# registering firm employee 
class CreateFirmEmployeeAPI(generics.GenericAPIView):
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
  serializer_class = UserSerializer


class RoleAPI(generics.GenericAPIView):
    serializer_class = RoleSerializer

    def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      role = serializer.validated_data
      
      return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": token,
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

# class RolePermissionsAPI(viewsets.ModelViewSet):
#     queryset = RolePermissions.objects.all()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = RolePermissionsSerializer

