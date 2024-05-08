from django.forms import ModelForm
from home.models import *

class Patientform(ModelForm):
    class Meta():
        model = Patient
        fields = ['gender','name','phone','birth_date','description']