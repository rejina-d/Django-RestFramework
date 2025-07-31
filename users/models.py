from django.db import models
from django.contrib.auth.models import User

def generateImagePath( instance, file):
    return f'images/{instance.id}/{file}'

# Create your models here.
class Profile(models.Model):
    class RoleOptions(models.TextChoices):
        Employer = 'Employer','Employer'
        Worker = 'Worker','Worker'
        
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    role = models.CharField(max_length=10, choices=RoleOptions.choices, default=RoleOptions.Worker)
    address = models.CharField(blank= True, null= True, max_length=50)
    dob = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(blank= True, null=True, upload_to='images/default_user.jpg')
    