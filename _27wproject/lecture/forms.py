from django import forms
from .models import Lecture

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['category', 'title', 'tutor', 'price', 'image', 'description']