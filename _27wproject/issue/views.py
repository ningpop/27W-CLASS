from django.shortcuts import render

# Create your views here.

def issue_board(request):
    return render(request, 'issue_board.html')

def issue_detail(request, issue_id):
    issue_detail = get_object_or_404(Issue, pk=issue_id)
    return render(request, 'issue_detail.html', {'issue': issue_detail})

def issue_create(request):
    return render(request, 'issue_create.html')