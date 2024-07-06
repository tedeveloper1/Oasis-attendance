from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.team_member_list, name='team_member_list'),
    path('view_member', views.view_member, name='view_member'),
    path('members/<int:pk>/', views.team_member_update, name='team_member_update'),
    path('members/<int:pk>/delete/', views.team_member_delete, name='team_member_delete'),
    path('members/new/', views.team_member_create, name='team_member_create'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/new/', views.attendance_create, name='attendance_create'),

]
