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
from django.urls import path, include
from . import views
# django rest framework -> router -> url

urlpatterns = [
     path('', views.IssueListView.as_view(), name='issue_board'),
     path('create/', views.IssueCreateView.as_view(), name='issue_create'),
     path('<int:pk>/', views.issue_detail, name='issue_detail'),
     # path('comment/write', views.write_comment, name='comment_write'),
     path('<int:pk>/update', views.IssueUpdateView.as_view(), name='issue_update'),
     path('<int:pk>/delete', views.IssueDeleteView.as_view(), name='issue_delete'),
     path('comment/write', views.comment_write, name='comment_write'),
     path('art/', views.issue_board_art, name='issue_board_art'),
     path('design/', views.issue_board_design, name='issue_board_design'),
     path('social/', views.issue_board_social, name='issue_board_social'),
]
