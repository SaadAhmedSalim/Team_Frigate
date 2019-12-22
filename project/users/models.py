from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

## User model

## A class named User.
class User(AbstractUser):
    ## A class variable is_doctor.
    is_doctor = models.BooleanField(default=False)
    ## A class variable is_patient.
    is_patient = models.BooleanField(default=False)
    ## A class variable NID.
    NID = models.CharField(max_length=50, blank=False, null=False)
    ## A class variable email.
    email = models.CharField(max_length=100)
    ## A class variable age.
    age = models.PositiveIntegerField(null=True, blank=True)
    ## A class variable gender.
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def get_absolute_url(self): # new
        return reverse('doctor_detail', args=[str(self.id)])


## Users Types

## Define a class Patient.
class Patient(models.Model):
    ## A class variable user.
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ## A class variable address.
    address = models.CharField(max_length=255, blank=False, null=False)

    ## Documentation for a method __str__
    #  @param self the object pointer
    def __str__(self):
        return self.user.first_name

## Define a class Doctor.
class Doctor(models.Model):
    ## A class variable user.
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ## A class variable SSC_GPA.
    SSC_GPA = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    ## A class variable HSC_GPA.
    HSC_GPA = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    ## A class variable BMDC_RegNo.
    BMDC_RegNo = models.CharField(max_length=100, blank=False, null=False)
    ## A class variable MBBS_Session.
    MBBS_Session = models.CharField(max_length=100, blank=False, null=False)
    ## A class variable MBBS_Inst.
    MBBS_Inst = models.CharField(max_length=100, blank=False, null=False)
    ## A class variable PostGrad_details.
    PostGrad_details = models.CharField(max_length=255, blank=True, null=True)

    ## Documentation for a method __str__
    #  @param self the object pointer .
    def __str__(self):
        return self.user.first_name
