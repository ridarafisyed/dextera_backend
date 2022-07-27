
from django.core.management import BaseCommand

from core.models.profile import Member, Profile

class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):
   
        u1 = Profile.objects.create(f_name="Sherlock", l_name="Holmes", c_email="firm1@firm1.com", group="firm", role="Director")
        print("Creating {}".format(u1))
        u1.save

        u2 = Profile.objects.create(f_name="Mycroft", l_name="Holmes", c_email="firm2@firm2.com",  group="firm", role="Director")
        print("Creating {}".format(u2))
        u2.save
       
        u3 = Profile.objects.create(f_name="John", l_name="Watson", c_email="lawyer1@firm1.com", group="lawyer", role="Sr. Atterney")
        print("Creating {}".format(u3))
        u3.save

        u4 = Profile.objects.create(f_name="Greg", l_name="Lestrade", c_email="lawyer2@firm2.com", group="lawyer", role="Sr. Atterney")
        print("Creating {}".format(u4))
        u4.save

        u5 = Profile.objects.create(f_name="James", l_name="Moriarty", c_email="user@firm2.com", group="client", role="")
        print("Creating {}".format(u5))
        u5.save