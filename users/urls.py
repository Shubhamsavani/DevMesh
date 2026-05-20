from django.urls import path
from . import views

urlpatterns = [
    path('',views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userprofile, name='userprofile'),
    path('login/', views.loginpage, name='loginpage'),
    path('logout/', views.logoutuser , name='logoutpage'),
    path('register/', views.registeruser, name='registeruser'),
    path('account/', views.userAcc, name='useracc'),
    path ('account_edit/', views.editaccount, name='editaccount'),
    path('create-skill/', views.createskill, name='createskill'),
    path('update_skill/<str:pk>', views.editskill, name='update_skill'),
    path('deleteskill/<str:pk>', views.deleteskill, name='deleteskill'),
]