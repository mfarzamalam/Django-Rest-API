from django.db import models

# Create your models here.
class Singer(models.Model):
    name   = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    song     = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    title    = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()