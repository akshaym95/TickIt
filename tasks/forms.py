from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Task

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the widgets for better styling
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose a username...'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password...'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password...'
        })
        
        # Customize help text
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters.'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'
        
        # Customize error messages
        self.fields['username'].error_messages = {
            'required': 'Please enter a username.',
            'unique': 'This username is already taken. Please choose a different one.',
            'max_length': 'Username cannot be longer than 150 characters.',
            'invalid': 'Username can only contain letters, digits, and @/./+/-/_ characters.'
        }
        
        self.fields['password1'].error_messages = {
            'required': 'Please enter a password.',
            'password_too_short': 'Password must be at least 8 characters long.',
            'password_too_common': 'This password is too common. Please choose a stronger password.',
            'password_entirely_numeric': 'Password cannot be entirely numeric.'
        }
        
        self.fields['password2'].error_messages = {
            'required': 'Please confirm your password.',
            'password_mismatch': 'The two password fields do not match.'
        }
    
    def clean_username(self):
        """Custom validation for username to provide better error messages"""
        username = self.cleaned_data.get('username')
        if username:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                raise ValidationError(
                    'This username is already taken. Please choose a different one.',
                    code='username_taken'
                )
        return username

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter task description (optional)...'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control'
            })
        } 