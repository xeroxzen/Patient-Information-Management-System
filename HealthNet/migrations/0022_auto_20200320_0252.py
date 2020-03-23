# Generated by Django 2.2.6 on 2020-03-20 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthNet', '0021_auto_20200320_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=models.CharField(default='cosmetics', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default='1955-3-25'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email_address',
            field=models.EmailField(default='nondumisomoyo@iCloud.com', max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='Petros', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='home_address',
            field=models.CharField(default='692 State House Ave, Emganwini', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='Nyoni', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='national_id',
            field=models.CharField(default='75-2597095C13', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default='+263 73 893 5414', max_length=30, unique=True),
        ),
    ]
