from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from .permissions import *

class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectOwnerOrReadOnly, ]