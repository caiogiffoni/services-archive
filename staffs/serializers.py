from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
