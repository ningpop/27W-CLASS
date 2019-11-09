from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture, Review
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

'''
def lecture_board(request):
    return render(request, 'lecture_board.html')
'''

def lecture_board(request):
    lectures = Lecture.objects
    lecture_list = Lecture.objects.all()
    paginator = Paginator(lecture_list, 12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'lecture_board.html', {'lectures': lectures, 'posts': posts})

'''
def lecture_detail(request):
    return render(request, 'lecture_detail.html')
'''

def lecture_detail(request, lecture_id):
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'lecture_detail.html', {'lecture': lecture_detail})

def lecture_create(request):
    return render(request, 'lecture_create.html')

def lecture_submit(request):
    lecture = Lecture()
    lecture.category = request.POST['category']
    lecture.title = request.POST['title']
    lecture.image = request.FILES['image']
    lecture.price = request.POST['price']
    lecture.description = request.POST['content']
    lecture.created_at = timezone.datetime.now()
    lecture.save()
    return redirect('/lecture/' + str(lecture.id))

def lecture_delete(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    lecture.delete()
    return redirect('/lecture/')

def review(request):
    if request.method == 'POST':
        review = Review()
        review.text = request.POST['text']
        review.score = request.POST['score']
        review.lecture = Lecture.objects.get(pk=request.POST['lecture']) # id로 객체 가져오기        
        review.user = request.user
        review.save()
        return redirect('/lecture/'+ str(review.lecture.id))
    else :
        return redirect('home')


# payment

def confirm_order(request, lecture_id):
    lecture_confirm = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'confirm_order.html', {'lecture': lecture_confirm})

def payment(request, lecture_id):
    lecture_payment = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'payment.html', {'lecture': lecture_payment})