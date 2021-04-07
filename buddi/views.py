from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserForm, UserProfileForm
from .models import *


def get_parent_regions():
    regions = Region.objects.filter(is_parent_region=True)
    return [r for r in regions]


# Create your views here.
def index(request):
    context_dict = {'regions': get_parent_regions()}
    print(context_dict)
    return render(request, 'buddi/index.html', context=context_dict)


def search(request, case, place):
    # case should denote whether
    # this is a looking for a sitter/looking for a pet to sit situation
    # place should be a region/region name, the differences can be easily fixed
    ad_list = []
    sitter_list = []
    context_dict = {'regions': get_parent_regions()}
    if request.method == 'POST':

        context_dict['cases'] = case

        if case == 'sitter':
            for s in Sitter.objects.all():
                if s.region.name == place:
                    sitter_list.append(s)

        if case == 'sit':
            for ad in Ad.objects.all():
                if ad.user.region.name == place:
                    ad_list.append(ad)

    context_dict['ads'] = ad_list
    context_dict['sitters'] = sitter_list

    return render(request, 'buddi/search.html', context_dict)


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


def user_profile(request, username):
    context_dict = {'regions': get_parent_regions()}
    user = User.objects.all().get(username=username)
    userprofile = UserProfile.objects.all().get(user=user)
    animals = Animal.objects.all().filter(user=userprofile)

    context_dict['current_user'] = user
    context_dict['userprofile'] = userprofile
    context_dict['pets'] = animals
    print(context_dict)
    return render(request, 'buddi/user_profile.html', context_dict)

def sitter_profile(request, username):
    
    context_dict = {'regions': get_parent_regions()}
    user = User.objects.all().get(username=username)
    userprofile = UserProfile.objects.all().get(user=user)
    sitter = Sitter.objects.all().get(user=userprofile)
    sitterop = SitterOperatesInRegion.objects.all().filter(sitter=sitter)
    
    context_dict['current_user'] = user
    context_dict['userprofile'] = userprofile
    context_dict['sitter_reg'] = sitterop
    
    return render(request, 'buddi/sitter.html', context_dict)
    


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
            profile = profile_form.save(commit=False)
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
                  'buddi/register.html',  # might need to change this to sign up?
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def find_sitter(request):
    context_dict = {'regions': get_parent_regions(),
                    'sitterM': Sitter.objects.all(),
                    'sitterR': SitterOperatesInRegion.objects.all(),
                    'comment': Comments.objects.all(),

                    }

    return render(request, 'buddi/sitter_profile.html', context=context_dict)
