from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
# Create your models here.

class Contact(models.Model):
    # one to one
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    # many to one
    #answers = models.ForeignKey(Answer, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True, related_name='contact')
    admin = models.CharField(max_length=100) # 미확정
    text = models.TextField()
    created_at = models.DateField(auto_now=True)