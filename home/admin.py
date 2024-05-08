from django.contrib import admin
from home.models import *

# Register your models here.
class patientadmin(admin.ModelAdmin):
    list_display=('gender','name','birth_date','phone')

admin.site.register(Patient,patientadmin)