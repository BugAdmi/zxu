# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from cent.models import CentView

class SerializerStaff(ModelSerializer):
    class Meta:
        model = CentView
        fields = "__all__"