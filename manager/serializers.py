from rest_framework import serializers
from manager.models import UserProfile, Project, Workflow, Task, ProgressLog, Comment


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = '__all__'


class WorkflowSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()

    class Meta:
        model = Workflow
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    workflow = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = '__all__'


class ProgressLogSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()

    class Meta:
        model = ProgressLog
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    task = serializers.StringRelatedField()
    project = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'
