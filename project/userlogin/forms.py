from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import authorization

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None

# class CustomerRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget = forms.PasswordInput())
#     Confirm_Password = forms.CharField(widget= forms.PasswordInput())
#     class Meta:
#         model = authorization
#         fields = ["username", "name", "position", "company_name" ,"email","password","Confirm_Password"]
#         widgets = {
#             'username' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'name' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'position' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'company_name' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
#             'password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
#             'Confirm_Password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         super(CustomerRegistrationForm, self).__init__(*args, **kwargs)
#         self.fields['password'].widget.attrs['class'] = 'form-control'
#         self.fields['Confirm_Password'].widget.attrs['class'] = 'form-control'