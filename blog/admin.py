from django.contrib import admin
from .models import Post, Comment, Subjects, Student, Environment, System, Project
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Subjects)
admin.site.register(Student)
admin.site.register(Environment)
admin.site.register(System)
admin.site.register(Project)