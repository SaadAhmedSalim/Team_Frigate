from django.contrib import admin

from.models import Medicine, PrescriptionMedicine, Prescription

admin.site.register(Medicine)  # it will allow to show medicine add in database
admin.site.register(Prescription)  # it will allow to generate prescription in database
admin.site.register(PrescriptionMedicine)  # it will allow to add medicine in prescription in database
