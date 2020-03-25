from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Community, CommunityComment
from .forms import CommunityFormModel

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
# Create your views here.

def community_board(request):
    community_list = Community.objects.all().order_by('-id')
    paginator = Paginator(community_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
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
    community = get_object_or_404(Community, pk=community_id)
    comments = CommunityComment.objects.filter(community=community.id)

    context = {
        'community_detail': community,
        'comments' : comments,
    }

    return render(request, 'community_detail.html', context)


def community_create(request):
    if request.method == 'POST':
        username = Community.objects.create(user=request.user)
        community_form = CommunityFormModel(request.POST, request.FILES, instance=username)
        
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


@login_required(login_url="/accounts/login")
#def comment_write(request):
def community_comment(request):
    errors = []
    if request.method == 'POST':
        community_id = request.POST.get('community_id', '').strip()
        print("!!!!!!!!!" + request.POST.get('community_id'))
        text = request.POST.get('content', '').strip()

        if not text:
            errors.append('댓글을 입력해주세요.')

        if not errors:
            comment = CommunityComment.objects.create(
                user=request.user, community_id=community_id, text=text)

            print(comment.community.id)
            return redirect(reverse('community_detail', kwargs={'community_id': comment.community.id}))

    return render(request, 'community_detail.html', {'user': request.user, 'errors': errors})
