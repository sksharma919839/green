from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializers import *


class serviceView(viewsets.ModelViewSet):
    queryset = service.objects.all()
    serializer_class = serviceSerializer
    parser_classes = (MultiPartParser, FormParser)
