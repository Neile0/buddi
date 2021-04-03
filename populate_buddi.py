"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','buddi_project.settings')

import django
django.setup()
from buddi.models import *

def populate():
    """
    
    
    
