from django.urls import path, include
from .viewsets import  RegisterAPI, LoginAPI, UserAPI,CreateClientAPI, CreateFirmEmployeeAPI, RoleAPI, UserListAPI, PermissionsAPI, RolePermissionAPI
from knox import views as knox_views

from rest_framework import routers

router = routers.DefaultRouter()

router.register('auth/roles', RoleAPI, "roles"),
router.register('auth/users-list', UserListAPI, "users_list")
router.register('auth/permissions', PermissionsAPI, "permissions")
router.register('auth/role-permissions', RolePermissionAPI, "role_permissions")
# router.register('auth/role-permissions/<int:pk>/', UserRolePermission, "role_permissions")

urlpatterns = router.urls + [
  # path('auth', include('knox.urls')),
  # path('auth/register', RegisterAPI.as_view()),
  # path('auth/register-client', CreateClientAPI.as_view()),
  # path('auth/register-firm-employee', CreateFirmEmployeeAPI.as_view()),
  # path('auth/login', LoginAPI.as_view()),
  # path('auth/user', UserAPI.as_view()),
  # path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
  path('auth', include('knox.urls')),
 
  path('auth/register', RegisterAPI.as_view()),
  path('auth/register-client', CreateClientAPI.as_view()),
  path('auth/register-firm-employee', CreateFirmEmployeeAPI.as_view()),
  path('auth/login', LoginAPI.as_view()),
  path('auth/user', UserAPI.as_view()),
  
  path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]