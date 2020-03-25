from django.contrib import admin
from .models import Community
from .models import CommunityComment

# Register your models here.
admin.site.register(Community)
admin.site.register(CommunityComment)