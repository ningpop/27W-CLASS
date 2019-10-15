"""_27wclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
import home.views
import accounts.views
import community.views
import contact.views
import issue.views
import lecture.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.community_board, name='community_board'),
    path('detail/', views.detail, name = 'detail'),
    path('create/', views.create, name = 'create'),

    #path('community_board/', .views.community_board, name = 'community_board'),
    
    #path('contact/contact_board', contact.views.contact_board, name = 'contact_board'),
    
    #path('issue/issue_board', issue.views.issue_board, name = 'issue_board'),
    
    #path('lecture/lecture_board', lecture.views.lecture_board, name = 'lecture_board'),
]