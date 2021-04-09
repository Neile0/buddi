import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'buddi_project.settings')

import django

django.setup()
from buddi.models import *


def populate():
    regions = [
        {'name': 'Glasgow', 'sub': None},
        {'name': 'City-Centre', 'sub': 'Glasgow'},
        {'name': 'West-End', 'sub': 'Glasgow'},
        {'name': 'Southside', 'sub': 'Glasgow'},
        {'name': 'Necropolis', 'sub': 'Glasgow'},
        {'name': 'Trongate', 'sub': 'Southside'},
        {'name': 'Maryhill', 'sub': 'West-End'},
        {'name': 'Hillhead', 'sub': 'West-End'},
        {'name': 'Edinburgh', 'sub': None},
        {'name': 'Aberdeen', 'sub': None},
        {'name': 'Dundee', 'sub': None},
        {'name': 'Inverness', 'sub': None},
        {'name': 'Stirling', 'sub': None},
        {'name': 'Dumfries', 'sub': None},
        {'name': 'London', 'sub': None},
        {'name': 'Manchester', 'sub': None},
        {'name': 'Birmingham', 'sub': None},
        {'name': 'Bristol', 'sub': None},
        {'name': 'Liverpool', 'sub': None},
        {'name': 'York', 'sub': None},


    ]

    types = ['Cat', 'Dog', 'Bunny', 'Parrot', 'Fish',]

    animals_1 = [
        {'name': 'Mindy',
         'type': 'cat',
         'bio': 'Very smart but shy at first.',
         'age': 2,
         'sex': 'F',
         'neutered': 'Y',
         'exercise': False,
         'exreq': 0,
         'display': True, },
        {'name': 'Bob',
         'type': 'dog',
         'bio': 'Friendly',
         'age': 5,
         'sex': 'M',
         'neutered': 'N',
         'exercise': True,
         'exreq': 2,
         'display': True, }
    ]

    animals_2 = [
        {'name': 'Hoppy',
         'type': 'bunny',
         'bio': 'Does not do much, easy to care for.',
         'age': 1,
         'sex': 'F',
         'neutered': 'N',
         'exercise': False,
         'exreq': 0,
         'display': False, },
        {'name': 'Fred',
         'type': 'cat',
         'bio': 'Needs to be fed often or will scream',
         'age': 7,
         'sex': 'M',
         'neutered': 'Y',
         'exercise': False,
         'exreq': 0,
         'display': True, },
        {'name': 'Dog',
         'type': 'cat',
         'bio': "Thinks he can bark. He can't.",
         'age': 4,
         'sex': 'M',
         'neutered': 'Y',
         'exercise': False,
         'exreq': 0,
         'display': True},
    ]
    
    animals_3=[
        {'name': 'Polly',
         'type': 'parrot',
         'bio': 'Gets lonely if I leave for longer time periods',
         'age': 1,
         'sex': 'f',
         'neutered': 'N/A',
         'exercise': False,
         'exreq': 0,
         'display': True,}]
    
    animals_4=[
        {'name': 'Poppy',
         'type': 'dog',
         'bio': 'The cutest friend you could have',
         'age': 4,
         'sex': 'M',
         'neutered': 'Y',
         'exercise': True,
         'exreq': 1,
         'display': True,},
        {'name': 'Rex',
         'type': 'fish',
         'bio': "Doesn't say much",
         'age': 1,
         'sex': 'M',
         'neutered': 'N/A',
         'exercise': False,
         'exreq': 0,
         'display': True,},
        {'name': 'Alfred',
         'type': 'fish',
         'bio': 'Golden and very pretty',
         'age': 7,
         'sex': 'F',
         'neutered': 'N/A',
         'exercise': False,
         'exreq': 0,
         'display': True,}
        ]
        
    animals_5=[
       {'name': 'Arthur',
         'type': 'dog',
         'bio': 'Large dog, must be taken on long walks daily',
         'age': 6,
         'sex': 'M',
         'neutered': 'Y',
         'exercise': True,
         'exreq': 4,
         'display': True,},
        {'name': 'Perry',
         'type': 'bunny',
         'bio': 'Small and silent',
         'age': 2,
         'sex': 'F',
         'neutered': 'N',
         'exercise': False,
         'exreq': 0,
         'display': True,}]
    
    animals_6=[
        {'name': 'Annelise',
         'type': 'cat',
         'bio': 'Does not like being alone',
         'age': 3,
         'sex': 'F',
         'neutered': 'Y',
         'exercise': False,
         'exreq': 0,
         'display': True,}]
        
    
    user_profiles = [
        {'bio': 'Owner of two nice pets.',
         'contact_no': '072347',
         'region': 'Glasgow',
         'sitter': False,
         'pets': animals_1},
        {'bio': 'Owner and sitter',
         'contact_no': '07483849',
         'region': 'Edinburgh',
         'sitter': True,
         'pets': animals_2, },
        {'bio': 'I sometimes need help with Polly, happy to help too!',
         'contact_no': '074875674',
         'region': 'Glasgow',
         'sitter': True,
         'pets': animals_3, },
        {'bio': 'I am looking for someone to take care of my pets while I am away with work',
         'contact_no': '0775533',
         'region': 'Edinburgh',
         'sitter': False,
         'pets': animals_4, },
        {'bio': 'Animal enthusiast',
         'contact_no': '098877564',
         'region': 'London',
         'sitter': True,
         'pets': animals_5, },
        {'bio': 'Cat needs a good sitter',
         'contact_no': '09884534',
         'region': 'London',
         'sitter': False,
         'pets': animals_6, },
    ]

    users = [
        {'username': 'janejones',
         'first_name': 'Jane',
         'last_name': 'Jones',
         'email': 'jane@jones.com',
         'password': 'thisisapassword5',
         'profile': user_profiles[0],
         },
        {'username': 'tomhenry',
         'first_name': 'Tom',
         'last_name': 'Henry',
         'email': 'tom@henry.com',
         'password': 'newpass890',
         'profile': user_profiles[1], },
        {'username': 'pamelared',
         'first_name': 'Pamela',
         'last_name': 'Red',
         'email': 'pamela@red.com',
         'password': 'pollyiscute',
         'profile': user_profiles[2], },
        {'username': 'alexbrown',
         'first_name': 'Alex',
         'last_name': 'Brown',
         'email': 'alex@brown.com',
         'password': 'passpass3',
         'profile': user_profiles[3], },
        {'username': 'calebcaleb',
         'first_name': 'Caleb',
         'last_name': 'Caleb',
         'email': 'caelb@caleb.com',
         'password': 'iwillforgetthis32',
         'profile': user_profiles[4], },
        {'username': 'laurengrey',
         'first_name': 'Lauren',
         'last_name': 'Grey',
         'email': 'lauren@grey.com',
         'password': 'yeyleyhey6',
         'profile': user_profiles[5], },
    ]
    
    comments=[
        {'sitter' :'tomhenry',
         'title' : 'Very good sitter',
         'rating': 10,
         'by':'janejones',
         'comment': "Took very good care of both of my pets while I was on holiday. I think they didn't even miss me!"},
        {'sitter' :'tomhenry',
         'title' : 'Pet was happy',
         'rating': 8,
         'by':'pamelared',
         'comment':'Looked after Polly for the weekend and taking care of her is not easy, but he did well.'},
        {'sitter' :'tomhenry',
         'title' : 'Very satisfied',
         'rating': 9,
         'by':'laurengrey',
         'comment':'My cat has never got along with a sitter so well!'},
        {'sitter' :'pamelared',
         'title' : 'Not the best, not the worst',
         'rating': 5,
         'by':'calebcaleb',
         'comment': 'A careful sitter, but not suited for looking after large dogs such as mine'},
        {'sitter' :'pamelared',
         'title' : 'Good',
         'rating': 7,
         'by':'alexbrown',
         'comment':'I am always happy to leave my fish in her care.'},
        {'sitter' :'calebcaleb',
         'title' : 'One of the best!',
         'rating': 9,
         'by':'janejones',
         'comment':'Mindy and Bob would love to see him again!',},
        {'sitter' :'calebcaleb',
         'title' : 'Not great',
         'rating': 4,
         'by':'pamelared',
         'comment':'He does not know how to take care of a parrot...'},
        {'sitter' :'calebcaleb',
         'title' : 'Did a good job',
         'rating': 8,
         'by':'tomhenry',
         'comment':'I can always trust him to take very good care of my pets.'},
        {'sitter' :'calebcaleb',
         'title' : 'Not my favourite',
         'rating':5,
         'by':'alexbrown',
         'comment':'The fish like him, but Poppy seems to disagree.'},
        {'sitter' :'tomhenry',
         'title' : 'Good enough',
         'rating': 6,
         'by':'alexbrown',
         'comment':'Would hire him again, but not my first choice.'
         },
         {'sitter' :'pamelared',
          'title' : 'Really good',
         'rating': 10,
         'by':'tomhenry',
         'comment':'Very good with my pets. Hoppy loves her, Fred and Dog do so too.'},
        ]

    rates = {'tomhenry': 34.5, 'pamelared':45, 'calebcaleb':50}
    
    for rg in regions:
        add_region(rg['name'], rg['sub'])

    for ty in types:
        t = add_type(ty)

    for usr in users:
        u = add_user(usr['username'], usr['first_name'], usr['last_name'],
                     usr['email'], usr['password'])
        pr = usr['profile']
        ur = add_userProfile(u, pr['bio'], pr['contact_no'], add_region(pr['region']), pr['sitter'])
        if (pr['sitter']):
            st = add_sitter(ur, rates[ur.user.username])
            add_sitteropreg(st, ur.region)
        ans = pr['pets']
        for p in ans:
            add_animal(ur, p['name'], add_type(p['type']), p['bio'], p['age'],
                       p['sex'], p['neutered'], p['exercise'], p['display'], p['exreq'])

    for pet in Animal.objects.all():
        add_ad(pet.user, pet, pet.type)
        
    for com in comments:
        user = User.objects.all().get(username=com['sitter'])
        userprofile = UserProfile.objects.all().get(user=user)
        sitter=Sitter.objects.all().get(user=userprofile)
        maker = User.objects.all().get(username=com['by'])
        makerprofile = UserProfile.objects.all().get(user=maker)
        add_comment(sitter, com['title'], com['rating'], makerprofile, com['comment'])
 

