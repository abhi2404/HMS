# Generated by Django 2.0 on 2020-06-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('doctor_degree', models.CharField(max_length=10)),
                ('status', models.CharField(default='pending', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
