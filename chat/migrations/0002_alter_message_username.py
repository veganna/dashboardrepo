# Generated by Django 3.2.5 on 2021-07-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
