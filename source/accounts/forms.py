from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Имя Пользователя'
    )
    password = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput
    )
    next = forms.CharField(
        required=False,
        widget=forms.HiddenInput
    )


class CustomUserCreationForm(forms.ModelForm):

    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Повторите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
            'email',
        )

        labels = {'email': 'Почта',
                  'username': 'Имя Пользователя',
                  'password_confirm': 'Повторите пароль',
                  'first_name': 'Имя',
                  'last_name': 'Фамилия',
                  }


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароль не совпадает')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email',
        )
        labels = {'email': 'Почта',
                  'first_name': 'Имя',
                  'last_name': 'Фамилия',
                  }
