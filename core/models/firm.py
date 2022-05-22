from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Firm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)

class FirmEmployee(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)


class FirmClient(models.Model):
    Client = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)