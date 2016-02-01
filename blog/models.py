from django.db import models

# Create your models here.
from django.utils import timezone

from datetime import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

# Modelo para crear formularios
class Subjects(models.Model):
    sub_name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)


class Student(models.Model):
    name=models.CharField(max_length=100)
    subject=models.ManyToManyField(Subjects)


class Environment(models.Model):
    environment_name = models.CharField(max_length=200)
    weight = models.BigIntegerField()
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField('date created', auto_now_add=True)

    class Meta:
        ordering = ('environment_name',)

    def __str__(self):
        return self.environment_name


class System(models.Model):
    system_name = models.CharField(max_length=25)
    description = models.TextField()
    created = models.DateTimeField('date created', auto_now_add=True)
    status = models.BooleanField(default=True)
    environments = models.ManyToManyField(Environment)

    class Meta:
        ordering = ('system_name',)

    def __str__(self):
        return self.system_name


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField('date created', auto_now_add=True)

    class Meta:
        ordering = ('project_name',)

    def __str__(self):
        return self.project_name
