from django.db import models
from django.utils import timezone


class SignUp(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name

class UploadFile(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/%y/%m/%d')
    created_date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.title