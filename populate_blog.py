import os
from django.core.files import File
from django.core.files.images import ImageFile
from PIL import Image
os.environ.setdefault('DJANGO_SETTINGS_MODULE','buddi_project.settings')

import django
django.setup()
from blog.models import *

def populate():
    News_topic_list = []
    for x in range(1,6):
        News_topic_list.append("Topic_"+str(x))

    News_contend_list = []
    for x in range(1, 6):
        News_contend_list.append("populate_blog/News_text"+str(x)+".txt")

    News_Pic_list = []
    for x in range(1, 6):
        News_Pic_list.append("populate_blog/News_Pic_" + str(x) + ".jpg")



    Vets_topic_list = []
    for x in range(1, 6):
        Vets_topic_list.append("Topic_" + str(x))

    Vet_contend_list = []
    for x in range(1, 6):
        Vet_contend_list.append("populate_blog/vet_text" + str(x) + ".txt")

    Vet_Pic_list = []
    for x in range(1, 6):
        Vet_Pic_list.append("populate_blog/Vet_Pic_" + str(x) + ".jpg")


    Shops_topic_list = []
    for x in range(1, 6):
        Shops_topic_list.append("Topic_" + str(x))

    Shop_contend_list = []
    for x in range(1, 6):
        Shop_contend_list.append("populate_blog/shop_text" + str(x) + ".txt")

    Shop_Pic_list = []
    for x in range(1, 6):
        Shop_Pic_list.append("populate_blog/Shop_Pic_" + str(x) + ".jpg")

    New_image =[]
    vet_image=[]
    shop_image=[]

    def addImgToObj(pathList , Tlist):

        for x in pathList:
            z = Image.open(x)
            Simg = ImageFile.open(z)
            z.close()
            Tlist.append(Simg)
            Simg.close()







    addImgToObj(News_Pic_list,New_image )
    addImgToObj(Vet_Pic_list, vet_image)
    addImgToObj(Shop_Pic_list, shop_image )




    for x in range(0,5):
        add_news(News_topic_list[x], File(open(News_contend_list[x], encoding="utf-8")),
                 New_image[x]
                 )
        add_vets(Vets_topic_list[x], File(open(Vet_contend_list[x], encoding="utf-8")),
                 vet_image[x]
                 )
        add_shop(Shops_topic_list[x], File(open(Shop_contend_list[x], encoding="utf-8")),
                 shop_image[x]

                 )



def add_news(topic, contend, image):
    n = news.objects.get_or_create(topic=topic, contend=contend, image=image)[0]
    n.save()
    return n

def add_vets(topic, contend, image):
    v = vet.objects.get_or_create(topic=topic, contend=contend, image=image)[0]
    v.save()
    return v

def add_shop(topic, contend, image):
    s = shop.objects.get_or_create(topic=topic, contend=contend, image=image)[0]
    s.save()
    return s






if __name__ == '__main__':
    print('Starting Blog population script...')
    populate()