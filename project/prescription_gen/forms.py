from django import forms
from django.forms.models import inlineformset_factory
from .models import Prescription, PrescriptionMedicine, Medicine


MedicineFormSet = inlineformset_factory(Prescription,
                                        PrescriptionMedicine,
                                        fk_name='prescription',
                                        fields=['medicine','timing', 'duration'],
                                        extra=1,
                                        can_delete=True)
