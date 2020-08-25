from rest_framework import serializers
from .models import toDo

class toDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = toDo
        fields = ('title', 'description', 'category', 'due_date')