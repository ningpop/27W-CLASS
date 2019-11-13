from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Community, Lecture, Issue
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    community_list = Community.objects.all().order_by('-id')[:6]
    lecture_list = Lecture.objects.all().order_by('-id')[:6]
    issue_list = Issue.objects.all().order_by('-id')[:6]
    return render(request, 'index.html', {'community_list': community_list, 'lecture_list': lecture_list, 'issue_list': issue_list})