from .serializers import DoctorSerializer
from .models import Doctor
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

"""
Views based on functions
@api_view(['GET','POST'])
def list_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
"""
#Views based on classes
class ListDoctorsView(ListAPIView,CreateAPIView):
    allowed_methods = ['GET','POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
