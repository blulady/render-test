# Generated by Django 3.1 on 2020-09-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_registrationtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], max_length=20),
        ),
    ]
