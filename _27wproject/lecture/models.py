from django.db import models
from django.contrib.auth.models import User
# Create your models here.

LECTURE_CATEGORY = [
    ('Art', 'Art'),
    ('Design', 'Design'),
    ('Social Media', 'Social Media'),
]

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    image = models.ImageField()
    tutor = models.CharField(max_length=50)
    # many to one field
    students = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students", null=True, blank=True)
    deadline = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    category = models.CharField(max_length=20, choices=LECTURE_CATEGORY, default='Art') # make category


class Review(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # many to one field.
    text = models.TextField()
    score = models.IntegerField()
    created_at = models.DateField(auto_now=True)