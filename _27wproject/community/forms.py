from django import forms
from .models import Community
from ckeditor_uploader.widgets import CKEditorUploadingWidget
 
class CommunityFormModel(forms.ModelForm):
    class Meta:
        model = Community
 
        fields = [
            'title', 
            'user',
            'category',
            'text', 
            ] 
        
        widgets = {
            'title':forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            
            'user': forms.Select(
                attrs={'class': 'custom-select'},
            ),
            
            'category': forms.Select(
                attrs={'class': 'custom-select'},
            ),

            'text': forms.CharField(
                widget=CKEditorUploadingWidget()
            ),
        }