
from django.core.management import BaseCommand
from accounts.models import UserAccount


FIRMS = {
    "admin" : ["admin","Super","Admin","admin@admin.com","admin1234"],
    "client" : ["client","Joe","Adam","admin@admin.com","admin1234"],
    "firm" : ["firm","Sherlock","Holmes","admin@admin.com","admin1234"],
    "lawyer" : ["lawyer","Super","Admin","admin@admin.com","admin1234"],
}
FIRM_EMPLOYEE ={

}
CLIENT ={
    
}

class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):
        for role_name in ROLES:

            new_role = Role.objects.create(name=role_name)
            
            for permission in PERMISSIONS:
                permission_obj = Permissions.objects.create(role = new_role, name = permission)
                name = "permission {} with role {}".format(permission, role_name)
                print("Creating {}".format(name))