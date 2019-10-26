from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

'''
def contact_board(request):
    return render(request, 'contact_board.html')
'''

def contact_board(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'contact_board.html', {'posts': posts})

def contact_create(request):
    return render(request, 'contact_create.html')

def contact_detail(request, contact_id):
    contact_detail = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contact_detail.html', {'contact': contact_detail})

def submit(request):
    contact = Contact()
    contact.title = request.POST['title']
    contact.text = request.POST['content']
    contact.user = request.user
    contact.created_at = timezone.datetime.now()
    contact.save()
    return redirect('/contact/' + str(contact.id))

def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect('/contact/')