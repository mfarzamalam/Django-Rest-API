from django.urls import path
# from .views import hello_api
from .views import StudentList, StudentCreate, StudentRetrieve, StudentUpdate, StudentDelete

urlpatterns = [
    path('studentApi/', StudentList.as_view()),
    # path('studentApi/', StudentCreate.as_view()),
    # path('studentApi/<int:pk>/', StudentRetrieve.as_view()),
    # path('studentApi/<int:pk>/', StudentUpdate.as_view()),
    # path('studentApi/<int:pk>/', StudentDelete.as_view()),
    # path('studentApi/<int:pk>/', student_api.as_view()),
]
