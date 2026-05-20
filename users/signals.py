from django.db.models.signals import post_save, post_delete
# importing the models 
from django.contrib.auth.models import User
from .models import Profile



# @receiver(post_save, sender=Profile) #you can also call the receiver like this but for this we have to imort the receiver but Note that most f the 3rd party signals will be using this syntax 
def createProfile (sender, instance, created, **kwargs):
    # here we will write logic to automatically create a profile when a user is created
    if created:
        user= instance #the instance will contain the user data of the instance that triggered this event so we saveit in user for firther ease 
        profile= Profile.objects.create(
            user=user, #here we set the user in the profile to our instnace 
            username=user.username,
            email=user.email,
            name=user.first_name,
            )

# for deleting the user we do not need to make a signal as we have already set the profile to CASCADE and will delete the profile if auser is deleted 
def deleteUser(sender, instance, **kwargs): 
    user=instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender= Profile)