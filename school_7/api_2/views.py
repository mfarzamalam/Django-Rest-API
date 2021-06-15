from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin, 
    CreateModelMixin, 
    RetrieveModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin,
)


#### Class which doesnot required primary key(pk) #####

class StudentList_Create(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



#### Class which required primary key(pk) #####

class StudentRetrieve_Update_Delete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)