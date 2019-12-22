from django.db import models
from django.urls import reverse

from users.models import User, Patient, Doctor
## Define a class called medicine.
class Medicine(models.Model):
    ## A class variable.
    name = models.CharField(max_length=50)
    miligram = models.PositiveIntegerField(default=5)
    ## @var named name
    ## @var named miligram

    ## Documentation for a method
    #  called get_absolute_url which is used in testcase
    #  @param self The object pointer
    def get_absolute_url(self):
        return reverse('home')


    ## Documentation for a method
    #  called __str__ which is used in testcase
    #  @param self The object pointer
    def __str__(self):
        return self.name

## Define a class called prescription
class Prescription(models.Model):
    ## A class variable named doctor.
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    ## A class variable named patient.
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ## A class variable named timestamp.
    timestamp = models.DateTimeField(auto_now_add=True)
    ## A class variable named tests.
    tests = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "{}. Prescription for {} by {} {}".format(self.id,
                self.patient.user.first_name, self.doctor.user.first_name,
                self.timestamp)

    def get_absolute_url(self):
        return reverse('pr_update', kwargs={'pk': self.pk})

## Define a class called prescriptionMedicine
class PrescriptionMedicine(models.Model):
    ## A class variable named prescription.
    prescription = models.ForeignKey('Prescription', related_name='pr_med', on_delete=models.CASCADE)
    ## A class variable named medicine.
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    ## A class variable named timing.
    timing = models.CharField(max_length=20, default = '1 + 0 + 1')
    ## A class variable named duration.
    duration = models.CharField(max_length=20, default = '1 week')

    def __str__(self):
        return self.medicine.name
