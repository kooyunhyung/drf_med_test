from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import med_dispenser
from .serializers import MedSerializer

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def bloodSugar(request, id):
    totalBloodSugar = med_dispenser.objects.all()
    serializer = MedSerializer(totalBloodSugar, many=True)
    return Response(serializer.data)