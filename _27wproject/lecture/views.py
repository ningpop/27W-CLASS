from django.shortcuts import render, get_object_or_404

# Create your views here.

def lecture_board(request):
    return render(request, 'lecture_board.html')

def lecture_detail(request):
    return render(request, 'lecture_detail.html')