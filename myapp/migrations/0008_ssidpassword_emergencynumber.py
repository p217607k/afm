# Generated by Django 4.0.5 on 2022-12-14 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0007_rename_status1_tempuser_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ssidPassword',
            fields=[
                ('d_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.alldevices')),
                ('ssid1', models.CharField(blank=True, max_length=15, unique=True)),
                ('password1', models.CharField(blank=True, max_length=50)),
                ('ssid2', models.CharField(blank=True, max_length=15, unique=True)),
                ('password2', models.CharField(blank=True, max_length=50)),
                ('ssid3', models.CharField(blank=True, max_length=15, unique=True)),
                ('password3', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='emergencyNumber',
            fields=[
                ('d_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.alldevices')),
                ('number1', models.CharField(max_length=12, null=True)),
                ('number2', models.CharField(max_length=12, null=True)),
                ('number3', models.CharField(max_length=12, null=True)),
                ('number4', models.CharField(max_length=12, null=True)),
                ('number5', models.CharField(max_length=12, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
