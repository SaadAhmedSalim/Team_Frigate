from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import (Doctor, Patient, User)
## for public view

## Define a class name PatientSignUpForm.
class PatientSignUpForm(UserCreationForm):
    ## @var named address.
    address = forms.CharField(label='Address')

    ## Define a meta class.
    class Meta(UserCreationForm.Meta):
        ## A class variable named model.
        model = User
        ## @var model will inherit users.user.
        ## A class variable named fields.
        fields = UserCreationForm.Meta.fields + ('NID', 'email', 'age', 'gender', 'first_name', 'last_name')
        ## @var fields will inherit all the objects from users.user.

    ## Documentation for a method
    #  called save which used as a super class.
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True

        user.save()
        address = self.cleaned_data.get('address')
        patient = Patient.objects.create(user=user, address=address)

        return user
        ## return the user

## Define a class called DoctorSignUpFrom.
class DoctorSignUpFrom(UserCreationForm):
    ## A class variable named SSC_GPA.
    SSC_GPA = forms.DecimalField(label="SSC GPA")
    ## A class variable named HSC_GPA.
    HSC_GPA = forms.DecimalField(label="HSC GPA")
    ## A class variable named BMDC_RegNo.
    BMDC_RegNo = forms.CharField(label='BMDC Reg No')
    ## A class variable named MBBS_Session.
    MBBS_Session = forms.CharField(label='MBBS Session')
    ## A class variable named MBBS_Inst.
    MBBS_Inst = forms.CharField(label='Institution')
    ## A class variable named PostGrad_details.
    PostGrad_details = forms.CharField(label='PostGrad Info')


    ## define a class Meta
    #  which will inherit users.user
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
