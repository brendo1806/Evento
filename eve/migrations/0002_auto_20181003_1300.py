# Generated by Django 2.0.5 on 2018-10-03 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eve', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eve',
            old_name='Nome',
            new_name='nome',
        ),
    ]