from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TeamMemberForm(forms.ModelForm):
     class Meta:
        model = Team
        fields = ['first_name', 'last_name', 'age','gender' ,'school_name', 'parent_name', 'address', 'parent_tel']
        widgets = {
            'gender': forms.RadioSelect(choices=Team.GENDER_CHOICES),
        }

class HandballMemberForm(forms.ModelForm):
    class Meta:
        model = HandballMember
        fields = ['first_name', 'last_name', 'age','gender' ,'school_name', 'parent_name', 'address', 'parent_tel']
        widgets = {
            'gender':forms.RadioSelect(choices=HandballMember.GENDER_CHOICES),
        }

class ValleyballMemberForm(forms.ModelForm):
    class Meta:
        model = VolleballMember
        fields = ['first_name', 'last_name', 'age','gender' ,'school_name', 'parent_name', 'address', 'parent_tel']
        widgets = {
            'gender':forms.RadioSelect(choices=HandballMember.GENDER_CHOICES),
        }
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attend
        fields = ['date']  # Adjust fields as per your model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


