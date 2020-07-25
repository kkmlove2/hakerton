from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm

user = get_user_model()

class loginForm(AuthenticationForm):
    pass

class registerForm(UserCreationForm):

    class Meta:
        model = user
        fields = ['username', 'password1','password2','email','birthday','gender']

class changeForm(UserChangeForm):

    class Meta:
        model = user
        fields = ['username', 'email', 'birthday', 'gender']