from rest_framework import serializers
from .models import med_dispenser

class MedSerializer(serializers.ModelSerializer):
    class Meta:
        model = med_dispenser
        fields = ('title','bloodSugar','bloodPressure_high','bloodPressure_low','liverShame')