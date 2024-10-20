from rest_framework import serializers
from .models import *


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = "__all__"
