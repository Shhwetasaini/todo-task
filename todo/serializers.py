from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status']

    def validate(self, data):
        title = data.get('title')
        status_value = data.get('status')
        
        if not title:
            raise serializers.ValidationError({'title': 'This field is required.'})
        if status_value not in dict(Todo.STATUS_CHOICES).keys():
            raise serializers.ValidationError({'status': 'Invalid status value.'})
        
        return data
