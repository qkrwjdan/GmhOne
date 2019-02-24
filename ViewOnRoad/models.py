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
    file = models.FileField(upload_to='uploads')
    created_date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.title


class storyonroad_uploadFile_model(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default = timezone.now)
    file = models.FileField(upload_to='uploads/',default='settings.MEDIA_ROOT/uploads/GMH_logo.png')
    text = models.TextField()
    
    def __str__(self):
        return self.title


class longWay_uploadFile_model(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default = timezone.now)
    text = models.TextField()
    file = models.FileField(upload_to='uploads/',default='settings.MEDIA_ROOT/uploads/GMH_logo.png')
    MENU_1 = "ASIA"
    MENU_2 = "CHINA"
    MENU_3 = "TAI"
    MENU_4 = "MIDDEL_EAST"
    MENU_5 = "EUROPE"
    MENU_6 = "AFRICA"
    MENU_7 = "AMERICA"
    MENU_CHOICES = (
        (MENU_1,"아시아"),
        (MENU_2,"중국"),
        (MENU_3,"태국"),
        (MENU_4,"중동"),
        (MENU_5,"유럽"),
        (MENU_6,"아프리카"),
        (MENU_7,"아메리카")
    )
    detail_menu = models.CharField(
        max_length = 10,
        choices = MENU_CHOICES,
        default = MENU_1,
    )
    
    def __str__(self):
        return self.title


class roadview_uploadFile_model(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default = timezone.now)
    file = models.FileField(upload_to='uploads/',default='settings.MEDIA_ROOT/uploads/GMH_logo.png')
    text = models.TextField()

    
    def __str__(self):
        return self.title


