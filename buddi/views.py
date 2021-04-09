from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserForm, UserProfileForm, AnimalForm, OpregForm, SearchForm
from .models import *

def get_parent_regions():
    regions = Region.objects.filter(is_parent_region=True)
    return [r for r in regions]

# Create your views here.
def index(request):
    context_dict = {'regions': get_parent_regions()}
    return render(request, 'buddi/index.html', context=context_dict)


def search_test(request, case, place):
    # case should denote whether
    # this is a looking for a sitter/looking for a pet to sit situation
    # place should be a region/region name, the differences can be easily fixed
    ad_list = []
    sitter_list = []
    context_dict = {'regions': get_parent_regions()}
    context_dict['case'] = case
    region = Region.objects.get(name=place)
    print(region)

    if case == 'sitter':
        sitter_ids = SitterOperatesInRegion.objects.all().filter(region=region).values('sitter_id')
        sitter_id_list = [s['sitter_id'] for s in sitter_ids]
        sitter_list = Sitter.objects.filter(id__in=sitter_id_list)
        print(sitter_list)

    if case == 'sit':
        owners = UserProfile.objects.filter(region=region)
        ad_list = Ad.objects.filter(user__in=owners)

    context_dict['ads'] = ad_list
    context_dict['sitters'] = sitter_list

    return render(request, 'buddi/search.html', context=context_dict)


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
    user_target = User.objects.all().get(username=username)
    user_profile = UserProfile.objects.all().get(user=user_target)
    animals = Animal.objects.all().filter(user=user_profile)

    context_dict['user_target'] = user_target
    context_dict['user_profile'] = user_profile
    context_dict['pets'] = animals

    return render(request, 'buddi/user_profile.html', context=context_dict)


def sitter_profile(request, username):
    context_dict = {'regions': get_parent_regions()}
    user = User.objects.all().get(username=username)
    userprofile = UserProfile.objects.all().get(user=user)
    sitter = Sitter.objects.all().get(user=userprofile)
    sitterop = SitterOperatesInRegion.objects.all().filter(sitter=sitter)

    context_dict['current_user'] = user
    context_dict['userprofile'] = userprofile
    context_dict['sitter_reg'] = sitterop

    return render(request, 'buddi/sitter.html', context=context_dict)


@login_required
def delete_animal(request, animal_id):
    animal = Animal.objects.all().get(id=animal_id)
    user = animal.user.user.username
    animal.delete()
    return redirect(reverse('buddi:user',
                            kwargs={'username': user}))


@login_required
def delete_opregion(request, sitteropreg_id):
    opreg = SitterOperatesInRegion.objects.all().get(id=sitteropreg_id)
    user = opreg.sitter.user.user.username
    opreg.delete()
    return redirect(reverse('buddi:sitter',
                            kwargs={'username': user}))


@login_required
def add_pet(request, username):
    context_dict = {'regions': get_parent_regions()}
    user = User.objects.all().get(username=username)
    userprofile = UserProfile.objects.all().get(user=user)
    form = AnimalForm()
    if request.method == 'POST':
        form = AnimalForm(request.POST)

        if form.is_valid():
            animal = form.save(commit=False)
            animal.user = userprofile
            animal.image_dir = slugify(userprofile.profile_url + animal.name)
            animal.save()

            return redirect(reverse('buddi:user',
                                    kwargs={'username': user}))
        else:
            print(form.errors)
    context_dict['form'] = form
    context_dict['current_user'] = user
    return render(request, 'buddi/add_pet.html', context=context_dict)


@login_required
def add_opreg(request, username):
    user = User.objects.all().get(username=username)
    userprofile = UserProfile.objects.all().get(user=user)
    sitter = Sitter.objects.all().get(user=userprofile)
    form = OpregForm()

    if request.method == 'POST':
        form = OpregForm(request.POST)

        if form.is_valid():
            opreg = form.save(commit=False)
            opreg.sitter = sitter
            opreg.save()

            return redirect(reverse('buddi:sitter',
                                    kwargs={'username': user}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'current_user': user}
    return render(request, 'buddi/add_opreg.html', context=context_dict)


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
                  context={'regions': get_parent_regions(), 'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def sitter(request, username):
    context_dict = {'regions': get_parent_regions()}

    user_target = User.objects.all().get(username=username)
    user_profile = UserProfile.objects.all().get(user=user_target)
    animals = Animal.objects.all().filter(user=user_profile)

    context_dict['user_target'] = user_target
    context_dict['user_profile'] = user_profile
    context_dict['pets'] = animals

    sitter = Sitter.objects.get(user=user_profile)

    try:
        comments = Comments.objects.get(sitter=sitter)
    except:
        comments = []
    try:
        sitter_regions = SitterOperatesInRegion.objects.all().get(sitter=sitter)
    except:
        sitter_regions = []

    context_dict['sitter'] = sitter
    context_dict['sitter_regions'] = sitter_regions
    context_dict['sitter_comments'] = comments

    if comments:
        rating = sum([c.rating for c in comments])
    else:
        rating = 0
    context_dict['sitter_rating'] = rating

    return render(request, 'buddi/sitter_profile.html', context=context_dict)


def find_sitter(request):
    return HttpResponse("Replace view with sitter()")


def sit(request, param):
    sitter_list = []
    context_dict = {'regions': get_parent_regions()}

    region = Region.objects.get(name__iexact=param)
    print(region)

    owners = UserProfile.objects.filter(region=region)
    ad_list = Ad.objects.filter(user__in=owners)
    images = []
    for ad in ad_list:
        image = AnimalImages.objects.all().get(animal=ad.animal)[0]
        images.append(image)

    context_dict['ads'] = ad_list
    context_dict['ad_image'] = images
    context_dict['sitters'] = sitter_list
    context_dict['region'] = region
    context_dict['type'] = "sit"

    return render(request, 'buddi/search.html', context=context_dict)


def sitters(request, param):
    print(param)
    ad_list = []
    ad_image = []
    context_dict = {'regions': get_parent_regions()}
    region = Region.objects.get(name__iexact=param)
    print(region)
    sitter_ids = SitterOperatesInRegion.objects.all().filter(region=region).values('sitter_id')
    sitter_id_list = [s['sitter_id'] for s in sitter_ids]
    sitter_list = Sitter.objects.filter(id__in=sitter_id_list)

    context_dict['ads'] = ad_list
    context_dict['sitters'] = sitter_list
    context_dict['region'] = region
    context_dict['type'] = "sitters"
    return render(request, 'buddi/search.html', context=context_dict)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['type'] == "sit":
                return redirect('/sit/{0}'.format(form.cleaned_data['region'].lower()))
            elif form.cleaned_data['type'] == "sitter":
                return redirect('/sitters/{0}'.format(form.cleaned_data['region'].lower()))
        else:
            return HttpResponse("form invalid")
    else:
        return HttpResponse("not working")


def change_user_image(request, username):
    return HttpResponse("Changing")

def login_ajax(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        response_data = {}
        if login_form.is_valid():
            response_data['result'] = 'Success!'
            response_data['message'] = 'You"re logged in'
        else:
            response_data['result'] = 'failed'
            response_data['message'] = 'You messed up'

        return HttpResponse(json.dumps(response_data), content_type="application/json")