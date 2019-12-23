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
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', views.logout, name = 'logout'),
    path('accounts/agreement/',TemplateView.as_view(template_name = "agreement.html"),name='agreement'),
    path('<int:pk>/update', views.AccountUpdateView.as_view(), name='update_account'),
    path('mypage/<int:pk>', views.get_mypage, name='mypage')
]