from django import forms
from .models import Issue
from django.db import transaction

ISSUE_CATEGORY = [
    ('Art', 'Art'),
    ('Design', 'Design'),
    ('Social Media', 'Social Media'),
]


class IssueForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

   # form css 넣기 Library https://pypi.org/project/django-widget-tweaks/
    title = forms.CharField(
        error_messages={
            'required': '글의 제목을 입력해주세요.'
        }, label='제목', max_length=100,
        widget=forms.TextInput(attrs={'class':"input-lg"}),
    )
    text = forms.CharField(
        error_messages={
            'required': '내용을 적어주세요.'
        }, label='본문'
    )
    
    image = forms.FileField(
        error_messages={
            'required': '이미지를 넣어주세요.'
        }, label='이미지'
    )

    category = forms.CharField(
        error_messages={
            'required': '카테고리를 설정 해주세요.'
        }, label='카테고리'
    )



    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        image = cleaned_data.get('image')
        category = cleaned_data.get('category')

        if not (title and text and category):
            self.add_error('title', '값이 없습니다')
            self.add_error('text', '값이 없습니다')
            self.add_error('image', '값이 없습니다')
            self.add_error('category', '값이 없습니다')
