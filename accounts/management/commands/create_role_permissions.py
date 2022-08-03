
from django.core.management import BaseCommand
# from accounts.models import Role, Permissions

from accounts.models import  FunctionPermissions, Role,  UserRole, Permissions, RoleFunctions

ROLES =['Principal', 
        'Partner',
        'Director',
        'Accounting',
        'Manager',
        'Sr. Attorney', 
        'Jr. Attorney', 
        'Paralegal', 
        'Assistant', 
        'Administrator', 
        'IT']


PERMISSIONS_ALL = ['view','edit', 'create', 'delete' ]

PERMISSIONS_CONTACT =['contacts', 'team', 'office', 'region']

FUNCTIONS = ['Contact', 
            'Matter', 
            'Calender', 
            'Flat Fee', 
            'Expenses',
            'Trust',
            'Task(s)',
            'Invoice', 
            'Payments',
            'Full DOB',
            'Full SSN', 
            'Partial DOB', 
            'Partial SSN',
            'Roles', 
            'Reports', 
            'Discounts', 
            'Bank Acounts']



class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):

         for role_name in ROLES:
            new_role = Role.objects.create(name=role_name)
            
            for item in FUNCTIONS:            
                func= RoleFunctions.objects.create(name = item, role=new_role)
                func.save()
                for perm in PERMISSIONS_ALL:
                    permission= FunctionPermissions.objects.create(role = new_role, func = func, name = perm)
                    permission.save()
                    name = "permission -- {} function -- {} with role -- {}".format(perm, func, role_name)
                    print("Creating {}".format(name))
                if item == "Contact":
                    for c_perm in PERMISSIONS_CONTACT:
                        c_permission, create = FunctionPermissions.objects.get_or_create(role = new_role, func = func, name = c_perm)
                        name = "permission -- {} function -- {} with role -- {}".format(perm, func, role_name)
                        print("Creating {}".format(name))
                            
                
        