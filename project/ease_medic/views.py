from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView

from users.models import Patient

# Defining a function which redirects home page by default also adding doctor and patient page if request
def home(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect('doctor_home')
        else:
            return redirect('patient_home')
    return render(request, 'home.html')

# A class which will show doctors home page
class DoctorHomeView(TemplateView):
    template_name = 'doctor_home.html'  # it is in templates-users-

# A class which will show patients home page
class PatientHomeView(TemplateView):
    template_name = 'patient_home.html' # it is in templates-users-

# A class which will show search bar
class SearchView(TemplateView):
    template_name = 'search_form.html' # it is in templates-users-

# A class which will show patient list in doctors home page
class PatientSearchView(ListView):
    model = Patient  # defined in database
    template_name = 'patient_search_results.html'  # it is in templates-users-

    def get_queryset(self):
        """It’s also possible to customize the queryset
            by overriding the get_queryset()
            some builtin query-> filter(), all(), get(), exclude()"""
        query = self.request.GET.get('q')
        object_list = Patient.objects.filter(user__NID=query)
        return object_list
