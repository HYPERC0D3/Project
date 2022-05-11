from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/croprecommendor/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                print(form)
                return redirect('/accounts/login/')
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/croprecommendor/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print('Username OR password is correct')
                return redirect('/croprecommendor/')
            else:
                print('Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/croprecommendor/')


@login_required(login_url='login/')
def home(request):
    context={}
    context['user'] = request.user
    return HttpResponseRedirect('/croprecommendor/')

