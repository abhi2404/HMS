# Generated by Django 2.0 on 2020-06-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0008_auto_20200618_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_appointment',
            name='notification',
            field=models.CharField(default='show', max_length=15),
        ),
    ]
