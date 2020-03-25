from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from .models import Community, CommunityComment
from .forms import CommunityFormModel

from django.core.paginator import Paginator
# Create your views here.

def community_board(request):
    community_list = Community.objects.all().order_by('-id')
    #clist = Community.objects.all()
    #paginator = Paginator(clist, 10)
    paginator = Paginator(community_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    #return render(request, 'community_board.html', {'community_list': community_list, 'posts':posts})
    return render(request, 'community_board.html', {'posts':posts})

# category filtering function
def community_board_art(request):
    community_list = Community.objects.all().order_by('-id').filter(category='Art')
    paginator = Paginator(community_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'community_board.html', {'posts': posts})

def community_board_design(request):
    community_list = Community.objects.all().order_by('-id').filter(category='Design')
    paginator = Paginator(community_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'community_board.html', {'posts': posts})

def community_board_social(request):
    community_list = Community.objects.all().order_by('-id').filter(category='Social Media')
    paginator = Paginator(community_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'community_board.html', {'posts': posts})


def community_detail(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    #comments = CommunityComment.objects.filter(community_id)

    context = {
        'community_detail': community_detail,
        #'comments': comments
    }

    return render(request, 'community_detail.html', context)


def community_create(request):
    '''
    community = Community(user=request.user)
    community_list = Community.objects
    
    if request.method == 'POST':
        form = CommunityFormModel(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            #return redirect('/community/')
            return render(request, 'community_board.html', {'community_list': community_list})

    else:
        form = CommunityFormModel()
        return render(request, 'community_create.html', {'form':form})
    '''

    if request.method == 'POST':
        community_form = CommunityFormModel(request.POST, request.FILES)
        if community_form.is_valid():
            community_form.save()
            return redirect('/community/')
    else:
        community_form = CommunityFormModel()
    return render(request, 'community_create.html', {'community_form': community_form})

def community_update(request, community_id):
    community_update = get_object_or_404(Community, pk=community_id)
    if request.method == 'POST':
        community_form = CommunityFormModel(request.POST, request.FILES, instance=community_update)
        if community_form.is_valid():
            community_form.save()
            return redirect('/community/detail/' + str(community_id))
    else:
        community_form = CommunityFormModel(instance=community_update)
    return render(request, 'community_update.html', {'community_form':community_form})

def community_delete(request, community_id):
    community = Community.objects.get(pk=community_id)
    print("delete : ",Community.objects.get)
    community.delete() 
    return redirect('/community/')

'''

<수정 전>

from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Community

# Create your views here.
'''

'''
class IndexView(ListView):
    template_name = 'community_board.html'
    context_object_name = 'community_object'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[5:]

'''

'''
def community_board(request):
    community_list = Community.objects
    return render(request, 'community_board.html', {'community_list': community_list})

def community_detail(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    return render(request, 'community_detail.html', {'community_detail':community_detail})


def community_create(request):
    '''

'''
    community = Community()
    community.title = request.GET['title']
    community.text = request.GET['text']

    #나머지 필드들은 추후에 추가할 예정

    community.save()
    return redirect('community/')
'''

'''
    return render(request, 'community_create.html')
'''