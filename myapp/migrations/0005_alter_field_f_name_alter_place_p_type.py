# Generated by Django 4.0.8 on 2022-10-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_field_id_place_id_alter_field_f_id_alter_place_p_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='f_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='place',
            name='p_type',
            field=models.CharField(max_length=15),
        ),
    ]
