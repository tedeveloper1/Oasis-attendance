# Generated by Django 5.0.4 on 2024-07-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_team_address_alter_team_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]