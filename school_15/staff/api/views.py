from staff.models import create_read
from staff.api.serializers import Create_read_serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserApi(ModelViewSet):
    queryset  = create_read.objects.all()
    serializer_class = Create_read_serializer
    authentication_classes = [SessionAuthentication]
    permission_classes     = [IsAuthenticatedOrReadOnly]