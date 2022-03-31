import json

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from utils.utils import github_oauth
# Create your views here.

def is_password_safe(p: str):
    """
    test password, wip.
    """
    length_safe = len(p) >= 8
    return length_safe

def github_login(request):
    return redirect(github_oauth.oauth_url()[0])

def github_callback(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    if not code:
        return redirect(reverse('home'))
    token = github_oauth.access_token(code, state)
    user_info = github_oauth.user_info(token)
    user_info = json.loads(user_info)
    gh_id = user_info.get('id')
    username = f'github_{gh_id}'
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.create_user(username=username)
        user.set_unusable_password()
        user.save()
    login(request, user)
    return redirect(reverse('home'))

def accounts_login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    if request.method == 'POST':
        redir_to = request.GET.get('next', '/')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redir_to)
        else:
            return redirect(reverse('login'))

def accounts_signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if is_password_safe(password) is False:
            return render(request, 'accounts/signup.html', {
                'info': 'password too simple! we need at least 8 characters!'
            })
        if not password.strip() or not username.strip():
            return render(request, 'accounts/signup.html', {'info': 'bad info'})
        user_exists = User.objects.filter(username=username).first() is not None
        if user_exists:
            return render(request, 'accounts/signup.html', {'info': 'user exists'})
        user = User.objects.create_user(username=username,
                                        password=password)
        login(request, user)
        return redirect(reverse('home'))


@login_required
def accounts_logout(request):
    logout(request)
    return redirect(reverse('home'))