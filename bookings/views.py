from .serializers import AppointmentSerializer
from .models import Appointment
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class AppointmentView(ListAPIView, CreateAPIView):
    """
    Get the appoinment date and time
    """
    allowed_methods = ['GET','POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class DetailAppoinmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
