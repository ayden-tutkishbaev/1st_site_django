from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, \
    UserCreationForm

from .models import Article, Profile, Comment


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
    first_name = forms.CharField(label='Your first name', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'First name'}))
    last_name = forms.CharField(label='Your last name', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                      'placeholder': 'Last name'}))
    # name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control',
    #                                                                    'placeholder': 'name'}))
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
                  # 'name',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                              'placeholder': 'username'}))
    first_name = forms.CharField(label="Your first name",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Your first name'
                                 }))
    last_name = forms.CharField(label="Your last name",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Your last name'
                                }))

    email = forms.EmailField(label='Your email address', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'phone',
            'address',
            'job',
            'image',
            'description'
        )

    widgets = {
        'job': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Job'
        }),
        'address': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Job'
        }),
        'phone': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone'
        }),
        'image': forms.FileInput(attrs={
            'class': 'form-control'
        }),
        'description': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'About yourself'
        })
    }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Your comment"
            })
        }