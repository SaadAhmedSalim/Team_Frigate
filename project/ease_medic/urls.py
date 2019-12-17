from django.contrib import admin
from django.urls import path, include
from .views import home, PatientSearchView, SearchView, DoctorHomeView, PatientHomeView
# imported from templates-users-home.html
# imported from views.py - (ease_medic)
urlpatterns = [
    path('admin/', admin.site.urls),   # it will redirect default Django administration page
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),  # it will redirect main home page
    path('', home, name='home'),
    path('medication/', include('prescription_gen.urls')),  # it will redirect prescriptions page
    path('search/', SearchView.as_view(), name='search'),   # search process
    path('search/patient/', PatientSearchView.as_view(), name='search_results'),  # patient can be searched by Doctors
    path('home/doctor', DoctorHomeView.as_view(), name='doctor_home'), # it will show doctors home page
    path('home/patient', PatientHomeView.as_view(), name='patient_home'),  # it will show patients home page
]
