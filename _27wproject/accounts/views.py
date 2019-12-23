from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Profile
from django.shortcuts import render, redirect, reverse, get_object_or_404


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


@method_decorator(login_required, name='dispatch')
class AccountDetailView(DetailView):

    model = Profile
    template_name = 'mypage.html'
    context_object_name = 'mypage'


@login_required
def get_mypage(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = Profile.objects.filter(user=user.id)

    return render(request, 'mypage.html', context={'user': user, 'profile': profile})

@method_decorator(login_required, name='dispatch')
class AccountUpdateView(UpdateView):

    model = User
    template_name = 'update_account.html'
    context_object_name = 'account'
    fields = ('id', 'password', 'username')

    def get_success_url(self):
        return reverse_lazy('mypage', kwargs={'pk': self.object.id})
