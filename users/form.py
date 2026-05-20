from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill

class CustomUserCreationForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels ={
            'first_name': 'Name',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for k,v in self.fields.items():
            v.widget.attrs.update({'class': 'input'})

class profileform (ModelForm):
    class Meta:
        model= Profile
        fields = ['name', 'email', 'username', 'location','short_intro', 'bio','profile_image', 'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website'] 
    def __init__ (self, *args, **kwargs):
        super(profileform, self).__init__(*args, **kwargs)
        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})

class skillform (ModelForm):
    class Meta:
        model= Skill
        fields =['name', 'description']
    
    def __init__ (self, *args, **kwargs):
        super(skillform, self).__init__(*args, **kwargs)
        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})