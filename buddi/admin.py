from django.contrib import admin
from buddi.models import Animal, AnimalType, Region, Sitter, UserProfile, SitterOperatesInRegion, Comments, AnimalImages, Ad

# Register your models here.
admin.site.register(Animal)
admin.site.register(AnimalType)
admin.site.register(Region)
