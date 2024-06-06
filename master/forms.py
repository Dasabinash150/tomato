from django import forms 
from .models import *

class MasterForm(forms.ModelForm):
    class Meta:
        model =  User
        fields = ['username','email','password']
        widgets= {'password':forms.PasswordInput}
        help_texts= {'username':''}
        
class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'item_id': forms.TextInput(attrs={'class': 'form-control'}),
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'item_desc': forms.Textarea(attrs={'class': 'form-control','rows': 5, 'cols': 40 }),
            'item_type': forms.Select(attrs={'class': 'form-control'}),
            'item_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        exclude = ['item_id']