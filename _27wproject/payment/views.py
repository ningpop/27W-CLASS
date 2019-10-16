from django.shortcuts import render

# Create your views here.

def confirm_order(request):
    return render(request, 'confirm_order.html')

def payment(request):
    return render(request, 'payment.html')