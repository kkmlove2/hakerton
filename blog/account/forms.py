  
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm

user = get_user_model()

class loginForm(AuthenticationForm):
    pass

class registerForm(UserCreationForm):

    birthday = forms.DateField(
           label='birthday',
           widget=forms.widgets.DateInput(attrs={'type':'date'}),
       )

    class Meta:
        model = user
        fields = ['username', 'password1','password2','email','birthday','gender']

class changeForm(UserChangeForm):

    class Meta:
        model = user
        fields = ['username', 'email', 'birthday', 'gender']