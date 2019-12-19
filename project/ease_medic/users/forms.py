from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import (Doctor, Patient, User)


#for public view
class PatientSignUpForm(UserCreationForm):
    address = forms.CharField(label='Address')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('NID', 'email', 'age', 'gender', 'first_name', 'last_name')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True

        user.save()
        address = self.cleaned_data.get('address')
        patient = Patient.objects.create(user=user, address=address)

        return user


class DoctorSignUpFrom(UserCreationForm):
    SSC_GPA = forms.DecimalField(label="SSC GPA")
    HSC_GPA = forms.DecimalField(label="HSC GPA")
    BMDC_RegNo = forms.CharField(label='BMDC Reg No')
    MBBS_Session = forms.CharField(label='MBBS Session')
    MBBS_Inst = forms.CharField(label='Institution')
    PostGrad_details = forms.CharField(label='PostGrad Info')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('NID', 'email', 'age', 'gender', 'first_name', 'last_name')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()

        SSC_GPA = self.cleaned_data.get('SSC_GPA')
        HSC_GPA = self.cleaned_data.get('HSC_GPA')
        BMDC_RegNo = self.cleaned_data.get('BMDC_RegNo')
        MBBS_Session = self.cleaned_data.get('MBBS_Session')
        MBBS_Inst = self.cleaned_data.get('MBBS_Inst')
        PostGrad_details = self.cleaned_data.get('PostGrad_details')
        doctor = Doctor.objects.create(user=user, SSC_GPA=SSC_GPA, HSC_GPA=HSC_GPA,
                            BMDC_RegNo=BMDC_RegNo, MBBS_Session=MBBS_Session,
                            MBBS_Inst=MBBS_Inst, PostGrad_details=PostGrad_details)
        return user
