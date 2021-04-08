from django.test import TestCase, RequestFactory
from blog.apps import BlogConfig
from django.apps import apps
from .models import *
from buddi.apps import BuddiConfig
from .views import user_profile
import populate_buddi


# Create your tests here.

class blogReportConfigTest(TestCase):

    def test_app(self):
        self.assertEqual(BlogConfig.name, 'blog')
        self.assertEqual(apps.get_app_config('blog').name, 'blog')

class buddiReportConfigTest(TestCase):

    def test_app(self):
        self.assertEqual(BuddiConfig.name, 'buddi')
        self.assertEqual(apps.get_app_config('buddi').name, 'buddi')



class pop_buddi_script_test(TestCase):
    regions = [
        {'name': 'Glasgow', 'sub': None},
        {'name': 'Edinburgh', 'sub': None},
        {'name': 'London', 'sub': None},
        {'name': 'West End', 'sub': 'Glasgow'}
    ]

    types = ['Cat', 'Dog', 'Bunny', 'Parrot']

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





    def setUp(self):
        import populate_buddi
        populate_buddi.populate()

    def test_user(self):
        users = [
            {'username': 'janejones',
             'first_name': 'Jane',
             'last_name': 'Jones',
             'email': 'jane@jones.com',
             'password': 'thisisapassword5',

             },
            {'username': 'tomhenry',
             'first_name': 'Tom',
             'last_name': 'Henry',
             'email': 'tom@henry.com',
             'password': 'newpass890',
              }
        ]
        for x in range(1,3):
            self.assertEqual(User.objects.get(pk=x).username, users[x-1].get('username'))
            self.assertEqual(User.objects.get(pk=x).email, users[x-1].get('email'))
            self.assertEqual(User.objects.get(pk=x).last_name, users[x-1].get('last_name'))
            self.assertEqual(User.objects.get(pk=x).first_name, users[x - 1].get('first_name'))


    def test_usPro(self):
        user_profiles = [
            {'bio': 'Owner of two nice pets.',
             'contact_no': '072347',
             'region': 'Glasgow',
             'sitter': False,
             },
            {'bio': 'Owner and sitter',
             'contact_no': '07483849',
             'region': 'Edinburgh',
             'sitter': True,
              },
        ]
        for x in range(len(user_profiles)):
            self.assertEqual(UserProfile.objects.get(pk = x).bio, user_profiles[x].get('bio'))
            self.assertEqual(UserProfile.objects.get(pk =x).contact_no, user_profiles[x].get('contact_no'))
            self.assertEqual(UserProfile.objects.get(pk=x).region, user_profiles[x].get('region'))
            self.assertEqual(UserProfile.objects.get(pk=x).sitter, user_profiles[x].get('sitter'))

