from django.contrib import admin
from .models import Singer, Song, Student
# Register your models here.

admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Student)