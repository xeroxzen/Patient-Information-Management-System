# Generated by Django 2.2.6 on 2019-11-19 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'ordering': ('-username',), 'verbose_name_plural': 'Admin'},
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='identification_id',
            new_name='unique_id',
        ),
    ]
