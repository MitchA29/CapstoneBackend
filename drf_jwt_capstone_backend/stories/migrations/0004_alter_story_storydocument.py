# Generated by Django 3.2.8 on 2022-01-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_alter_story_storygenre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='storyDocument',
            field=models.CharField(max_length=100),
        ),
    ]