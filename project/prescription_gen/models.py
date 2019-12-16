from django.db import models
from django.urls import reverse

from users.models import User, Patient, Doctor

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    miligram = models.PositiveIntegerField(default=5)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name

class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    tests = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "{}. Prescription for {} by {} {}".format(self.id,
                self.patient.user.first_name, self.doctor.user.first_name,
                self.timestamp)

    def get_absolute_url(self):
        return reverse('pr_update', kwargs={'pk': self.pk})

class PrescriptionMedicine(models.Model):
    prescription = models.ForeignKey('Prescription', related_name='pr_med', on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    timing = models.CharField(max_length=20, default = '1 + 0 + 1')
    duration = models.CharField(max_length=20, default = '1 week')

    def __str__(self):
        return self.medicine.name
