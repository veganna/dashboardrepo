# Generated by Django 3.2.5 on 2021-07-18 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbase',
            name='years_old',
            field=models.DateField(blank=True),
        ),
    ]
