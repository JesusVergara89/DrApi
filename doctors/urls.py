from django.urls import path
from .views import ListDoctorsView, DetailDoctorView
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet

router = DefaultRouter()
router.register('doctors',DoctorViewSet)

urlpatterns = router.urls

"""
[
    path("doctors/", ListDoctorsView.as_view()),
    path("doctors/<int:pk>/", DetailDoctorView.as_view()),
]
"""