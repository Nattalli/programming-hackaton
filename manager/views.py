from rest_framework.viewsets import ModelViewSet
from manager.models import UserProfile, Project, Workflow, Task, ProgressLog, Comment
from manager.permissions import IsManager
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
    # permission_classes = [IsManager]


class WorkflowViewSet(ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        if project_id:
            return self.queryset.filter(project_id=project_id)
        return self.queryset


class ProgressLogViewSet(ModelViewSet):
    queryset = ProgressLog.objects.all()
    serializer_class = ProgressLogSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
