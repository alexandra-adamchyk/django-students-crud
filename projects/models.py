# Teaser (Trailer,  big picture)
# Forget about it.. "M"
# MTV =>models, template, view
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Stage(models.Model):
    name = models.CharField(max_length=50, unique=True)   
    order_no = models.PositiveIntegerField()


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # relationships
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')
    stage = models.ForeignKey(Stage, on_delete=models.RESTRICT, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add means use the time at which the object is created
    updated_at = models.DateTimeField(auto_now=True)
