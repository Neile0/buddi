from django.apps import apps
from django.test import TestCase
from blog.apps import BlogConfig
from buddi.apps import BuddiConfig
from blog.models import *
from .views import *



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



    def check_animal_data(self,pk,name, type, bio, age, sex, neutered, exercise, exreq, display ):
        self.assertEqual(Animal.objects.get(pk=pk).name, name)
        self.assertEqual(Animal.objects.get(pk=pk).type, type)
        self.assertEqual(Animal.objects.get(pk=pk).bio, bio)
        self.assertEqual(Animal.objects.get(pk=pk).age, age)
        self.assertEqual(Animal.objects.get(pk=pk).sex, sex)
        self.assertEqual(Animal.objects.get(pk=pk).neutered, neutered)
        self.assertEqual(Animal.objects.get(pk=pk).exercise, exercise)
        self.assertEqual(Animal.objects.get(pk=pk).exreq, exreq)
        self.assertEqual(Animal.objects.get(pk=pk).display, display)

    def test_animal(self):

        self.check_animal_data(1,'Mindy', 'cat', 'Very smart but shy at first.', 2,'F','Y',
                               False, 0,True)
        self.check_animal_data(2, 'Bob', 'dog', 'Friendly', 5, 'M', 'N',
                               True, 2, True)
        self.check_animal_data(3, 'Hoppy', 'bunny', 'Does not do much, easy to care for.',
                               1, 'F', 'N',
                               False, 0, False)
        self.check_animal_data(4, 'Fred', 'cat', 'Needs to be fed often or will scream',
                               7, 'M', 'Y',
                               False, 0, True)
        self.check_animal_data(5, 'Dog', 'cat', "Thinks he can bark. He can't.",
                               4, 'M', 'Y',
                               False, 0, True)



class populateBlog_test(TestCase):
    def setUp(self):
        import populate_blog
        populate_blog.populate()

    def check_topic(self, listNews, listVet, listShop):
        for x in range(6):
            self.assertEqual(news.objects.get(pk=x).topic, listNews[x])
            self.assertEqual(shop.objects.get(pk=x).topic, listShop[x])
            self.assertEqual(vet.objects.get(pk=x).topic, listVet[x])

        
    def test_topic(self):
        News_topic_list = []
        for x in range(1, 6):
            News_topic_list.append("Topic_" + str(x))

        Vets_topic_list = []
        for x in range(1, 6):
            Vets_topic_list.append("Topic_" + str(x))

        Shops_topic_list = []
        for x in range(1, 6):
            Shops_topic_list.append("Topic_" + str(x))

        self.check_topic(News_topic_list,Vets_topic_list, Shops_topic_list)


    def check_conntend(self, listNew, listVet, listShop):
        for x in range(6):
            self.assertEqual(news.objects.get(news.objects.get(pk=x).contend, open(listNew[x])))
            self.assertEqual(news.objects.get(vet.objects.get(pk=x).contend, open(listVet[x])))
            self.assertEqual(news.objects.get(shop.objects.get(pk=x).contend, open(listShop[x])))


    def test_contend(self):
        News_contend_list = []
        for x in range(1, 6):
            News_contend_list.append("populate_blog/News_text" + str(x) + ".txt")

        Vet_contend_list = []
        for x in range(1, 6):
            Vet_contend_list.append("populate_blog/vet_text" + str(x) + ".txt")

        Shop_contend_list = []
        for x in range(1, 6):
            Shop_contend_list.append("populate_blog/shop_text" + str(x) + ".txt")

        self.check_conntend(News_contend_list, Vet_contend_list, Shop_contend_list)


class testIndexView(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('buddi:index'))

    def test_index_use_template(self):
        self.assertTemplateUsed(self.response, 'buddi/index.html',
                               f"Your index() view does not use the expected index.html template.")

    def test_index_uses_context_dictionary(self):

        self.assertTrue('regions' in self.response.context_dict,
                        f"You didn't pass any information in this page")

        message = self.response.context['regions']
        expected = get_parent_regions()
        self.assertEqual(message, expected,
                         f"You did't parse correct information")


class testUserProfileView(TestCase):
    def setUp(self):

        self.response = self.client.get(reverse('buddi:user_profile'))

    def test_UserProfile_use_template(self):
        self.assertTemplateUsed(self.response, 'buddi/user_profile.html',
                               f"Your user_profile() view does not use the expected user_profile.html template.")





class testSitter(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('buddi:sitter'))

    def test_Sitter_use_template(self):
        self.assertTemplateUsed(self.response, 'buddi/sitter_profile.html',
                               f"Your user_profile() view does not use the expected sitter_profile.html template.")



class testSitterProfile(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('buddi:sitter_profile'))

    def test_Sitter_Profile_use_template(self):
        self.assertTemplateUsed(self.response, 'buddi/sitter.html',
                               f"Your user_profile() view does not use the expected sitter.html template.")


class testSit(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('buddi:sit'))

    def test_sit_use_template(self):
        self.assertTemplateUsed(self.response, 'buddi/search.html',
                               f"Your user_profile() view does not use the expected search.html template.")

















