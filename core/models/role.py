from django.db import models



class UserGroup(models.Model):
    name = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.name

class UserRole(models.Model):
    name = models.CharField(max_length=250, unique=True)
    contacts = models.CharField(max_length=12, default="00_ffffffff")
    matter= models.CharField(max_length=12, default="01_ffffffff")
    calendar= models.CharField(max_length=12, default="02_ffffffff")
    flat_fee= models.CharField(max_length=10, default="03_ffffffff")
    expenses= models.CharField(max_length=12, default="04_ffffffff")
    trust= models.CharField(max_length=12, default="05_ffffffff")
    tasks= models.CharField(max_length=12, default="06_ffffffff")
    invoice= models.CharField(max_length=12, default="07_ffffffff")
    payments= models.CharField(max_length=12, default="08_ffffffff")
    full_dob= models.CharField(max_length=12, default="09_ffffffff")
    full_ssn= models.CharField(max_length=12, default="10_ffffffff")
    partial_ssn= models.CharField(max_length=12, default="11_ffffffff")
    partial_dob= models.CharField(max_length=12, default="12_ffffffff")
    roles= models.CharField(max_length=12, default="13_ffffffff")
    reports= models.CharField(max_length=12, default="14_ffffffff")
    discounts= models.CharField(max_length=12, default="15_ffffffff")
    bank_accounts= models.CharField(max_length=12, default="16_ffffffff")
    
    def __str__(self):
        return self.name




