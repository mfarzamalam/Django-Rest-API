from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    age  = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    
    #### Field level validations
    def validate_age(self, value):
        if value > 25:
            print(value)
            raise serializers.ValidationError("People with age more than 25 are not allowed to sit in")
        else:
            return value


    #### object level validations
    def validate(self, data):
        name = data.get('name')
        database_names = Student.objects.values_list('name', flat=True)

        for all_name in database_names:
            if name in all_name:
                raise serializers.ValidationError("Person is already exist")
        else:
            return data