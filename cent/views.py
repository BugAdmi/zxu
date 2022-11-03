from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from cent.models import CentView
from cent.serializer import SerializerStaff
class StaffView(ModelViewSet):
    queryset = CentView.objects.all()
    serializer_class = SerializerStaff
