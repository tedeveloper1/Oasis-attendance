from django.contrib import admin
from .models import Team, Attend  # Ensure TeamMember is imported

admin.site.register(Team)
admin.site.register(Attend)