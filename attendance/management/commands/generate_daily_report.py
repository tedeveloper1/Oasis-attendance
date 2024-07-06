# generate_daily_report.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.template.loader import render_to_string
from attendance.models import Team, Attend
import os

class Command(BaseCommand):
    help = 'Generate daily attendance report'

    def handle(self, *args, **options):
        today = timezone.localtime().date()
        attended_members = Team.objects.filter(attend__date=today, attend__present=True)
        absent_members = Team.objects.exclude(attend__date=today, attend__present=True)

        # Render the report
        report_html = render_to_string('attendance/daily_report.html', {
            'today': today,
            'attended_members': attended_members,
            'absent_members': absent_members,
        })

        # Define the report path
        report_path = os.path.join('reports', f'report_{today}.html')
        os.makedirs(os.path.dirname(report_path), exist_ok=True)

        # Save the report
        with open(report_path, 'w') as f:
            f.write(report_html)

        self.stdout.write(self.style.SUCCESS(f'Report for {today} generated at {report_path}'))
