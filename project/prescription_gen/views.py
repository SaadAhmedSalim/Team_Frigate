from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import CreateView, DetailView
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Medicine, PrescriptionMedicine, Prescription
from .forms import MedicineFormSet
from users.models import User, Doctor, Patient

class MedicineCreateView(CreateView):
    model = Medicine
    template_name = 'prescription_gen/medicine_new.html'
    fields = '__all__'


class PrescriptionMedicineCreate(CreateView):
    model = PrescriptionMedicine
    template_name = 'prescription_gen/pr_medicine.html'
    fields = '__all__'



class PrescriptionMedicineUpdateView(TemplateResponseMixin, View):
    template_name = 'prescription_gen/formset.html'
    prescription = None

    def get_formset(self, data=None):
        return MedicineFormSet(instance=self.prescription, data=data)

    def dispatch(self, request, pk):
        self.prescription = get_object_or_404(Prescription, id=pk)
        return super(PrescriptionMedicineUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'prescription': self.prescription,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        p_key = self.kwargs['pk']
        if formset.is_valid():
            formset.save()
            return redirect('pr_update', p_key) ## Update with prescription detail
        return self.render_to_response({'prescription': self.prescription,
                                        'formset': formset})

class PrescriptionCreateView(CreateView):
    model = Prescription
    fields = ['tests']
    template_name = 'prescription_gen/pr_create.html'

    # def get_success_url(self):
    #         return reverse('pr_update', kwargs={'pk': self.object.pk})
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         self.fcc_form = form.save(commit=True)
    #         #messages.add_message(self.request, messages,INFO, 'prescription created')
    #         return HttpResponseRedirect(reverse('pr_update', kwargs={'pk': self.fcc_form.uuid}))

    def form_valid(self, form):
        user = self.request.user
        doctor = Doctor.objects.get(user=user)
        patient = Patient.objects.get(pk=self.kwargs['pk'])
        form.instance.doctor = doctor
        form.instance.patient = patient
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        flag = request.user.is_doctor
        if not flag:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(PrescriptionCreateView, self).get_context_data(*args, **kwargs)
        patient_id = self.kwargs['pk']
        patient = Patient.objects.get(pk=patient_id)
        context['patient'] = patient
        doctor = self.request.user
        context['doctor'] = Doctor.objects.filter(user=doctor)
        return context


class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'prescription_gen/prescription_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PrescriptionDetailView, self).get_context_data(*args, **kwargs)
        id = self.kwargs['pk']
        context['medicines'] = PrescriptionMedicine.objects.filter(prescription__id=id)
        return context
