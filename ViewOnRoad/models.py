from django.db import models
from django.utils import timezone


class SignUp(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name
