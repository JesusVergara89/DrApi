from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor

class DoctorViewSetTest(TestCase):
    
    def setUp(self):

        self.patient = Patient.objects.create(
        first_name = "Samuel",
        last_name = "Vergara",
        date_of_bith = "2010-12-03",
        contact_number = "12345678",
        email = "samuel@example.com",
        address = "colombia colombia sahagun",
        medical_history = "healthy"
        )

        self.doctor = Doctor.objects.create(
            first_name = "Romina",
            last_name = "Melchor",
            qualification = "neurology",   
            contact_number = "234568732738",
            email = "doctor3@example.com",
            address = "chile alemania calle 4",
            biography = "Nothing",
            is_on_vacation = False 
            )

        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse('doctor-appointments',
        kwargs= {
            "pk": self.doctor.id
        }
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)