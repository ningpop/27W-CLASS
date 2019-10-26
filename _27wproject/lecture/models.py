from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
# Create your models here.

LECTURE_CATEGORY = [
    ('Art', 'Art'),
    ('Design', 'Design'),
    ('Social Media', 'Social Media'),
]

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='lecture_images/')
    tutor = models.CharField(max_length=50)
    # many to one field
    students = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students", null=True, blank=True)
    deadline = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    category = models.CharField(max_length=20, choices=LECTURE_CATEGORY, default='None') # make category

    def __str__(self):
        return self.title
        
    # delete 오버라이딩
    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Lecture, self).delete(*args, **kargs) # 원래의 delete 함수를 실행


class Review(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # many to one field.
    text = models.TextField()
    score = models.IntegerField()
    created_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
