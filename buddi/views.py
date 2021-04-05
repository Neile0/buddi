from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm
from datetime import datetime
from .models import Sitter, SitterOperatesInRegion, Comments, Ad
from .filters import AdFilter



# Create your views here.
def index(request):
    #return HttpResponse("What are you looking for today?")
    return render(request, 'buddi/index.html')

def search(request):
    ads = AdFilter(request.GET, queryset = Ad.objects.all())
    return render(request, 'buddi/search.html', {'filter':ads})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('buddi:index'))
            else:
                return HttpResponse("Your Buddi account is not active.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login.")
    else:
        return render(request, 'buddi/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('buddi:index'))


def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            if 'picture' in request.FILES:
                profile_picture = request.FILES['picture']
            profile.save()
            
            registered = True
            
        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request,
                  'buddi/register.html', #might need to change this to sign up?
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})


def find_sitter(request):
    contextBox = {'sitterM' : Sitter.objects.all(),
                  'sitterR' : SitterOperatesInRegion.objects.all(),
                  'comment' : Comments.objects.all(),

                  }

    return render(request, 'buddi/sitter_profile.html', contextBox)

