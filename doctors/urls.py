from django.urls import path
from .views import detail_doctor,ListDoctorsView

urlpatterns = [
    path("doctors/", ListDoctorsView.as_view(), name="list_doctors"),
    path("doctors/<int:pk>", detail_doctor, name="detail_doctor"),
]