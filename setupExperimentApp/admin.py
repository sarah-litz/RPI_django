from django.contrib import admin

# Register your models here.
from .models import Experiment, Script 

admin.site.register(Experiment)
admin.site.register(Script)
