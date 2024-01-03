

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Username or Email',
        widget=forms.TextInput(attrs={'autofocus': True}),
    )

    def clean_username(self):
        identifier = self.cleaned_data.get('username')
        UserModel = get_user_model()

        if '@' in identifier:
            try:
                user = UserModel.objects.get(email=identifier)
            except UserModel.DoesNotExist:
                raise forms.ValidationError("User with this email does not exist.")
            return user.username
        else:
            return identifier

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
