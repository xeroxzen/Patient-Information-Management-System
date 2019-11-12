# Generated by Django 2.2.6 on 2019-11-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthNet', '0010_auto_20191111_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
