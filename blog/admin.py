from django.contrib import admin
from .models import Post, Comment, Subjects, Student
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Subjects)
admin.site.register(Student)