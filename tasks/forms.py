from django import forms
from .models import Task

class createTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write a task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a task description'
            }),
            'important': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'border: 1px solid black'
            })
        }