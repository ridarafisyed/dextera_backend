from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    user = models.ForeignKey(User, related_name="role", on_delete=models.CASCADE )
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name