from accounts.models import FunctionPermissions, Role, RoleFunctions,  UserRole, Permissions
from rest_framework import status
from accounts.serializer.role import FunctionPermissionsSerializer, RoleSerializer, RoleFunctionsSerializer
from rest_framework import generics, permissions 
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model


PERMISSIONS_ALL = ['view','edit', 'create', 'delete' ]

PERMISSIONS_CONTACT =['contacts', 'team', 'office', 'region']

FUNCTIONS = ['Contact', 'Matter', 'Calender', 'Flat Fee', 'Expenses','Trust','Task(s)',
    'Invoice', 'Payments','Full DOB','Full SSN', 'Partial DOB', 'Partial SSN',
    'Roles', 'Reports', 'Discounts', 'Bank Acounts']

class RolesCreateView(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      role = serializer.save()
      for item in FUNCTIONS:
        fun = RoleFunctions.objects.create(role = role, name = item)
        fun.save()
        for perm in PERMISSIONS_ALL:
          fun = FunctionPermissions.objects.create(role = role, function = fun, name = perm)
          fun.save()
        if item == "Contact":
          for c_perm in PERMISSIONS_CONTACT:
            c_fun = FunctionPermissions.objects.create(role = role, func = fun, name = c_perm)
            c_fun.save()
      return Response({
        "role": RoleSerializer(role, context=self.get_serializer_context()).data,
        
        "status": status.HTTP_200_OK
      })

class RolesListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class SingleRoleView(generics.RetrieveUpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class DeleteRoleView(generics.DestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RolesCreateView(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      role = serializer.save()
      for permission in PERMISSIONS:
        fun = RoleFunctions.objects.create(role = role, name = permission)
        fun.save()
        permission = F

      return Response({
        "role": RoleSerializer(role, context=self.get_serializer_context()).data,
        
        "status": status.HTTP_200_OK
      })

class RoleFunctionsCreateView(generics.CreateAPIView):
    queryset = RoleFunctions.objects.all()
    serializer_class = RoleFunctionsSerializer

class RoleFunctionsListView(generics.ListAPIView):
    queryset = RoleFunctions.objects.all()
    serializer_class = RoleFunctionsSerializer

class SingleRoleFunctionView(generics.RetrieveUpdateAPIView):
    queryset = RoleFunctions.objects.all()
    serializer_class = RoleFunctionsSerializer

class DeleteRoleFunctionView(generics.DestroyAPIView):
    queryset = RoleFunctions.objects.all()
    serializer_class = RoleFunctionsSerializer



class RoleFunctionPermissionCreateView(generics.CreateAPIView):
  queryset = FunctionPermissions.objects.all()
  serializer_class = FunctionPermissionsSerializer

class RoleFunctionPermissionsListView(generics.ListAPIView):
  queryset = FunctionPermissions.objects.all()
  serializer_class = FunctionPermissionsSerializer

class DeleteRoleFunctionPermissionView(generics.DestroyAPIView):
  queryset = FunctionPermissions.objects.all()
  serializer_class = FunctionPermissionsSerializer

class SingleRoleFunctionPermissionView(generics.RetrieveUpdateAPIView):
  queryset = FunctionPermissions.objects.all()
  serializer_class = FunctionPermissionsSerializer