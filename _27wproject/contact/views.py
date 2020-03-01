from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact, Answer
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import ContactForm

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
    if request.method == 'POST':
        username = Contact.objects.create(user=request.user)
        contact_form = ContactForm(request.POST, instance=username)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('/contact/')
    else:
        contact_form = ContactForm()
    return render(request, 'contact_create.html', {'contact_form': contact_form})

def contact_detail(request, contact_id):
    contact_detail = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contact_detail.html', {'contact': contact_detail})

def contact_update(request, contact_id):
    contact_update = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, instance=contact_update)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('/contact/' + str(contact_id))
    else:
        contact_form = ContactForm(instance=contact_update)
    return render(request, 'contact_create.html', {'contact_form':contact_form})

def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect('/contact/')

def submit(request):
    contact = Contact()
    contact.title = request.POST['title']
    contact.text = request.POST['content']
    contact.user = request.user
    contact.created_at = timezone.datetime.now()
    contact.save()
    return redirect('/contact/' + str(contact.id))

def answer(request):
    if request.method == 'POST':
        answer = Answer()
        answer.text = request.POST['text']
        answer.contact = Contact.objects.get(pk=request.POST['contact']) # id로 객체 가져오기        
        answer.admin = request.user
        answer.save()
        return redirect('/contact/'+ str(answer.contact.id))
    else :
        return redirect('home')

def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('/contact/')