# Generated by Django 2.2.6 on 2020-03-16 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthNet', '0014_auto_20200302_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=models.CharField(default='house dust mite', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='body_mass',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='consultation_fee',
            field=models.DecimalField(decimal_places=2, default=3.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='current_medication',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='current_temperature',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default='1966-12-31'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='description_of_the_condition',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email_address',
            field=models.EmailField(default='edwickmvundla@aol.com', max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='employment_status',
            field=models.CharField(choices=[('Not Applicable', 'NOT APPLICABLE'), ('Employed', 'EMPLOYED'), ('Unemployed', 'UNEMPLOYED'), ('Contract Employee', 'CONTRACT EMPLOYEE'), ('Student', 'STUDENT'), ('Retired', 'RETIRED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='Evelyn', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='home_address',
            field=models.CharField(default='9677 University Road, Harrisvale', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='Siziba', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(choices=[('N/A', 'Not Applicable'), ('ENGAGED', 'Engaged'), ('SINGLE', 'Single'), ('DIVORCED', 'Divorced'), ('SEPARATED', 'Separated'), ('MARRIED', 'Married'), ('WIDOWED', 'Widowed')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='national_id',
            field=models.CharField(default='19-5983676P47', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default='+263 77 241 3786', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='title',
            field=models.CharField(blank=True, choices=[('Mr', 'MR.'), ('Mrs', 'MRS.'), ('Ms', 'MS.'), ('Prof', 'PROF.'), ('Dr', 'DR.'), ('Rev', 'REV.')], max_length=10, null=True),
        ),
    ]