
from django.core.management import BaseCommand
# from django.contrib.auth.models import Group
# from accounts.models import Role
from django.contrib.auth import get_user_model

User = get_user_model()



# FIRMS = {
#     "firm1" : ["firm1","Sherlock","Holmes","firm1@firm1.com","firm1234"],
#     "firm2" : ["firm2","Mycroft","Holmes","firm2@firm2.com","firm1234"],
# }
# FIRM_EMPLOYEE ={
#     "lawyer1" : ["lawyer1","John","Lawyer","lawyer1@firm1.com","firm1234"],
#     "lawyer2" : ["lawyer2","John","Lawyer","lawyer2@firm2.com","firm1234"],
# }
# CLIENT ={
#     "client" : ["client","Joe","Adam","admin@admin.com","admin1234"],

# }

# #  group = Group.objects.get("client")
# #         user.group = group


# #  role = Role.objects.get("Sr. Atterney")
# #         user.role = role
class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):
   
        u1 = User.objects.create_client(username="firm1", first_name="Sherlock", last_name="Holmes", email="firm1@firm1.com", password="firm11234")
       
        print("Creating {}".format(u1))
        u1.save

        u2 = User.objects.create_client(username="firm2", first_name="Mycroft", last_name="Holmes", email="firm2@firm2.com", password="firm21234" )
      
        print("Creating {}".format(u2))
        u2.save
       
        u3 = User.objects.create_firm_employee(username="lawyer1", first_name="John", last_name="Watson", email="lawyer1@firm1.com", password="lawyer11234")
       
        print("Creating {}".format(u3))
        u3.save

        u4 = User.objects.create_firm_employee(username="lawyer2", first_name="Greg", last_name="Lestrade", email="lawyer2@firm2.com", password="lawyer21234")
        
        print("Creating {}".format(u4))
        u4.save
       

        u5 = User.objects.create(username="user", first_name="James", last_name="Moriarty", email="user@firm2.com", password="user1234" )
        
        print("Creating {}".format(u5))
        u5.save