from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Hospital(models.Model):
    name=models.CharField(max_length=30)
    address = models.TextField(max_length=150,null=False)
    email=models.EmailField(unique=False)
    phone= models.IntegerField(max_length=10)
    description=models.CharField(max_length=400)

class Patient(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=6)
    phone=models.IntegerField(max_length=10)
    birth_date=models.DateField(null=True)
    description=models.CharField(max_length=50)

class categeory(models.Model):
    categeory ={"Emergency":"Emergency 1","OPD":"OPD 2","Criticle Illness":"Criticle Illness 3","Healthy":"Healthy 4"}

class BloodType(models.Model):
    BLOOD_GROUPS=[('A+','A+'),('B+','B+'),('AB+','AB+'),('O+','O+'),('A-','A-'),('B-','B-'),('AB-','AB-'),('O-','O-')]
    blood_type = models.CharField(max_length=3, choices=BLOOD_GROUPS)

class BloodSupply(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
