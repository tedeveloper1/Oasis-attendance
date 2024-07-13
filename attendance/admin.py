from django.contrib import admin
from .models import *  # Ensure TeamMember is imported

admin.site.register(Team)
admin.site.register(Attend)
admin.site.register(HandballMember)
admin.site.register(VolleballMember)
admin.site.register(Karate)
admin.site.register(MinFoot)
admin.site.register(Tradition)