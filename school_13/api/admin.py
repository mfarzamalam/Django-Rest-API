from django.contrib import admin
from .models import School

# Register your models here.
@admin.register(School)
class AdminSchool(admin.ModelAdmin):
    list_display = ['id','name','student','teacher','total_staff']