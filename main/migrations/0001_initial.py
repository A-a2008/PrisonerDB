# Generated by Django 5.0.1 on 2024-01-26 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FIR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fir_number', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('date_of_registration', models.DateField()),
                ('ps_id_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prisoner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('mobile_numbers', models.TextField(help_text='Enter mobile numbers, separated by commas')),
                ('email', models.EmailField(max_length=254)),
                ('join_date', models.DateField()),
                ('duration', models.CharField(max_length=100)),
                ('exit_date', models.DateField()),
                ('ward', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bar_no', models.CharField(max_length=100)),
                ('prisoners', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prisoners', to='main.prisoner')),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_type', models.CharField(max_length=200)),
                ('crime_location', models.CharField(max_length=200)),
                ('crime_date', models.DateField()),
                ('fir', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fir', to='main.fir')),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crimes', to='main.prisoner')),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court_name', models.CharField(max_length=100)),
                ('court_location', models.CharField(max_length=200)),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courts', to='main.prisoner')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('log_in_time', models.DateTimeField()),
                ('log_out_time', models.DateTimeField()),
                ('prisoner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visitor', to='main.prisoner')),
            ],
        ),
    ]
