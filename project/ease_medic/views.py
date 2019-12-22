from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView

from users.models import Patient


def home(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect('doctor_home')
        else:
            return redirect('patient_home')
    return render(request, 'home.html')

class DoctorHomeView(TemplateView):
    template_name = 'doctor_home.html'


class PatientHomeView(TemplateView):
    template_name = 'patient_home.html'


class SearchView(TemplateView):
    template_name = 'search_form.html'

class PatientSearchView(ListView):
    model = Patient
    template_name = 'patient_search_results.html'

    def get_queryset(self):
        """It’s also possible to customize the queryset
            by overriding the get_queryset()
            some builtin query-> filter(), all(), get(), exclude()"""
        query = self.request.GET.get('q')
        object_list = Patient.objects.filter(user__NID=query)
        return object_list

class GoogleApiView(TemplateView):
    template_name = 'googleApi.html'
