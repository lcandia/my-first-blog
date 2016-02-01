from django.contrib import admin
from .models import Post, Comment, Subjects, Student, Environment, System, Project
#from .forms import SystemForm
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Subjects)
admin.site.register(Student)
admin.site.register(Environment)
admin.site.register(System)
admin.site.register(Project)

#class SystemAdmin(admin.ModelAdmin):
#    form = SystemForm
#    filter_horizontal = ('environments',)