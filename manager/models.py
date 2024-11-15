from django.db import models
from django.contrib.auth.models import User


class StatusChoices(models.TextChoices):
    BACKLOG = 'backlog', 'Backlog'
    TO_DO = 'to_do', 'To Do'
    IN_PROGRESS = 'in_progress', 'In Progress'
    REVIEW = 'review', 'Review'
    COMPLETED = 'completed', 'Completed'
    ARCHIVED = 'archived', 'Archived'


class RoleChoices(models.TextChoices):
    MANAGER = 'manager', 'Manager'
    USER = 'user', 'User'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50, choices=RoleChoices.choices)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name


class Workflow(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='workflows')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ])
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title


class ProgressLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='progress_logs')
    updated_at = models.DateTimeField(auto_now=True)
    progress_percentage = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Progress for {self.task.title} - {self.progress_percentage}%"


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"
