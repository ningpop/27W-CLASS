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
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.community_board, name='community_board'),
    path('art/', views.community_board_art, name='community_board_art'),
    path('design/', views.community_board_design, name='community_board_design'),
    path('social/', views.community_board_social, name='community_board_social'),
    path('detail/<int:community_id>', views.community_detail, name = 'community_detail'),
    path('create/', views.community_create, name = 'community_create'),
    path('update/<int:community_id>', views.community_update, name = 'community_update'),
    path('delete/<int:community_id>', views.community_delete, name = 'community_delete'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)