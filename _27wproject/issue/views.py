from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import transaction
# specific to this view
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# specific to this view
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from .models import Issue, IssueComment
from .forms import IssueForm
from django.views.generic.edit import FormView

@login_required(login_url="/accounts/login")
@transaction.atomic
def update_issue(request):
    if request.method == 'POST':
        issue_form = IssueForm(request.POST, instance=request.user)
        
        if issue_form.is_valid():
            issue_form.save()
            
            messages.success(request, ('issue was successfully updated!'))
            return redirect('myprofile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'filter/updateprofile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class IssueListView(ListView):

    model = Issue
    template_name = 'issue_board.html'
    context_object_name = 'issues'
    paginate_by = 12

    # Overriding for pagination
    def get_context_data(self, **kwargs):
        context = super(IssueListView, self).get_context_data(**kwargs)
        issues = self.get_queryset()
        paginator = Paginator(issues, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            issues = paginator.page(page)
        except PageNotAnInteger:
            issues = paginator.page(1)
        except EmptyPage:
            issues = paginaotor.page(paginator.num_pages)

        context["issues"] = issues
        return context


def issue_board_art(request):
    issue_list = Issue.objects.all().order_by('-id').filter(category='Art')
    paginator = Paginator(issue_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'issue_board.html', {'issues': posts})


def issue_board_design(request):
    issue_list = Issue.objects.all().order_by('-id').filter(category='Design')
    paginator = Paginator(issue_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'issue_board.html', {'issues': posts})


def issue_board_social(request):
    issue_list = Issue.objects.all().order_by('-id').filter(category='Social')
    paginator = Paginator(issue_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'issue_board.html', {'issues': posts})


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

@method_decorator(login_required(login_url="/accounts/login"), name='dispatch')
class IssueCreateView(CreateView):
    model = Issue
    template_name = 'issue_create.html'
    fields = ('title', 'text', 'image', 'category')
    success_url = reverse_lazy('issue_board')


def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    comments = IssueComment.objects.filter(issue=issue.id)

    return render(request, 'issue_detail.html', context={'issue': issue, 'comments':comments})


@method_decorator(login_required(login_url="/accounts/login"), name='dispatch')
class IssueUpdateView(UpdateView):

    model = Issue
    form_calss = IssueForm
    template_name = 'issue_update.html'
    context_object_name = 'issue'
    fields = ('title', 'text', 'image')


    def get_success_url(self):
        return reverse_lazy('issue_detail', kwargs={'pk': self.object.id})


@method_decorator(login_required(login_url="/accounts/login"), name='dispatch')
class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue_delete.html'
    success_url = reverse_lazy('issue_board')



@login_required(login_url="/accounts/login")
def comment_write(request):
    errors = []
    if request.method == 'POST':
        issue_id = request.POST.get('issue_id', '').strip()
        print(issue_id)
        text = request.POST.get('content', '').strip()

        if not text:
            errors.append('댓글을 입력해주세요.')

        if not errors:
            comment = IssueComment.objects.create(
                user=request.user, issue_id=issue_id, text=text)

            print(comment.issue.id)
            return redirect(reverse('issue_detail', kwargs={'pk': comment.issue.id}))

    return render(request, 'issue_detail.html', {'user': request.user, 'errors': errors})


"""
@login_required
def comment_write(request):
    errors = []
    if request.method == 'POST':
        post_id = request.POST.get('post_id', '').strip()
        content = request.POST.get('content', '').strip()

        if not content:
            errors.append('댓글을 입력해주세요.')

        if not errors:
            comment = Comment.objects.create(
                user=request.user, post_id=post_id, content=content)

            return redirect(reverse('blogs:post_detail', kwargs={'post_id': comment.post.id}))

    return render(request, 'post_detail.html', {'user': request.user, 'errors': errors})
"""