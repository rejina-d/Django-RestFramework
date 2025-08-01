from django.db import models
from django.contrib.auth.models import User

def generateImagePath(instance, file):
    return f'images/projects{instance.user.username}/{file}'

# Create your models here.
class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        IN_PROGRESS = 'In Progress', 'In Progress'
        COMPLETED = 'Completed', 'Completed'
        CANCELED = 'Canceled', 'Canceled'
        PENDING = 'Pending', 'Pending'
        
    class PriorityOptions(models.TextChoices):
        LOW = 'Low', 'Low'
        MEDIUM = 'Medium', 'Medium'
        HIGH = 'High', 'High'
        
    
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null= True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to= models.ManyToManyField(User, blank=True, null= True, related_name='assigned_projects')
    status = models.CharField(max_length=11, choices=ProjectStatus.choices, default=ProjectStatus.PENDING)
    priority = models.CharField(max_length=11, choices=PriorityOptions.choices, default=PriorityOptions.MEDIUM)
    image= models.ImageField(upload_to=generateImagePath, blank=True, null=True, default ="images/projects/default.jpg")
    start_date= models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.title
    
    
    
