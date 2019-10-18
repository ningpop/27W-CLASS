from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['id'], password=request.POST['password1'], email=request.POST['email'])
        user.profile.phoneNumber = request.POST['phoneNumber']
        auth.login(request, user)
        return redirect('index')
    return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'index.html',{'confirm' : user.username+"님 환영합니다"})
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout (request):
    auth.logout(request)
    return redirect('index')



