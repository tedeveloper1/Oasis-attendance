from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('members/', views.team_member_list, name='team_member_list'),
    path('handball/new/', views.hand_ball_create, name='hand_ball_create'),
    path('view_member', views.view_member, name='view_member'),
    path('members/<int:pk>/', views.team_member_update, name='team_member_update'),
    path('members/<int:pk>/delete/', views.team_member_delete, name='team_member_delete'),
    path('members/new/', views.team_member_create, name='team_member_create'),
    path('valleball/new/', views.volleyball_create, name='volleyball_create'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('valley_attendance_list', views.valley_attendance_list, name='valley_attendance_list'),
    path('download-attendance/', views.download_attendance_csv, name='download_attendance_csv'),
    path('attendance/new/', views.attendance_create, name='attendance_create'),
    path('vally_ballattendance_create', views.vally_ballattendance_create, name='vally_ballattendance_create'),
    path('volleyball_management/', views.volleyball_management, name='volleyball_management'),
    path('handball_management/', views.handball_management, name='handball_management'),
    path('basketball_management/', views.basketball_management, name='basketball_management'),
    path('karate_management/', views.karate_management, name='karate_management'),
    path('dance_management/', views.dance_management, name='dance_management'),

]
