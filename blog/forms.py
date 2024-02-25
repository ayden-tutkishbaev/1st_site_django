from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Article


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',
                  'description',
                  'photo',
                  'category')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Headline'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                              'placeholder': 'username'}))
    password = forms.CharField(label='Password', max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'password'}))


class RegisterUser(UserCreationForm):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                              'placeholder': 'username'}))
    name = forms.CharField(label='Your name', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'name'}))
    email = forms.EmailField(label='Your email address', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'email'}))
    password1 = forms.CharField(label='Create a password', max_length=20,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'password'}))
    password2 = forms.CharField(label='Confirm your password', max_length=20,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ('username',
                  'name',
                  'email',
                  'password1',
                  'password2')
