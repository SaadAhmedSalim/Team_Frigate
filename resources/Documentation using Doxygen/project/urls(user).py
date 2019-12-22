from django.urls import include, path

from .views import (SignUpView, DoctorSignUpView, PatientSignUpView,
            DoctorsListView, PatientDetailView, DoctorDetailView)

## add urls
urlpatterns = [
    ## Locate the sign page
    path('signup/', SignUpView.as_view(), name='signup'),
    ## Locate the doctors sign up page
    path('signup/doctor', DoctorSignUpView.as_view(), name='signup_doctor'),
    ## Locate the patients sign up page
    path('signup/patient', PatientSignUpView.as_view(), name='signup_patient'),
    ## Locate the doctors list for view
    path('doctors/', DoctorsListView.as_view(), name='doctor_list'),
    ## Locate the patient details in patient page
    path('patient/<pk>/', PatientDetailView.as_view(), name='patient_detail'),
    ## Locate the doctors details in doctors page
    path('doctor/<pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
]
