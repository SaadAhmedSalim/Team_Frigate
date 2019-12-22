## @package forms
#  Documentation for this module named prescription generate.
#
#  More details about forms.

from django import forms
from django.forms.models import inlineformset_factory
from .models import Prescription, PrescriptionMedicine, Medicine

## inlineformset_factory(parent_model, model, form=ModelForm, formset=BaseInlineFormSet, fk_name=None,
#  fields=None, exclude=None, extra=3, can_order=False, can_delete=True, max_num=None,
#  formfield_callback=None, widgets=None, validate_max=False, localized_fields=None, labels=None, help_texts=None,
#   error_messages=None, min_num=None, validate_min=False, field_classes=None)

MedicineFormSet = inlineformset_factory(Prescription,
                                        PrescriptionMedicine,
                                        fk_name='prescription',
                                        fields=['medicine','timing', 'duration'],
                                        extra=1,
                                        can_delete=True)
## We use foreign key of prescription.
