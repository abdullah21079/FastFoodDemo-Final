# Generated by Django 5.0.4 on 2024-05-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile1', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=16),
        ),
    ]
