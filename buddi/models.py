from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Region(models.Model):
    REGION_LENGTH = 120
    name = models.CharField(max_length=REGION_LENGTH, unique=True)
    is_subregion_of = models.ForeignKey('self', on_delete=models.CASCADE)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    NAME_MAX_LENGTH = 128
    BIO_MAX_LENGTH = 300
    PHONE_NUMBER_LENGTH = 11

    #Li delete the following datafield as I think some of them already in the default user setting.
    #forename = models.CharField(max_length=NAME_MAX_LENGTH)
    #middle_names = models.CharField(max_length=NAME_MAX_LENGTH, default="")
    #surname = models.CharField(max_length=NAME_MAX_LENGTH)
    bio = models.CharField(max_length=BIO_MAX_LENGTH)
    profile_image = models.ImageField(upload_to='profile_images', blank=True,
                                      default="profile_images/profile_image_placeholder.jpg")
    profile_url = models.URLField(blank=True, unique=True)
    contact_no = models.CharField(max_length=PHONE_NUMBER_LENGTH)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    is_sitter = models.BooleanField(default=False)

    def __str__(self):
        return "(" + self.forname + self.middle_names + self.surname + "," + self.profile_url + ")"


class AnimalType(models.Model):
    type = models.CharField(max_length=128)

    def __str__(self):
        return self.type


class Animal(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    NAME_MAX_LENGTH = 128
    BIO_MAX_LENGTH = 300

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    bio = models.CharField(max_length=BIO_MAX_LENGTH)
    age = models.IntegerField()

    class SexChoicesEnum(models.TextChoices):
        MALE = ('M', 'Male')
        FEMALE = ('F', 'Female')

    sex = models.CharField(max_length=1, choices=SexChoicesEnum.choices)

    class IsNeuteredEnum(models.TextChoices):
        YES = ('Y', 'Yes')
        NO = ('N', 'No')
        PREFER_NOT_TO_SAY = ('N/A', 'Prefer not to say')

    is_neutered = models.CharField(max_length=3, choices=IsNeuteredEnum.choices)
    requires_exercise = models.BooleanField()
    exercise_requirement = IntegerRangeField(min_value=1, max_value=10)
    is_displayed = models.BooleanField(default=True)
    image_dir = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.image_dir = slugify(self.user.profile_url + self.name)

    def __str__(self):

        return "(" + self.name + "," + UserProfile.__str__(User) + ")"


class AnimalImages(models.Model):
    def image_directory_path(self, name):

        # file will be uploaded to MEDIA_ROOT/<animal>/<image-name>
        return '{0}/{1}'.format(self.user.animal.image_dir, name)
    
    DIR = "animal_images/"
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path)

    def __str__(self):
        return self.DIR + self.animal.image_dir + self.image


class Sitter(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    hourly_rate = models.DecimalField(max_digits=4, decimal_places=1 )


class SitterOperatesInRegion(models.Model):
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Comments(models.Model):
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    rating = IntegerRangeField(min_value=0, max_value=10)


class Ad(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)

