from django.db import models



class UserGroup(models.Model):
    name = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.name

class UserRole(models.Model):
    name = models.CharField(max_length=250, unique=True)
    contacts = models.CharField(max_length=10, default="ffffffff")
    matter= models.CharField(max_length=10, default="ffffffff")
    calendar= models.CharField(max_length=10, default="ffffffff")
    flat_fee= models.CharField(max_length=10, default="ffffffff")
    expenses= models.CharField(max_length=10, default="ffffffff")
    trust= models.CharField(max_length=10, default="ffffffff")
    tasks= models.CharField(max_length=10, default="ffffffff")
    invoice= models.CharField(max_length=10, default="ffffffff")
    payments= models.CharField(max_length=10, default="ffffffff")
    full_dob= models.CharField(max_length=10, default="ffffffff")
    full_ssn= models.CharField(max_length=10, default="ffffffff")
    partial_ssn= models.CharField(max_length=10, default="ffffffff")
    partial_dob= models.CharField(max_length=10, default="ffffffff")
    roles= models.CharField(max_length=10, default="ffffffff")
    reports= models.CharField(max_length=10, default="ffffffff")
    discounts= models.CharField(max_length=10, default="ffffffff")
    bank_accounts= models.CharField(max_length=10, default="ffffffff")
    
    def __str__(self):
        return self.name




