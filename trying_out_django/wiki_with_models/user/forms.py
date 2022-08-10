from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import modelformset_factory

class create_user(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1")
        def save(self, commit = True):  
            user = User.objects.create_user(  
                self.cleaned_data['username'],  
                self.cleaned_data['email'],  
                self.cleaned_data['password1']  
            )  
            return user


class login_request(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password")
