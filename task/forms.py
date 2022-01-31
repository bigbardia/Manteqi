from task.models import Task
from django import forms

class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(label="enter your task" , widget=forms.TextInput())
    class Meta:
        model = Task
        fields = ["title"]
