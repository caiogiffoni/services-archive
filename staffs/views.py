from django.shortcuts import render
from rest_framework import generics

from staffs.models import Staff
from staffs.serializers import StaffSerializer

# Create your views here.


class StaffView(generics.ListCreateAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

    lookup_url_kwarg = "staff_id"
