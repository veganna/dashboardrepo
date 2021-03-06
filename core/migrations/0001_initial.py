# Generated by Django 3.2.5 on 2021-07-19 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=30)),
                ('client_name', models.CharField(max_length=30)),
                ('work_hours', models.PositiveIntegerField(default=1)),
                ('due_date', models.DateField()),
                ('created_data', models.DateField(auto_now_add=True)),
                ('about_task', models.TextField(blank=True)),
                ('files_link', models.TextField(blank=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]
