from rest_framework import serializers
from staff.models import create_read


class Create_read_serializer(serializers.ModelSerializer):
    class Meta:
        model = create_read
        fields = ['name','email']