from django import forms
from .models import Team, Attend

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['first_name', 'last_name', 'age', 'school_name', 'parent_name', 'address', 'parent_tel']
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attend
        fields = ['date']  # Adjust fields as per your model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
