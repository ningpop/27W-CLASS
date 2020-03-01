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

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lecture_board, name='lecture_board'),
    path('art/', views.lecture_board_art, name='lecture_board_art'),
    path('design/', views.lecture_board_design, name='lecture_board_design'),
    path('social/', views.lecture_board_social, name='lecture_board_social'),
    path('<int:lecture_id>/', views.lecture_detail, name = 'lecture_detail'),
    path('create/', views.lecture_create, name = 'lecture_create'),
    #path('submit/', views.lecture_submit, name = 'lecture_submit'),
    path('<int:lecture_id>/update/', views.lecture_update, name = 'lecture_update'),
    path('<int:lecture_id>/delete/', views.lecture_delete, name = 'lecture_delete'),
    path('review/',views.review, name="review"),
    path('<int:lecture_id>/confirm_order/', views.confirm_order, name = 'confirm_order'),
    path('<int:lecture_id>/payment/', views.payment, name = 'payment'),
]
