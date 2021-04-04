
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','buddi_project.settings')

import django
django.setup()
from buddi.models import *

def populate():
    
    regions = [
        {'name': 'Glasgow' },
        {'name': 'Edinburgh'},
        {'name': 'London'},
        ]
    animals_1= [
        {'name': 'Mindy',
         'type': 'cat',
         'bio': 'Very smart but shy at first.',
         'age': 2,
         'sex': 'F',
         'neuterd': 'Y',
         'exercise': False,
         'display': True,},
        {'name': 'Bob',
         'type': 'dog',
         'bio': 'Friendly',
         'age': 5,
         'sex': 'M',
         'neuterd': 'N',
         'exercise': True,
         'exreqmin':2,
         'exreqmax':4,
         'display': True,},
        ]
    
    animals_2 = [
        {'name': 'Hoppy',
         'type': 'bunny',
         'bio': 'Does not do much, easy to care for.',
         'age': 1,
         'sex': 'F',
         'neuterd': 'N',
         'exercise': False,
         'display': False,},
        {'name': 'Fred',
         'type': 'cat',
         'bio': 'Needs to be fed often or will scream',
         'age': 7,
         'sex': 'M',
         'neuterd': 'Y',
         'exercise': False,
         'display': True,},
        {'name': 'Dog',
         'type': 'cat',
         'bio' : "Thinks he can bark. He can't.",
         'age': 4,
         'sex': 'M',
         'nuetered': 'Y',
         'exercise': False,
         'display': True},
        ]
    
    user_profiles =[
        {'bio' : 'Owner of two nice pets.',
        'contact_no': '072347',
        'region':'Glasgow',
        'sitter': False,},
        {'bio' : 'Owner and sitter',
        'contact_no': '07483849',
        'region':'Edinburgh',
        'sitter': True,},
        ]
    
    users = [
        {'username': 'janejones',
         'first_name': 'Jane',
         'last_name': 'Jones',
         'email': 'jane@jones.com',
         'password':'thisisapassword5',
         'profile': user_profiles[0],
         'pets': animals_1,
         },
        {'username': 'tomhenry',
         'first_name': 'Tom',
         'last_name': 'Henry',
         'email': 'tom@henry.com',
         'password': 'newpass890',
         'profile': user_profiles[1],
         'pets': animals_2,},
        ]
    
    

    for usr in users:
        u = add_user(usr['username'], usr['first_name'], usr['last_name'], 
                     usr['email'], usr['password'])
        pr = usr['profile']
        add_userProfile(u, pr['bio'], pr['contact_no'], pr['region'], pr['sitter'])
        ans = usr['pets']
        for p in ans:
            add_animal(u, p['name'], p['type'], p['bio'], p['age'],
                       p['sex'], p['neutered'], p['exercise'], p['display'])
    

def add_user(username, first_name, last_name, email, password):
    u=User.objects.get_or_create(username=username, first_name=first_name, 
                                 last_name=last_name, email=email)[0]
    u.set_password(password)
    u.save()
    return u

def add_userProfile(user, bio, contact, region, sitter):
    up = UserProfile.objects.get_or_create(user=user)[0]
    up.bio = bio
    up.contact_no = contact
    up.region = region
    up.is_sitter = sitter
    up.save()
    return up

def add_animal(user, name, type, bio, age, sex, neutered, exercise, display,
               exmin=0, exmax=0):
    a = Animal.objects.get_or_create(user=user, name=name)[0]
    a.type = type
    a.bio = bio
    a.age = age
    a.sex = sex
    a.is_neutered = neutered
    a.requires_exercise = exercise
    if(exercise):
        a.exercise_requirement = IntegerRangeField(exmin, exmax)
    a.display = display
    a.save()
    return a
    

# Start execution here!
    
if __name__ == '__main__':
    print('Starting Buddi population script...')
    populate()
    
    
    
