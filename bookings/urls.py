from django.urls import path
from .views import AppointmentView, DetailAppoinmentView

urlpatterns = [
    path("appoinment/", AppointmentView.as_view()),
    path("appoinment/<int:pk>/", DetailAppoinmentView.as_view()),
]