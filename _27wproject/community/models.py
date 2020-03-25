from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


COMMUNITY_CATEGORY = [
    ('Art', 'Art'),
    ('Design', 'Design'),
    ('Social Media', 'Social Media'),
]

class Community(models.Model):
    #https://blog.hannal.com/2015/06/start_with_django_webframework_08/
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  
    ##추가
    
    title = models.CharField(max_length=100)
    text = RichTextUploadingField()

    category = models.CharField(max_length=20, choices=COMMUNITY_CATEGORY, default='None') # make category
    created_at = models.DateField(auto_now=True)

    def get_user(self):
        return User.objects.get(pk=self.user_id)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Community.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Community, self).save(*args, **kwargs)


class CommunityComment(models.Model):
    # one to one field
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text