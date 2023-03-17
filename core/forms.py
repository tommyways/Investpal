from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from currency.models import Contact
# from .models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'w-full py-4 px-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-4 px-6 rounded-xl'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'country','first_name','last_name')

    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'w-full py-4 px-4 px-6 rounded-xl'
    }))
    email = forms.CharField(help_text=False,widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address',
        'class': 'w-full py-4 px-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Confirm Password',
        'class': 'w-full py-4 px-4 px-6 rounded-xl'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First name',
        'class': 'w-full py-4 px-4 px-6 rounded-xl'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last name',
        'class': 'w-full py-4 px-4 px-6 rounded-xl'
    }))
    country = forms.CharField(widget=forms.TextInput)




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('cryptocurrency' ,'amount', 'receiver_wallet')
    cryptocurrency = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Example : Bitcoin",
        'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'
    }))
    amount = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Amount',
        'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'
    }))
    receiver_wallet = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Receiver's Wallet",
        'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'
    }))


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={
                                'placeholder': "Username",
                                'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'
                               }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                'placeholder': "Email",
                                'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'

                             }))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'bio']

    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'placeholder': "",
        'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'
    }))
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Bio",
        'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'
    }))


# class WithdrawalForm(forms.Form):
#     class Meta:
#         model = Withdraw
#         fields = ('cryptocurrency' ,'amount', 'receiver_wallet',)
#     cryptocurrency = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': "Example : Bitcoin",
#         'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'
#     }))
#     amount = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Amount',
#         'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'
#     }))
#     receiver_wallet = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': "Receiver's Wallet",
#         'class': 'w-full py-4 px-4 px-6 rounded-xl bg-blue-200'
#     }))
    