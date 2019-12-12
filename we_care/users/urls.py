from django.urls import include, path

from .views import SignUpView, DoctorSignUpView, PatientSignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/doctor', DoctorSignUpView.as_view(), name='signup_doctor'),
    path('signup/patient', PatientSignUpView.as_view(), name='signup_patient'),
]
