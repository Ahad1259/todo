from django import forms
from . models import Task

class TaskFrom(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["user", "is_completed"]
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-md mt-2 px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter Title Here'
            }),
            'discription': forms.TextInput(attrs={
                'class': 'w-md mt-2 px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter Discription Here',
                'min' : '0'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'w-md mt-2 px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400',
                'type' : 'date'
            }),
            'due_time': forms.TimeInput(attrs={
                'class': 'w-md mt-2 px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400',
                'type' : 'time'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select px-4 py-2 rounded border border-gray-300 w-md',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select px-4 py-2 rounded border border-gray-300 w-md',
            }),
            }