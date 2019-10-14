from django.shortcuts import render

# Create your views here.

def contact_board(request):
    return render(request, 'contact_board.html')