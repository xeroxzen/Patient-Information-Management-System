from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Patient, Doctor
from .forms import PatientModelForm, PatientForm, ContactForm, ContactModelForm

login_required_m = method_decorator(login_required)

@login_required
def index(request):
    context = {
        'title': 'HealthNet Dashboard',
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/index.html', context)

# A function to add new patient to the database
# This form uses the PatientModelForm()
@login_required
def patient_form(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            # Process the cleaned_data
            patient = Patient.objects.create(
                prefix = form.cleaned_data.get('prefix'),
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                date_of_birth = form.cleaned_data.get('date_of_birth'),
                gender = form.cleaned_data.get('gender'),
                home_address = form.cleaned_data.get('home_address'),
                national_id = form.cleaned_data.get('national_id'),
                phone_number = form.cleaned_data.get('phone_number'),
                email_address = form.cleaned_data.get('email_address'),
                purpose_of_visit = form.cleaned_data.get('purpose_of_visit'),
                description_of_the_condition = form.cleaned_data.get('description_of_the_condition'),
                prescription = form.cleaned_data.get('prescription'),
                current_temperature = form.cleaned_data.get('current_temperature'),
                blood_type = form.cleaned_data.get('blood_type'),
                current_medication = form.cleaned_data.get('current_medication'),
                body_mass = form.cleaned_data.get('body_mass'),
                allergies = form.cleaned_data.get('allergies'),
                employment_status = form.cleaned_data.get('employment_status'),
                consulted_doctor = form.cleaned_data.get('consulted_doctor'),
                marital_status = form.cleaned_data.get('marital_status'),
                medical_aid_group = form.cleaned_data.get('medical_aid_group'),
                date_of_visit = form.cleaned_data.get('date_of_visit'),
            )
            patient.prefix = form.cleaned_data.get('prefix')
            patient.first_name = form.cleaned_data.get('first_name')
            patient.last_name = form.cleaned_data.get('last_name')
            patient.date_of_birth = form.cleaned_data.get('date_of_birth')
            patient.gender = form.cleaned_data.get('gender')
            patient.home_address = form.cleaned_data.get('home_address')
            patient.national_id = form.cleaned_data.get('national_id')
            patient.phone_number = form.cleaned_data.get('phone_number')
            patient.email_address = form.cleaned_data.get('email_address')
            patient.purpose_of_visit = form.cleaned_data.get('purpose_of_visit')
            patient.description_of_the_condition = form.cleaned_data.get('description_of_the_condition')
            patient.prescription = form.cleaned_data.get('prescription')
            patient.current_temperature = form.cleaned_data.get('current_temperature')
            patient.blood_type = form.cleaned_data.get('blood_type')
            patient.current_medication = form.cleaned_data.get('current_medication')
            patient.body_mass = form.cleaned_data.get('body_mass')
            patient.allergies = form.cleaned_data.get('allergies')
            patient.employment_status = form.cleaned_data.get('employment_status')
            patient.consulted_doctor = form.cleaned_data.get('consulted_doctor')
            patient.marital_status = form.cleaned_data.get('marital_status')
            patient.medical_aid_group = form.cleaned_data.get('medical_aid_group')
            patient.date_of_visit = form.cleaned_data.get('date_of_visit')

            print('Data saved successfully')
            patient.save()
            return HttpResponse('Patient successfully added to the database')

    else:
        form = PatientForm()

    context = {
        'form': form,
        'title': "Add New Patient",
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/form.html', context)

# A function for a successfull posting
# def success(request):
#      return HttpResponseRedirect('/HealthNet/success.html')

# A function to view all patients in the database
@login_required
def view_all(request):
    template_name = 'view_patients.html'
    patients = Patient.objects.all()
    paginator = Paginator(patients, 30)
    if request.method == 'GET':
        page = request.GET.get('page')
    patients = paginator.get_page(page)

    context = {
        'title': 'All Patients',
        'patients': patients,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
        }

    return render(request, 'HealthNet/view_patients.html', context)

@login_required
def staff(request):
    template = 'staff.html'
    staff = Doctor.objects.all()
    paginator = Paginator(staff, 20)
    if request.method == 'GET':
        page = request.GET.get('page')
    staff = paginator.get_page(page)

    context = {
        'title': 'All Doctors',
        'staff': staff,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
        }

    return render(request, 'HealthNet/staff.html', context)

# A function to to view details of any patient selected, they're selected using the unique id

@login_required
def patient_info(request, id):
    template_name = 'detail_patient.html'
    patient = Patient.objects.get(id=id)

    context = {
        'title': 'Information',
        'patient': patient,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/detail_patient.html', context)

# This is a function for editing a patient's Information

@login_required
def edit_info(request, id=None):
    item = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/HealthNet/patients/view_all')

    context = {
        'title': 'Updating Information',
        'form': form,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/form.html', context)

def delete_info(request, id=None):
    item = get_object_or_404(Patient, id=id)
    item.delete()
    return redirect('HealthNet/patients/view_all')
# A function used to see if there are any reports generated by the system
@login_required
def get_reports(request):
    template_name = "reports.html"
    reports = Patient.objects.all()
    alert_list = [
        "Flu",
        "Cholera",
        "Waterborne",
        "Rubella"
    ]

    # if reports in alert_list:
    paginator = Paginator(reports, 30)
    if request.method == 'GET':
        page_requested = request.GET.get('page')
    reports = paginator.get_page(page_requested)

    context = {
        'title' : 'Reports',
        'report' : reports,
        'project_name' : 'ProMed HealthNet Inc',
        'creator' : 'Andile XeroxZen',
        'purpose' : 'Patient Information Management System'
    }

    return render(request, 'HealthNet/reports.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:

            form.save()

    context = {
        'form' : form,
        'project_name' : 'ProMed HealthNet Inc',
        'title' : 'Contact Us'
    }
    return render(request, 'HealthNet/form.html', context)

def contact_snippet(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid():
            contact = Contact.objects.create(
                name = form.cleaned_data.get('name'),
                subject = form.cleaned_data.get('subject'),
                email = form.cleaned_data.get('email'),
                category = form.cleaned_data.get('category'),
                message = form.cleaned_data.get('message')
            )

            contact.save()

    form = ContactForm()

    context = {
        'form' : form,
        'project_name' : 'ProMed HealthNet Inc',
        'title' : 'Contact Us'
    }

    return render(request, 'HealthNet/form.html', context)
