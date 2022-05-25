from django.urls import path, include
from .viewsets import  GroupAPI, RegisterAPI, IsActiveUserAPI, LoginAPI, UserAPI,CreateClientAPI, CreateFirmEmployeeAPI, RoleAPI, UserListAPI, PermissionsAPI, RolePermissionAPI, UserRoleAPI
from knox import views as knox_views

from rest_framework import routers

router = routers.DefaultRouter()

router.register('auth/roles', RoleAPI, "roles"),
router.register('auth/users-list', UserListAPI, "users_list")
router.register('auth/users-role-list', UserRoleAPI, "users_role_list")
router.register('auth/permissions', PermissionsAPI, "permissions")
router.register('auth/role-permissions', RolePermissionAPI, "role_permissions")
router.register('auth/groups', GroupAPI, "group")
router.register('auth/is-active-user', IsActiveUserAPI, "is_active_user")
router.register('auth/register-client', CreateClientAPI, "register-client" )
router.register('auth/register-firm-employee', CreateFirmEmployeeAPI, "register_firm_employe"),


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
  # path('auth/register-client', CreateClientAPI.as_view()),

  
  path('auth/login', LoginAPI.as_view()),
  path('auth/user', UserAPI.as_view()),
  
  path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]