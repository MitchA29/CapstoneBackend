# Generated by Django 3.2.8 on 2021-12-29 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='user',
            new_name='clubCreator',
        ),
    ]