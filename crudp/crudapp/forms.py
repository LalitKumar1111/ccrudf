from django import forms
from .models import User


class Crudform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'phone', 'email', 'address']