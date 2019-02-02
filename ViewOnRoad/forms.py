from django import forms
from .models import SignUp,UploadFile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['name','password']
    

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['title','file']