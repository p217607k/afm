# Generated by Django 4.0.5 on 2022-12-08 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempuser',
            name='f_id',
        ),
        migrations.AlterField(
            model_name='tempuser',
            name='d_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.alldevices'),
        ),
    ]