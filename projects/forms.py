from django.forms import ModelForm
from django import forms 
from .models import Project

class ProjectForm(ModelForm): #here you can keep whatever name you want of the forms just remember to use the same name in views.py
    class Meta:
        model = Project # here we specify name of the model(datat_base)
        fields = ['title','description', 'image','demo_link','source_link','tags'] #this will create form fiedlds for the attributes passed in the list. for form with all field " fields= '__all__' "
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        } #we here made the tags input field to look like a checkbox ather than user needing to press ctrl and select it we could have modified the class by this but we are going to override init method to do so 
        #now we are going to override the __init__ method and *args is arguments and **kwargs is kew word arguments  
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for k,v in self.fields.items():#this lines simply means for every key value pair in self-> fields-> items() do the following thing 
            v.widget.attrs.update({'class': 'input'})   
        #adding class to each individual element is lengthy proceess so we need to loop it as above
        # self.fields['title'].widget.attrs.update({"class": "input",})