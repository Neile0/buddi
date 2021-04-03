from django.contrib import admin
from .models import Animal, AnimalType, Region, Sitter, UserProfile, SitterOperatesInRegion, Comments, AnimalImages, Ad



# Register your models here.
#Do we need all these? Not sure. Feel free to remove the unnecessary
admin.site.register(Animal)
admin.site.register(AnimalType)
admin.site.register(Region)
admin.site.register(Sitter)
admin.site.register(UserProfile)
admin.site.register(SitterOperatesInRegion)
admin.site.register(Comments)
admin.site.register(AnimalImages)
admin.site.register(Ad)



