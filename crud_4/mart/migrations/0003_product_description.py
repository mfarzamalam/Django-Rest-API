# Generated by Django 4.0 on 2021-12-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]