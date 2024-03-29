# Generated by Django 2.2.6 on 2020-03-17 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthNet', '0019_auto_20200317_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=models.CharField(default='Milk', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default='2010-3-29'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email_address',
            field=models.EmailField(default='siphomarara@gmail.com', max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='Melody', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='home_address',
            field=models.CharField(default='459 Norwark Road, Emganwini', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='Sikhosana', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='national_id',
            field=models.CharField(default='86-6730350K36', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default='+263 77 375 2510', max_length=30, unique=True),
        ),
    ]
