# Generated by Django 3.2.5 on 2022-07-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
