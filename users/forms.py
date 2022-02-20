from django import forms
from . import models
from django.contrib.auth.models import User

class profileForm(forms.ModelForm):
    password1 = forms.CharField(required=True,widget=forms.PasswordInput())
    password2 = forms.CharField(required=True,widget=forms.PasswordInput())
    class Meta:
        model = models.profile
        #model = models.profile  
        fields = ["username",
        "first_name",
        "last_name",
        "email",
        "MobileNumber",
        "birthday",
        "profileimage",
        "password1",
        "password2"]
