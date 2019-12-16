from django.contrib import admin

from.models import Medicine, PrescriptionMedicine, Prescription

admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(PrescriptionMedicine)
