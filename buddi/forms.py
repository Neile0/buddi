
from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, Region, Animal, AnimalType


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    picture = forms.FileField(required=False)

    class Meta:
        model = UserProfile
        fields = ('picture',)
        
        
SEX_CHOICES= (('M', 'Male'),
    ('F', 'Female'),)

NEUTERED_CHOICES=(
    ('Y', 'Yes'),
    ('N', 'No'),
    ('N/A', 'Prefer not to say'),)

TYPES=(
       (AnimalType.objects.get(type ='cat'), 'cat'),
       (AnimalType.objects.get(type ='dog'), 'dog'),
       (AnimalType.objects.get(type = 'bunny'), 'bunny'),
       )
    

class AnimalForm(forms.ModelForm):
   
    name = forms.CharField(max_length=Animal.NAME_MAX_LENGTH,
                           help_text="Please enter the name of your pet")
    type=forms.CharField(max_length=128, help_text="What type of pet do you have?")
    bio = forms.CharField(max_length=Animal.BIO_MAX_LENGTH,
                          help_text="Give us some details about your pet",
                          required=False)
    age = forms.IntegerField(help_text="Please enter the age of your pet")
    sex = forms.MultipleChoiceField(choices=SEX_CHOICES,
                                    help_text="Please enter your pet's gender")
    is_neutered = forms.MultipleChoiceField(choices=NEUTERED_CHOICES,
                                            help_text="Is your pet neutered?")
    requires_exercise=forms.BooleanField(required=False,
                                         help_text="This pet needs exercise")
    exercise_requirement=forms.IntegerField(help_text="If the pet does not need exercise, plase enter 0")
    is_displayed=forms.BooleanField(required=False,
                                    help_text='I want this pet to be displayed')
    
    class Meta:
        model = Animal
        exclude = ('user', 'image_dir')
        
    def clean(self):
        cleaned_data=self.cleaned_data
        text_type = cleaned_data.get('type')
        true_type = AnimalType.objects.all().get(type=text_type)
        cleaned_data['type'] = true_type
        cleaned_data['sex'] = cleaned_data['sex'][0] 
        cleaned_data['is_neutered'] = cleaned_data['is_neutered'][0]
        
        return cleaned_data
    
    
    
  
        

