# Generated by Django 3.2.4 on 2021-06-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='result',
        ),
        migrations.AddField(
            model_name='student',
            name='faculty_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
