from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Community

# Create your views here.

'''
class IndexView(ListView):
    template_name = 'community_board.html'
    context_object_name = 'community_object'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[5:]

'''

def community_board(request):
    community_list = Community.objects
    return render(request, 'community_board.html', {'community_list': community_list})

def community_detail(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    return render(request, 'community_detail.html', {'community_detail':community_detail})


def community_create(request):
    '''
    community = Community()
    community.title = request.GET['title']
    community.text = request.GET['text']

    #나머지 필드들은 추후에 추가할 예정

    community.save()
    return redirect('community/')
    '''
    return render(request, 'community_create.html')