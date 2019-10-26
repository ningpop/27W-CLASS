from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture
from django.utils import timezone
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
    return render(request, 'lecture_detail.html', {'lecture': lecture_detail})

def lecture_create(request):
    return render(request, 'lecture_create.html')

def submit(request):
    lecture = Lecture()
    lecture.category = request.POST['category']
    lecture.title = request.POST['title']
    lecture.image = request.FILES['image']
    lecture.description = request.POST['content']
    lecture.created_at = timezone.datetime.now()
    lecture.save()
    return redirect('/lecture/' + str(lecture.id))
