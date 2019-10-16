from django.shortcuts import render
#
from django.views.generic import ListView
#from .models import Question

# Create your views here.

'''
class IndexView(ListView):
    template_name = 'community_board.html'
    context_object_name = 'community_object'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[5:]

'''

def community_board(request):
    return render(request, 'community_board.html')

def create(request):
    return render(request, 'create.html')

def community_detail(request):
    return render(request, 'community_detail.html')  