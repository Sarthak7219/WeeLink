from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-0',
        'placeholder': 'Your Full Name'
    }))

    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-0',
        'placeholder': 'Username'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-0',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-0',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['full_name', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['full_name']
        if commit:
            user.save()
        return user
