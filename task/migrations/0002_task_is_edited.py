# Generated by Django 4.0 on 2022-01-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
    ]