def add_region(name, sub=None):
    try:
        p = Region.objects.get(name=sub)
        r = Region.objects.get_or_create(name=name, is_subregion_of=p)[0]
        r.save()
        return r
    except:
        r = Region.objects.get_or_create(name=name)[0]
        r.save()
        return r


def add_type(name):
    t = AnimalType.objects.get_or_create(type=name)[0]
    t.save()
    return t


def add_user(username, first_name, last_name, email, password):
    u = User.objects.get_or_create(username=username, first_name=first_name,
                                   last_name=last_name, email=email)[0]
    u.set_password(password)
    u.save()
    return u


def add_userProfile(user, bio, contact, region, sitter):
    up = UserProfile.objects.get_or_create(user=user, region=region)[0]
    up.bio = bio
    up.profile_url = slugify('buddi' + user.username)
    up.contact_no = contact
    up.is_sitter = sitter
    up.save()
    return up


def add_animal(user, name, type, bio, age, sex, neutered, exercise, display,
               ex):
    a = Animal.objects.get_or_create(user=user, name=name, type=type, age=age,
                                     requires_exercise=exercise,
                                     exercise_requirement=ex, image_dir=slugify(user.profile_url + name))[0]
    a.bio = bio
    a.sex = sex
    a.is_neutered = neutered
    a.is_displayed = display
    a.save()
    return a


def add_sitter(userprofile, rate):
    s = Sitter.objects.get_or_create(user=userprofile, hourly_rate=rate)[0]
    s.save()
    return s


def add_sitteropreg(sitter, region):
    opreg = SitterOperatesInRegion.objects.get_or_create(sitter=sitter, region=region)[0]
    opreg.save()
    return opreg


def add_ad(userprofile, animal, type):
    ad = Ad.objects.get_or_create(user=userprofile, animal=animal, type=type)[0]
    ad.save()
    return ad

def add_comment(sitter, title, rating, made_by, comment):
    c = Comments.objects.get_or_create(sitter=sitter, title=title, rating=rating,
                                       made_by=made_by, comment=comment)[0]
    c.save()
    return c

# Start execution here!

if __name__ == '__main__':
    print('Starting Buddi population script...')
    populate()
