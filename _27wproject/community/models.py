from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
category = ()
"""

class CommunityComment(models.Model):
    # one to one field
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now=True)

class Community(models.Model):
    # one to one field
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    # many to one field
    #필수 입력란으로 되어있음, 테스트를 위해 주석 처리
    #comments = models.ForeignKey(CommunityComment, on_delete=models.CASCADE)
    image = models.ImageField()
    category = models.IntegerField()
    created_at = models.DateField(auto_now=True)
    #like = models.IntegerField()  # 미확정
    #unlike = models.IntegerField() # 미확정