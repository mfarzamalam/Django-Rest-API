from django.contrib import admin
from django.urls import path
from API.views import StudentJsonObjectView, StudentJsonQuerySetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json-single/', StudentJsonObjectView),
    path('json-all/', StudentJsonQuerySetView),
]
