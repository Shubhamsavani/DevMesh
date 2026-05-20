from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # here we connect the signals to our main app 
    def ready(self):
        import users.signals