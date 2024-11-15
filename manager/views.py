from rest_framework.viewsets import ModelViewSet
from manager.models import UserProfile, Project, Workflow, Task, ProgressLog, Comment
from manager.serializers import (
    UserProfileSerializer,
    ProjectSerializer,
    WorkflowSerializer,
    TaskSerializer,
    ProgressLogSerializer,
    CommentSerializer,
)


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class WorkflowViewSet(ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProgressLogViewSet(ModelViewSet):
    queryset = ProgressLog.objects.all()
    serializer_class = ProgressLogSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
