from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    ROLES = [
        ('student', 'Student'),
        ('technician', 'Technician')
    ]

    role = forms.ChoiceField(choices=ROLES)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }
