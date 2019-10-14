from django.shortcuts import render

# Create your views here.

def issue_board(request):
    return render(request, 'issue_board.html')