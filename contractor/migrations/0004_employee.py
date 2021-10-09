# Generated by Django 3.1 on 2021-10-08 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contractor', '0003_auto_20211008_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=150)),
                ('apprentice', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=150)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=150)),
                ('legall_in_au', models.CharField(max_length=100)),
                ('work_in_ct', models.CharField(max_length=100)),
                ('experience_ct', models.CharField(max_length=100)),
                ('aboriginal', models.CharField(max_length=100)),
                ('islander', models.CharField(max_length=100)),
                ('medical', models.CharField(max_length=100)),
                ('english', models.CharField(max_length=100)),
                ('interpreter', models.CharField(max_length=100)),
                ('em_name', models.CharField(max_length=100)),
                ('em_phone', models.CharField(max_length=30)),
                ('em_relation', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
