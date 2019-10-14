from django.shortcuts import render

# Create your views here.

def lecture_board(request):
    return render(request, 'lecture_board.html')