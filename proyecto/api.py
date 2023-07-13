from .models import Proyecto
from rest_framework import viewsets, permissions
from .serializers import SerializarProyecto

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SerializarProyecto