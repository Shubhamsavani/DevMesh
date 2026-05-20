from django.shortcuts import render, redirect
from django.http import HttpResponse #import this file for makeing the function work
from django.contrib.auth.decorators import login_required
from .models import Project
from .utils import search_projects, pagination
from .forms import ProjectForm
from django.db.models import Q

def projects(request):
    project, search_query = search_projects(request)
    # project, p_range = pagination (request, project)
    argument={'project': project, 'search_query': search_query, } #'page_range':p_range
    return render(request,'projectsApp/all_projects.html', argument)

def project(request, pk):
    #return HttpResponse("Project"+' '+str(pk))# this will show "Project(id) on the screen"... usage of this is when u need to also pass an id 
    arg=Project.objects.get(id=pk)
    tags= arg.tags.all() #you can query manytomany relation from here or may also query it from html  <!-- you can also query the manytomany relation from here also by writing {% for tag in project.tags.all %} -->   
    argument1={'project': arg, 'tags': tags}
    return render(request,'projectsApp/project.html',argument1 )#used to render the html file from templates folder

@login_required(login_url='loginpage')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form= ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit= False)
            project.owner = profile
            form.save()
        return redirect('useracc') 
    content={'form': form}
    return render(request,'projectsApp/projects_form.html',content)

@login_required(login_url='loginpage')
def edit_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk) #this will get the project from the db 
    form = ProjectForm(instance=project) #here we use the same form 
    if request.method == 'POST':
        form= ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
        return redirect('useracc') 
    content={'form': form}
    return render(request,'projectsApp/projects_form.html',content)

@login_required(login_url='loginpage')
def delete_project(request,pk):
    profile= request.user.profile
    arg= profile.project_set.get(id=pk)
    if request.method == 'POST':
            arg.delete()
            return redirect('useracc')
    content={'object': arg.title}
    return render(request,'delete_template.html', content)