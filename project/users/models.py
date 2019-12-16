from django.db import models
from django.contrib.auth.models import AbstractUser

# User model
class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    NID = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


#Users Types
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.user.first_name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    SSC_GPA = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    HSC_GPA = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    BMDC_RegNo = models.CharField(max_length=100, blank=False, null=False)
    MBBS_Session = models.CharField(max_length=100, blank=False, null=False)
    MBBS_Inst = models.CharField(max_length=100, blank=False, null=False)
    PostGrad_details = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.first_name
