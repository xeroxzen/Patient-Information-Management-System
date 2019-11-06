# Generated by Django 2.2.6 on 2019-11-06 01:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(default='Dr', max_length=6)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('qualification', models.CharField(max_length=60)),
                ('specialty', models.CharField(max_length=60)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='HealthNet.Doctor')),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=10)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=12)),
                ('date_of_birth', models.DateField()),
                ('home_address', models.CharField(max_length=255)),
                ('national_id', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('purpose_of_visit', models.CharField(max_length=255)),
                ('description_of_the_condition', models.TextField()),
                ('prescription', models.CharField(max_length=255)),
                ('current_temperature', models.CharField(max_length=255)),
                ('blood_type', models.CharField(choices=[('A+', 'A+ Type'), ('B+', 'B+ Type'), ('AB+', 'AB+ Type'), ('O+', 'O+ Type'), ('A-', 'A- Type'), ('B-', 'B- Type'), ('AB-', 'AB- Type'), ('O-', 'O- Type')], max_length=255)),
                ('current_medication', models.CharField(max_length=255)),
                ('body_mass', models.CharField(max_length=255)),
                ('allergies', models.CharField(max_length=255)),
                ('employment_status', models.CharField(max_length=20)),
                ('marital_status', models.CharField(choices=[(0, 'Not Applicable'), (1, 'Engaged'), (2, 'Single'), (3, 'Divorced'), (4, 'Separated'), (5, 'Married')], max_length=20)),
                ('medical_aid_group', models.CharField(choices=[(0, 'N/A'), (1, 'MASCA'), (2, 'NUST Medical AID'), (3, 'Humana'), (4, 'Premier Services'), (5, 'PSMAS'), (6, 'Emergency 24'), (7, 'Emblem Healthcare'), (8, 'ZimAid'), (9, 'Kaiser Permanente'), (10, 'Wellpoint')], max_length=255)),
                ('date_of_visit', models.DateField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('consulted_doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor', to='HealthNet.Doctor')),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
        ),
    ]
