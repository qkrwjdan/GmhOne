from django import forms
from .models import longway_uploadFile_model
from . models import storyonroad_uploadFile_model,roadview_uploadFile_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

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
<<<<<<< HEAD
        fields = ['title','file','text']

class storyonroad_uploadFileForm(forms.ModelForm):
    class Meta:
        model = storyonroad_uploadFile_model
        fields = ['title','file','text']

class UserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
 
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
=======
        fields = ['title','file','text','detail_menu']
>>>>>>> e72bb57b00cf654f4ced432f41d2ccdddb1b226a
