# Generated by Django 4.0.6 on 2022-07-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otziv',
            name='phone',
            field=models.CharField(default=90242213, max_length=30),
            preserve_default=False,
        ),
    ]
