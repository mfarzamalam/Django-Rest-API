from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','roll','city','name']

    def validate(self, attrs):
        all_names = Student.objects.values_list('name', flat=True)
        name      = attrs.get('name')

        for names in all_names:
            if name == names:
                raise serializers.ValidationError("Name is already exist")
        
        return attrs