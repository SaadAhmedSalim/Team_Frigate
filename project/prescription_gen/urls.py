from django.urls import include, path

from .views import (MedicineCreateView, PrescriptionMedicineCreate,
                PrescriptionMedicineUpdateView, PrescriptionDetailView,
                PrescriptionCreateView, PrescriptionListView)
## add urls
#  to see the all branches
urlpatterns = [
    path('add/medicine/', MedicineCreateView.as_view(), name='add_medicine'),
    ## Locate the medicine page where can be added medicine
    path('add/prescription/medicine', PrescriptionMedicineCreate.as_view(), name='add_pr_med'),
    ## Locate the prescription where medicine can be added
    path('update/prescription/<pk>/', PrescriptionMedicineUpdateView.as_view(), name='pr_update'),
    ## Locate the prescription where it can be updated
    path('detail/prescription/<pk>/', PrescriptionDetailView.as_view(), name='pr_detail'),
    ## Locate the prescription where details can be seen
    path('add/prescription/patient/<pk>/', PrescriptionCreateView.as_view(), name='pr_create'),
    ## Locate the prescription where prescription can be created
    path('list/prescription/', PrescriptionListView.as_view(), name='pr_list'),
    ## Locate the prescription where it can be seen as a list view in admin
    ]
