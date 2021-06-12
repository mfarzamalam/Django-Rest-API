from rest_framework import serializers
from .models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name','age','city']
        # read_only_fields = ['name','age']
        # extra_kwargs     = {'name':{'read_only': True}}


    def validate_age(self, attrs):
        if attrs > 25:
            raise serializers.ValidationError("Age must be less than 25")
        else:
            return attrs


    def validate(self, attrs):
        seats = Student.objects.all()
        total = seats.count()

        if total < 5:
            return attrs
        else:
            raise serializers.ValidationError("Seat is full")