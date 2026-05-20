from django.db import models
import uuid


from users.models import Profile
# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title= models.CharField(max_length=200)
    image= models.ImageField(null=True, blank=True, default='default.jpg')
    description= models.TextField(null=True, blank=True)
    demo_link= models.CharField(max_length=2000, null=True, blank=True)
    source_link= models.CharField(max_length=2000, null=True, blank=True)
    tags= models.ManyToManyField('Tag', blank=True)
    vote_total= models.IntegerField(default=0,null=True, blank=True)
    vote_ratio= models.IntegerField(default=0,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title 

    class Meta: 
        ordering = ['created'] #-created will arrange in descending order 

class Review (models.Model): # this is going to be in one to many relationship with Projevct // we also need to create a attribute in projects as vote which displays the votes <check the project class for vote_total and vote_ratio attribute>
    VOTE_TYPE =(
        ('up', 'Up Vote'),#here up is the database representation and Up Vote is how it is going to display to the user
        ('down', 'Down Vote')
    )
    #owner:
    #CASCADE is used to delete the review in case the project is deleted you can also  use SET_NULL which will set the project name to NULL and let the rewiew exist in our database 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=20, choices=VOTE_TYPE) #this choices parameter is going to be a drop down list with options as Up Vote and Down Vote
    created = models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.value

class Tag (models.Model): #this is going to be a many to many relationship with the project// we also need to create a attribute in the project as tags <check projects for the tags attribute details>
    name= models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name