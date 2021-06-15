from django.urls import path
# from .views import hello_api
from .views import StudentList_Create, StudentRetrieve_Update_Delete

urlpatterns = [
    path('studentApi/', StudentList_Create.as_view()),
    path('studentApi/<int:pk>/', StudentRetrieve_Update_Delete.as_view()),
]