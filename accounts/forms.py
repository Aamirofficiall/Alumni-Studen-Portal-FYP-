from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ValidationError

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(
        attrs={
            'type':'email',
            'class':'input100',
            
        }
    ))
    password=forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'password',
            'class':'input100',
        }
    ))
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(widget=forms.TextInput(
        attrs={
            'type':'email',
            'class':'input100',
            
        }
    ))
    password1=forms.CharField(label="Password ",widget=forms.TextInput(
        attrs={
            'type':'password',
            'class':'input100',
    
        }
    ))
    password2=forms.CharField(label="Password Confirmation",widget=forms.TextInput(
        attrs={
            'type':'password',
            'class':'input100',
        }
    ))
    class Meta:
        model=User
        fields=['email','password1','password2']
                
        def clean_email(self):
            email = self.cleaned_data['email']
            pass1 = self.cleaned_data['password1']
            pass2 = self.cleaned_data['password2']
            if pass1!=pass2:
                raise ValidationError("Password did'nt match")
            user=User.objects.get(email=email)
            if  user:
                raise ValidationError('A user with same email exist')


            return email

class UpdateUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email']