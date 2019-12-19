
from django.contrib import admin
from django.urls import path, include
from .views import home, PatientSearchView, SearchView, DoctorHomeView, PatientHomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', home, name='home'),
    path('medication/', include('prescription_gen.urls')),
    path('search/', SearchView.as_view(), name='search'),
    path('search/patient/', PatientSearchView.as_view(), name='search_results'),
    path('home/doctor', DoctorHomeView.as_view(), name='doctor_home'),
    path('home/patient', PatientHomeView.as_view(), name='patient_home'),
]
