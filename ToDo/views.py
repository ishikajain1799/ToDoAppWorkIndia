from django.shortcuts import render
from rest_framework import viewsets
from .serializers import toDoSerializer
from .models import toDo

class toDoViewSet(viewsets.ModelViewSet):
    queryset = toDo.objects.all().order_by('due_date')
    serializer_class = toDoSerializer

# Create your views here.
