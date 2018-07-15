from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'dob']


class DynamicForm(forms.Form):
    dropdown = forms.Select(choices=(('menu_1', 'Menu 1'), ('menu_2', 'Menu 2')))
