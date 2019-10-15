from django.shortcuts import render

# Create your views here.

def community_board(request):
    return render(request, 'community_board.html')

def create(request):
    return render(request, 'create.html')

def detail(request):
    return render(request, 'detail.html')  