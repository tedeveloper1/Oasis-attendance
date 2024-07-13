from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Attend
import csv
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from .forms import *
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegisterForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'attendanc/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'attendanc/register.html', {'form': form})


            
            

@login_required(login_url='login')
def home(request):
    today = timezone.localtime().date()  # Get the local date based on the timezone
    attended_members = Team.objects.filter(attend__date=today, attend__present=True)
    absent_members = Team.objects.exclude(attend__date=today, attend__present=True)
    
    return render(request, 'attendanc/home.html', {
        'today': today,
        'attended_members': attended_members,
        'absent_members': absent_members
    })
# views.py
import csv
from django.http import HttpResponse



def view_member(request):
    query = request.GET.get('q')
    if query:
        members = Team.objects.filter(first_name__icontains=query) | Team.objects.filter(last_name__icontains=query)
    else:
        members = Team.objects.all()
    
    if 'download' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="team_members.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Age', 'Gender', 'Address', 'School Name', 'Parent Name', 'Parent Tel'])
        
        for member in members:
            writer.writerow([
                member.first_name,
                member.last_name,
                member.age,
                member.gender,
                member.address,
                member.school_name,
                member.parent_name,
                member.parent_tel
            ])
        
        return response
    else:
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
            return redirect('team_member_create')
    else:
        form = TeamMemberForm()
    
    return render(request, 'attendanc/team_member_form.html', {'form': form})

def hand_ball_create(request):
    if request.method == 'POST':
        form = HandballMember(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendanc/hand_ball_create',{'form': form})
        
    else:
        form = HandballMemberForm

    return render(request, 'attendanc/handball_form.html',{'form': form})

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
    selected_date = request.GET.get('date', None)
    if selected_date:
        attendance_records = Attend.objects.filter(date=selected_date)
    else:
        attendance_records = Attend.objects.all()
    
    context = {
        'attendance_records': attendance_records,
        'selected_date': selected_date,
    }
    return render(request, 'attendanc/attendance_list.html', context)


# Create a new attendance record
# views.py
def attendance_create(request):
    team_members = Team.objects.all()  # Query all team members
    today = timezone.localtime().date()  # Get today's date
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


def debug_date(request):
    print(timezone.now())
    return HttpResponse("Check your console for the current time.")

def download_attendance_csv(request):
    # Get the date from the request
    date_str = request.GET.get('date')
    date = parse_date(date_str)

    # Set up the HTTP response for CSV
    response = HttpResponse(content_type='text/csv')
    if date:
        response['Content-Disposition'] = f'attachment; filename="attendance_{date}.csv"'
        attendances = Attend.objects.select_related('member').filter(date=date)
    else:
        response['Content-Disposition'] = 'attachment; filename="attendance.csv"'
        attendances = Attend.objects.select_related('member').all()

    # Create CSV writer
    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Date', 'Status'])

    # Write data rows
    for attendance in attendances:
        writer.writerow([
            attendance.member.id,
            attendance.member.first_name,
            attendance.member.last_name,
            attendance.date,
            'Present' if attendance.present else 'Absent'
        ])

    return response
