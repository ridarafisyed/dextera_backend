
from django.core.management import BaseCommand
from accounts.models import UserAccount

ADMIN ={
    "admin" : ["admin","Super","Admin","admin@admin.com","admin1234", ],
}

FIRMS = {
    "firm1" : ["firm1","Sherlock","Holmes","firm1@firm1.com","firm1234"],
    "firm2" : ["firm2","Mycroft","Holmes","firm2@firm2.com","firm1234"],
}
FIRM_EMPLOYEE ={
    "lawyer1" : ["lawyer1","John","Lawyer","lawyer1@firm1.com","firm1234"],
    "lawyer2" : ["lawyer2","John","Lawyer","lawyer2@firm2.com","firm1234"],
}
CLIENT ={
    "client" : ["client","Joe","Adam","admin@admin.com","admin1234"],
}

class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):
        for user_ in USER:

            new_role = Role.objects.create(name=role_name)
            
            for permission in PERMISSIONS:
                permission_obj = Permissions.objects.create(role = new_role, name = permission)
                name = "permission {} with role {}".format(permission, role_name)
                print("Creating {}".format(name))