from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


# NOTE: all on_deletes are set to CASCADE. This would be changed in a realistic deployment


# A custom model that ensures an integer is between min and max values
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


# Written by Aidan
class Region(models.Model):
    REGION_LENGTH = 120
    name = models.CharField(max_length=REGION_LENGTH, unique=True, primary_key=True)
    is_subregion_of = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='parent_region')
    is_parent_region = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.is_subregion_of is not None:
            self.is_parent_region = False
        super(Region, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# Written by Aidan
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    NAME_MAX_LENGTH = 128
    BIO_MAX_LENGTH = 300
    PHONE_NUMBER_LENGTH = 11

    # Li delete the following datafield as I think some of them already in the default user setting.
    # forename = models.CharField(max_length=NAME_MAX_LENGTH)
    # middle_names = models.CharField(max_length=NAME_MAX_LENGTH, default="")
    # surname = models.CharField(max_length=NAME_MAX_LENGTH)
    bio = models.CharField(max_length=BIO_MAX_LENGTH)

    def profile_image_upload(self):
        return 'profile_images/{}'.format(self.user.username)

    profile_image = models.ImageField(upload_to=profile_image_upload, blank=True,
                                      default="profile_images/profile_image_placeholder.png")
    profile_url = models.URLField(blank=True, unique=True)
    contact_no = models.CharField(max_length=PHONE_NUMBER_LENGTH)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    is_sitter = models.BooleanField(default=False)

    def __str__(self):
        return "(" + self.user.first_name + self.user.last_name + ", " + self.profile_url + ")"


# Written by Aidan
class AnimalType(models.Model):
    type = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.type


# Written by Aidan
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
    exercise_requirement = IntegerRangeField(min_value=0, max_value=10)
    is_displayed = models.BooleanField(default=True)
    image_dir = models.SlugField(unique=True)

    def save_image(self, *args, **kwargs):
        self.image_dir = slugify(self.user.profile_url + self.name)

    def __str__(self):
        return "(" + self.name + "," + self.user.user.username + ")"


# Written by Aidan
class AnimalImages(models.Model):
    def image_directory_path(self, name):
        # file will be uploaded to MEDIA_ROOT/<animal>/<image-name>
        return '{0}/{1}'.format(self.animal, name)

    DIR = "animal_images/"
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path)

    class Meta:
        verbose_name = "Animal Images"

    def __str__(self):
        return self.DIR + self.animal.name + self.animal.image_dir


# Written by Aidan
class Sitter(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.user.user.username


# Written by Aidan
class SitterOperatesInRegion(models.Model):
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sitter's Regions"

    def __str__(self):
        return (self.sitter.user.user.username + " in " + self.region.name)


# Written by Aidan
class Comments(models.Model):
    MAX_COMMENT_LENGTH = 400
    MAX_COMMENT_SUBJECT = 120
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    title = models.CharField(max_length=MAX_COMMENT_SUBJECT)
    rating = IntegerRangeField(min_value=0, max_value=10)
    made_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.CharField(max_length=MAX_COMMENT_LENGTH, default="No message")

    class Meta:
        verbose_name = "Comments"


# Written by Aidan
class Ad(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)

    def __str__(self):
        show = self.animal.name + ", " + self.type.__str__()
        return show
