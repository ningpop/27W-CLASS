from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator
from .decorators import admin_required
from .models import Issue, IssueComment
from .forms import IssueForm

from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator


def issues(request):
    issues = Issue.objects.order_by('-created_at')
    issue_list = Issue.objects.all()
    paginator = Paginator(issue_list, 10)
    page = request.GET.get('page')
    page_issues = paginator.get_page(page)

    return render(request, 'issue_board.html', context={'issues': issues, 'page_issues': page_issues})


def issue_detail(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    comments = IssueComment.objects.filter(issue=issue.id)


    return render(request, 'issue_detail.html',
                  context={'issue': issue, 'comments': comments})


@login_required  # login_requierd source code - https://docs.djangoproject.com/en/2.2/_modules/django/contrib/auth/decorators/#login_required
def write_issue(request):
    errors = []
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        image = request.FILES.get('image')

        if not title:
            errors.append('제목을 입력해주세요.')

        if not content:
            errors.append('내용을 입력해주세요.')

        if not errors:
            issue = Issue.objects.create(
                user_id=request.user, title=title, text=content, image=image)

            # path('post/<int:article_id>/<int:post_id>/', views.post_detail, name='post_detail')
            # /post/%d/ % post.id == reverse('post_detail' , args=[post.id, article.id]) -> args로 할 경우 순서대로 url 로직 순서대로 들억야 함.
            return redirect(reverse('issue:issue_detail', kwargs={'issue_id': issue.id}))

    return render(request, 'issue_create.html', {'user': request.user, 'errors': errors})



def update_issue(request, issue_id):
    issue_id = int(issue_id)

    try:
        now_issue = Issue.objects.get(id=issue_id)
    except Issue.DoesNotExist:
        return redirect('issue')

    if request.method == "POST":
        issue = Issue.objects.get(pk=issue_id)
        issue.title = request.POST.get('title')
        issue.text = request.POST.get("content")
        issue.image = request.POST.get("image")
        issue.save()
        return redirect(reverse(f"/{issue_id}/", kwargs={"issue_id": issue.id}))

    return render(request, "issue_update.html")



def delete_issue(request, issue_id):
    issue = int(issue_id)
    try:
        issue = Issue.objects.get(id = issue_id)
    except Issue.DoesNotExist:
        return redirect('issue')
    issue.delete()
    return redirect('issue')

@login_required
def write_comment(request):
    errors = []
    if request.method == 'POST':
        issue_id = request.POST.get('post_id', '').strip()
        content = request.POST.get('content', '').strip()

        if not content:
            errors.append('댓글을 입력해주세요.')

        if not errors:
            comment = IssueComment.objects.create(
                user=request.user, issue_id=issue_id, text=content)

            return redirect(reverse('issue:issue_detail', kwargs={'post_id': comment.issue.id}))

    return render(request, 'issue_detail.html', {'user': request.user, 'errors': errors})


"""
class IssueList(ListView):
    model = Issue
    template_name = 'issue_board.html'
    context_object_name = 'issue_list'


class IssueDetail(DetailView):
    template_name = 'issue_detail.html'
    queryset = Issue.objects.all()
    context_object_name = 'issue'


@method_decorator(admin_required, name='dispatch')
class IssueCreate(FormView):
    template_name = 'issue_create.html'
    form_class = IssueForm
    success_url = ''

    def form_invalid(self, form):
        issue = Issue(
            title=form.data.get('title'),
            text=form.data.get('text'),
            image=form.data.get('image'),
            category=form.data.get('category'),
            created_at=form.data.get('created_at')
        )
        issue.save()
        return super().form_valid(form)

"""