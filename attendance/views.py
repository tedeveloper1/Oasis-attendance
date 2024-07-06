from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Attend
from .forms import TeamMemberForm, AttendanceForm
from django.utils import timezone

# Home view
def home(request):
    today = timezone.now().date()
    all_members = Team.objects.all()
    attendance_today = Attend.objects.filter(date=today)
    
    attended_member_ids = attendance_today.values_list('member_id', flat=True)
    attended_members = Team.objects.filter(id__in=attended_member_ids)
    absent_members = Team.objects.exclude(id__in=attended_member_ids)

    context = {
        'today': today,
        'attended_members': attended_members,
        'absent_members': absent_members,
    }
    return render(request, 'attendanc/home.html', context)
def view_member(request):
    members = Team.objects.all()
    return render(request, 'attendanc/view_member.html', {'members': members})


# Team member list view
def team_member_list(request):
    attendance_records = Attend.objects.select_related('member').all()
    return render(request, 'attendanc/attendance_list.html', {'attendance_records': attendance_records})

# Create a new team member
def team_member_create(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm()
    
    return render(request, 'attendanc/team_member_form.html', {'form': form})

# Update an existing team member
def team_member_update(request, pk):
    member = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm(instance=member)
    return render(request, 'attendanc/team_member_form.html', {'form': form})

# Delete a team member
def team_member_delete(request, pk):
    member = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('team_member_list')
    return render(request, 'attendanc/team_member_confirm_delete.html', {'member': member})

# Attendance list view
def attendance_list(request):
    attendance_records = Attend.objects.select_related('member').all()
    return render(request, 'attendanc/attendance_list.html', {'attendance_records': attendance_records})

# Create a new attendance record


# Create a new attendance record
# views.py
def attendance_create(request):
    team_members = Team.objects.all()  # Query all team members
    today = timezone.now().date()  # Get today's date
    present_member_ids = Attend.objects.filter(date=today, present=True).values_list('member_id', flat=True)

    if request.method == 'POST':
        selected_members = request.POST.getlist('members')  # Get selected member IDs
        # Delete existing attendance records for today
        Attend.objects.filter(date=today).delete()
        # Create new attendance records
        for member_id in selected_members:
            member = get_object_or_404(Team, pk=member_id)
            Attend.objects.create(
                member=member,
                date=today,
                present=True
            )
        return redirect('attendance_list')

    context = {
        'team_members': team_members,
        'present_member_ids': present_member_ids,
        'date': today,
    }
    return render(request, 'attendanc/attendance_form.html', context)



# Update an existing attendance record
# Update an existing attendance record
# views.py
def attendance_update(request, pk):
    attendance = get_object_or_404(Attend, pk=pk)
    team_members = Team.objects.all()  # Query all team members
    if request.method == 'POST':
        selected_members = request.POST.getlist('members')  # Get selected member IDs
        Attend.objects.filter(date=attendance.date).delete()  # Clear existing records for the date
        for member_id in selected_members:
            member = get_object_or_404(Team, pk=member_id)
            Attend.objects.create(
                member=member,
                date=attendance.date,
                present=True  # Assuming a checkbox tick means present
            )
        return redirect('attendance_list')
    return render(request, 'attendanc/attendance_form.html', {'team_members': team_members, 'date': attendance.date})



# Delete an attendance record
def attendance_delete(request, pk):
    attendance = get_object_or_404(Attend, pk=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'attendanc/attendance_confirm_delete.html', {'attendance': attendance})
