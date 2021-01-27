from django import forms
from address_book import models

class AddAddressForm(forms.ModelForm):
    class Meta:
        model=models.Address

        fields=['name','email','phone','address','city','state','country','pincode']