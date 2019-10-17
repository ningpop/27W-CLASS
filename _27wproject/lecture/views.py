from django.shortcuts import render, get_object_or_404
from .models import Lecture
# Create your views here.

'''
def lecture_board(request):
    return render(request, 'lecture_board.html')
'''

def lecture_board(request):
    lecture_list = Lecture.objects
    return render(request, 'lecture_board.html', {'lecture_list': lecture_list})

'''
def lecture_detail(request):
    return render(request, 'lecture_detail.html')
'''

def lecture_detail(request, lecture_id):
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'lecture_board.html', {'lecture': lecture_detail})
