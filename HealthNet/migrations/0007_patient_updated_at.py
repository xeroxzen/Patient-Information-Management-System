# Generated by Django 2.2.6 on 2019-11-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthNet', '0006_auto_20191110_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]