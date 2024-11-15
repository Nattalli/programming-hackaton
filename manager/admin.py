from django.contrib import admin
from .models import UserProfile, Project, Workflow, Task, ProgressLog, Comment


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'bio')
    search_fields = ('user__username', 'role')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'start_date', 'end_date', 'owner')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('name', 'owner__username', 'description')


@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    search_fields = ('name', 'project__name')
    list_filter = ('project',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'due_date', 'assigned_to', 'project')
    list_filter = ('status', 'priority', 'due_date', 'workflow', 'project')
    search_fields = ('title', 'description', 'assigned_to__username', 'project__name')


@admin.register(ProgressLog)
class ProgressLogAdmin(admin.ModelAdmin):
    list_display = ('task', 'progress_percentage', 'updated_at')
    list_filter = ('updated_at', 'progress_percentage')
    search_fields = ('task__title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'task', 'project')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'content', 'task__title', 'project__name')
