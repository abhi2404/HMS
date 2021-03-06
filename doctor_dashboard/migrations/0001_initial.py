# Generated by Django 2.0 on 2020-06-19 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient_details', '0008_auto_20200618_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='report_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bp', models.CharField(max_length=20)),
                ('SpO2', models.CharField(max_length=5)),
                ('prescription', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=100, null=True)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient_details.patient_history')),
            ],
        ),
    ]
