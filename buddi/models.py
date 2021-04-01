from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    NAME_MAX_LENGTH = 128
    BIO_MAX_LENGTH = 300
    PHONE_NUMBER_LENGTH = 11

    forename = models.CharField(max_length=NAME_MAX_LENGTH)
    middle_names = models.CharField(max_length=NAME_MAX_LENGTH, default="")
    surname = models.CharField(max_length=NAME_MAX_LENGTH)
    bio = models.CharField(max_length=BIO_MAX_LENGTH)
    profile_image = models.ImageField(upload_to='profile_images', blank=True,
                                      default="profile_images/profile_image_placeholder.jpg")
    profile_url = models.URLField(blank=True, unique=True)
    contact_no - models.CharField(max_length=PHONE_NUMBER_LENGTH)
    region = modls.ForeignKey(Region, on_delete=models.CASCADE)
    is_sitter = models.BooleanField(default=false)

    def __str__(self):
        return "(" + self.forname + self.middle_names + self.surname + "," + self.profile_url + ")"


class Animal(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    NAME_MAX_LENGTH = 128
    BIO_MAX_LENGTH = 300

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    bio = models.CharField(max_length=BIO_MAX_LENGTH)
    age = models.IntegerField()

    class SexChoicesEnum(mdoels.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('FEMALE')

    sex = models.CharField(max_length=1, choices=SexChoicesEnum.choices)

    class IsNeuteredEnum(models.TextChoices):
        YES = 'Y', _('Yes')
        NO = 'N', _('No')
        PREFER_NOT_TO_SAY = 'N/A', _('Prefer not to say')

    is_neutered = models.CharField(max_length=3, choices=IsNeuteredEnum.choices)
    requires_exercise = models.BooleanField()
    exercise_requirement = models.IntegerRangeField(min_value=1, max_value=10)
    is_displayed = models.BooleanField(default=True)
    image_dir = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.image_dir = slugify(user.profile_url + self.name)

    def __str__(self):
        return "(" + self.name + "," + UserProfile.__str__(user) + ")"


class AnimalType(models.Model):
    type = models.CharField(max_length=128)

    def __str__(self):
        return self.type


class AnimalImages(models.Model):
    DIR = "animal_images/"
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=DIR + animal.image_dir)

    def __str__(self):
        return self.DIR + animal.image_dir + self.image


class Sitter(models.Model):
    user = models.ForeignKey(UserProfile)

    hourly_rate = models.DecimalField()
