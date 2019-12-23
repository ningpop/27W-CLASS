from django.db import models
from django.contrib.auth.models import User
# Create your models here.

ISSUE_CATEGORY = [
    ('Art', 'Art'),
    ('Design', 'Design'),
    ('Social Media', 'Social Media'),
]



class Issue(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    # many to one field
    image = models.ImageField(upload_to='issue_images/')
    category = models.CharField(max_length=20, choices=ISSUE_CATEGORY, default='None') # make category
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:15]


class IssueComment(models.Model):
    # one to one field
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateField(auto_now=True)

