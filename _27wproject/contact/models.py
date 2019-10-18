from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Answer(models.Model):
    admin = models.CharField(max_length=100) # 미확정
    text = models.TextField()
    created_at = models.DateField(auto_now=True)


class Contact(models.Model):
    # one to one
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    # many to one
    answers = models.ForeignKey(Answer, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
