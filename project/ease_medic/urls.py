## @package pyexample
#  Documentation for this module.
#
#  More details.
from django.contrib import admin
from django.urls import path, include
from .views import home, PatientSearchView, SearchView, DoctorHomeView, PatientHomeView, GoogleApiView
## add urls
#  to see the all branches
urlpatterns = [
    path('admin/', admin.site.urls),
## Admin page view.
    path('accounts/', include('django.contrib.auth.urls')),
## Admin can view all the users pages.
    path('users/', include('users.urls')),
## user can view their prespective pages.
    path('', home, name='home'),
    path('medication/', include('prescription_gen.urls')),
## when a doctor generate a prescription they can follow this steps.
    path('search/', SearchView.as_view(), name='search'),
## This is for all to search doctor.
    path('search/patient/', PatientSearchView.as_view(), name='search_results'),
## This is for doctor who searches patient by using their NID.
    path('home/doctor', DoctorHomeView.as_view(), name='doctor_home'),
## This is doctors home page.
    path('home/patient', PatientHomeView.as_view(), name='patient_home'),
## This is patients home page.
    path('googleApi/',GoogleApiView.as_view(), name = 'api'),
]
