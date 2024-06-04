from django import forms 
from .models import *

class MasterForm(forms.ModelForm):
    class Meta:
        model =  User
        fields = ['username','email','password']
        widgets= {'password':forms.PasswordInput}
        help_texts= {'username':''}
        
