from django import forms
from django.forms.models import inlineformset_factory
from .models import Prescription, PrescriptionMedicine, Medicine


MedicineFormSet = inlineformset_factory(Prescription,
                                        PrescriptionMedicine,
                                        fk_name='prescription',
                                        fields=['medicine','timing', 'duration'],
                                        extra=1,
                                        can_delete=True)

# this set will allow to show the users the prescription details
# like which doctor gives this prescription
# it will show timing and can add another medicine in Prescription
