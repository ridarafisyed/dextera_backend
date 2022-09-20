
from django.core.management import BaseCommand
from core.models.finance import FinanceAccount
from core.models.profile import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):
   
        u1 = User.objects.get(username="firm1")
       
        u2 = User.objects.get(username="firm2")
       
        u3 = User.objects.get(username="lawyer1")


        u4 = User.objects.get(username="lawyer2")

        u5 = User.objects.get(username="user")

        m1 = FinanceAccount.objects.create(owner=u1)
        print("Creating {}".format(u1))
        m1.save

        m2 = FinanceAccount.objects.create(owner=u2)
        print("Creating {}".format(u2))
        m2.save

        m3 = FinanceAccount.objects.create(owner=u3)
        print("Creating {}".format(u3))
        m3.save

        m4 = FinanceAccount.objects.create(owner=u4)
        print("Creating {}".format(u4))
        m4.save

        m5 = FinanceAccount.objects.create(owner=u5)
        print("Creating {}".format(u5))
        m5.save



        


