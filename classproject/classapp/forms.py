from django import forms
from .models import myUser,Fooditem,Reviews
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Usercreate(forms.ModelForm):
    class Meta:
        model=myUser
        fields='__all__'

class createFooditem(forms.ModelForm):
    class Meta:
        model=Fooditem
        fields='__all__'

class createReviews(forms.ModelForm):
    class Meta:
        model=Reviews
        fields='__all__'

class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","password1","password2")