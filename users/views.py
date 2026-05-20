from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.models import User   
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.db.models import Q
from .models import Profile, Skill
from .form import CustomUserCreationForm, profileform, skillform
from .util import profile_filter
# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('profiles')#this will redirect the user when he is logged in to profiles rather than to show him login page i.e. restrict the user to see login poge again when he is logged in 
    if request.method == 'POST':
        u_name = request.POST.get('username') #this will get the username and password from the POST request and store it into variable 
        u_pass = request.POST.get('password')
        
        try: 
            user= User.objects.get(username=u_name)
        except:
            messages.error(request, "User does not exist.")  

        user = authenticate(request, username=u_name, password=u_pass) # now we match the username with the password and see that both matches for the same user or not and below are the conditions to follow 
        if user is not None:
            login(request, user)
            return redirect('profiles') 
        else:
            messages.error(request, "Username or password is incorrect.")
    page = 'login'
    arg = {'page': page, }
    return render (request, 'users/login_register.html', arg)
def logoutuser (request):
    logout(request)
    messages.info(request, "User was successfully loggedout!")
    return redirect('loginpage')

def registeruser (request):
    page =  'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # here we hold an instance of user and not commit it in order to make sure that the username is in lowercase only 
            user.username = user.username.lower()
            form.save()
            messages.success(request, "User was successfully registered")
            login (request, user)
            return redirect('editaccount')
        else:
            messages.error(request, "An error has occured during regestration.")
    arg = {'page': page, 'form': form, }
    return render(request, 'users/login_register.html', arg)

def profiles(request):
    profiles, search_query = profile_filter(request)
    arg= {'profiles':profiles, 'search_query': search_query}
    return render(request, 'users/all_profiles.html', arg)


def userprofile(request, pk):
    profile=Profile.objects.get(id=pk)
    skills= profile.skill_set.exclude(description__exact="")
    other_skill=profile.skill_set.filter(description="")
    arg= {'profile':profile,'skills':skills, 'other_skill':other_skill}
    return render(request, 'users/user_profile.html', arg)
    
@login_required(login_url='login')
def userAcc(request):
    profile= request.user.profile

    arg ={'profile': profile}
    return render (request, 'users/account.html', arg)

@login_required(login_url='login')
def editaccount(request):
    profile= request.user.profile
    form = profileform(instance=profile)
    if request.method == 'POST':
        form = profileform(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            form.save()
            return redirect('useracc')

    arg ={'form':form}
    return render(request, 'users/profileform.html', arg)

@login_required(login_url='login')
def createskill(request):
    profile = request.user.profile
    form = skillform() 
    arg ={'form': form}
    if request.method == 'POST':
        form = skillform(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit = False)
            form.owner = profile 
            form.save()
            messages.success(request, 'Skill was added successfully')
            return redirect('useracc')
    return render (request, 'users/skillform.html', arg)

@login_required(login_url='login')
def editskill(request, pk):
    profile= request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = skillform(instance= skill)

    if request.method == 'POST':
        form= skillform(request.POST, instance= skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'skill was updated successfully')
            return redirect ('useracc')
    arg={'form':form}
    return render(request, 'users/skillform.html', arg)

@login_required(login_url='login')
def deleteskill (request, pk):
    profile= request.user.profile
    skill= profile.skill_set.get(id=pk)
    if request.method =='POST':
        skill.delete()
        messages.success(request,'Skill was deleted successfully!')
        return redirect('useracc')
        
    arg= {'object': skill.name}
    return render (request, 'delete_template.html', arg  )