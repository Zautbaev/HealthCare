# Generated by Django 5.1.2 on 2024-10-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
