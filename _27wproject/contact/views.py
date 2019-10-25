from django.shortcuts import render
from .models import Contact

# Create your views here.

'''
def contact_board(request):
    return render(request, 'contact_board.html')
'''

def contact_board(request):
    contact_list = Contact.objects
    return render(request, 'contact_board.html', {'contact_list': contact_list})

def contact_create(request):
    return render(request, 'contact_create.html')

def contact_detail(request):
    return render(request, 'contact_detail.html')