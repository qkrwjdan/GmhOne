from django.db import models
from django.utils import timezone

class storyonroad_uploadFile_model(models.Model):
    # author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default = timezone.now)
    file = models.FileField(upload_to='uploads/',default='settings.MEDIA_ROOT/uploads/GMH_logo.png')
    text = models.TextField()
    MENU_1 = "MYROAD"
    MENU_2 = "RESTAURANT"
    MENU_3 = "HISTORY"
    MENU_4 = "FESTIVAL"
    MENU_5 = "HARDROAD"
    MENU_6 = "ADVENTURE"
    MENU_7 = "REST"
    MENU_CHOICES = (
        (MENU_1,"나의길이야기"),
        (MENU_2,"맛집으로 가는길"),
        (MENU_3,"역사 속으로 가는길"),
        (MENU_4,"축제가는 길"),
        (MENU_5,"고행의 길"),
        (MENU_6,"탐험의 길"),
        (MENU_7,"휴식의 길")
    )
    detail_menu = models.CharField(
        max_length = 10,
        choices = MENU_CHOICES,
        default = MENU_1,
    )
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


class longway_uploadFile_model(models.Model):
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
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


class roadview_uploadFile_model(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default = timezone.now)
    file = models.FileField(upload_to='uploads/',default='settings.MEDIA_ROOT/uploads/GMH_logo.png')
    text = models.TextField()
    MENU_1 = "서울"
    MENU_2 = "경기도"
    MENU_3 = "충청도"
    MENU_4 = "전라도"
    MENU_5 = "강원도"
    MENU_6 = "경상도"
    MENU_7 = "제주도"

    MENU_CHOICES = (
        (MENU_1,MENU_1),
        (MENU_2,MENU_2),
        (MENU_3,MENU_3),
        (MENU_4,MENU_4),
        (MENU_5,MENU_5),
        (MENU_6,MENU_6),
        (MENU_7,MENU_7),
    )
    detail_menu = models.CharField(
        max_length = 5,
        choices = MENU_CHOICES,
        default = MENU_1,
    )
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class question_model(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default = timezone.now)
    file = models.FileField(upload_to='uploads/',default = 'settings.MEDIA_ROOT/uploads/GMH_logo.png')
    text = models.TextField()

    def __str__(self):
        return self.title




