from rest_framework import routers
from .viewsets import ProjectViewSet

app_name= "users"
router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)