from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from .forms import DoctorSignUpFrom, PatientSignUpForm
from .models import Doctor, Patient, User


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpFrom
    template_name = 'registration/doctor_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/patient_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
