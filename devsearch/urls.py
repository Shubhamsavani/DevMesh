from django.contrib import admin
from django.urls import path, include #'from django.urls import include' to connect the urls.py of the apps file from the projects folder in this case 
from django.conf import settings
from django.conf.urls.static import static #IMPORTING THIS FOR RENDERING IMAGES IN OUR project.html template --- you also need to first add <MEDIA_URL= '/images/'> in settings.py file 
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('projects/', include('projects.urls')),
    path('', include('users.urls')), #this line will connect the url.py file from users to our project
]
 #for 7th line this line will connect the url.py file from the projects folder... i.e. if the url has something like '' than it will check in the url.py file from projects(our app)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #what we are doing here is basically taking the MEDIA_URL and adding it to MEDIA_ROOT which is passed to the project.html template
# urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)