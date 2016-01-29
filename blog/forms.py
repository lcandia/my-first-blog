from django import forms

from .models import Post, Comment, Environment, System, Project


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class EnvironmentForm(forms.ModelForm):

    class Meta:
        model = Environment
        fields = ('environment_name', 'weight',)


class SystemForm(forms.ModelForm):

    class Meta:
        model = System
        fields = ('system_name', 'description',)


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('project_name',)