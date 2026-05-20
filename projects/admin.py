from django.contrib import admin
from .models import Project, Review, Tag #this will import Project from models.py 
admin.site.register(Project) #this will register out table in admin panel and we can now see it there and perform CRUD operations in our DB
admin.site.register(Review)
admin.site.register(Tag)
