from django.urls import path, include
from rest_framework.routers import DefaultRouter
from manager.views import UserProfileViewSet, ProjectViewSet, WorkflowViewSet, TaskViewSet, ProgressLogViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'workflows', WorkflowViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'progress-logs', ProgressLogViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
