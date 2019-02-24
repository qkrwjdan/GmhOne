from django import forms
from .models import SignUp,longWay_uploadFile_model,UploadFile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['name','password']
    

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['title','file']

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

class longWay_UploadFileForm(forms.ModelForm):
    class Meta:
        model = longWay_uploadFile_model
        fields = ['title','file','text','detail_menu']
        

