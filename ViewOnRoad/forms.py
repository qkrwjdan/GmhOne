from django import forms
from .models import longway_uploadFile_model
from . models import storyonroad_uploadFile_model,roadview_uploadFile_model

class SelectMenuForm(forms.Form):
    MENU_1 = '길위의 이야기'
    MENU_2 = '먼길가기'
    MENU_3 = '거리탐방'

    MENU_CHOICES = (
        (MENU_1,u"길위의 이야기"),
        (MENU_1,u"먼길가기"),
        (MENU_1,u"거리탐방")
    )
    menu = forms.ChoiceField(choices = MENU_CHOICES)

class SelectMenuForm2(forms.Form):
    MENU_1 = '길위의 이야기'
    MENU_2 = '먼길가기'
    MENU_3 = '거리탐방'

    MENU_CHOICES = (
        (MENU_1,u"길위의 이야기"),
        (MENU_1,u"먼길가기"),
        (MENU_1,u"거리탐방")
    )
    menu = forms.ChoiceField(choices = MENU_CHOICES)

class storyonroad_uploadFileForm(forms.ModelForm):
    class Meta:
        model = storyonroad_uploadFile_model
        fields = ['title','file','text','detail_menu']

class longway_UploadFileForm(forms.ModelForm):
    class Meta:
        model = longway_uploadFile_model
        fields = ['title','file','text','detail_menu']

class roadview_uploadFileForm(forms.ModelForm):
    class Meta:
        model = roadview_uploadFile_model
        fields = ['title','file','text','detail_menu']
