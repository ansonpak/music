from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404

from account.forms import UserForm, UserProfileForm, PhotoUrlForm, ProfileForm
from account.models import UserProfile


def account(request, userID):
    account = get_object_or_404(User, id=userID)
    context = {
        'account': account,
        'userprofile': UserProfile.objects.filter(user=account)
    }
    return render(request, 'account/account.html', context)
    
def register(request):
    template = 'account/register.html'
    if request.method=='GET':
        return render(request, template, {'userForm':UserForm(),'userProfileForm':UserProfileForm()})
    # request.method == 'POST':
    userForm = UserForm(request.POST)
    userProfileForm = UserProfileForm(request.POST)
    if not (userForm.is_valid() and userProfileForm.is_valid()):
        return render(request, template, {'userForm':userForm,'userProfileForm':userProfileForm})
    user = userForm.save()
    user.set_password(user.password)
    user.save()
    userProfile = userProfileForm.save(commit=False)
    userProfile.user = user
    userProfile.save()
    messages.success(request, '歡迎註冊')
    return redirect(reverse('main:main'))


def userLogin(request):
    template = 'account/userLogin.html'
    if request.method=='GET':
        return render(request, template)
    # request.method=='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if not user: # authenticate fail
        return render(request, template, {'error':'登入失敗'})
    if not user.is_active:
        return render(request, template, {'error':'帳號已停用'})
    # login success
    login(request, user)
    messages.success(request, '登入成功')
    return redirect(reverse('main:main'))

@login_required
def userLogout(request):
    logout(request)
    messages.success(request, '歡迎再度光臨')
    return redirect(reverse('main:main'))


def photoUrlUpdate(request, userID):
    userProfile = get_object_or_404(UserProfile, id=userID)
    template = 'account/photoUrlUpdate.html'
    if request.method=='GET':
        form = PhotoUrlForm(instance=userProfile)
        return render(request, template, {'form':form, 'userProfile':userProfile})
    # POST
    form = PhotoUrlForm(request.POST, instance=userProfile)
    if not form.is_valid():
        return render(request, template, {'form':form, 'userProfile':userProfile})
    form.save()
    return redirect('account:account', userID=userID)

def profileUpdate(request, userID):
    userProfile = get_object_or_404(UserProfile, id=userID)
    template = 'account/profileUpdate.html'
    if request.method=='GET':
        form = ProfileForm(instance=userProfile)
        return render(request, template, {'form':form, 'userProfile':userProfile})
    # POST
    form = ProfileForm(request.POST, instance=userProfile)
    if not form.is_valid():
        return render(request, template, {'form':form, 'userProfile':userProfile})
    form.save()
    return redirect('account:account', userID=userID)