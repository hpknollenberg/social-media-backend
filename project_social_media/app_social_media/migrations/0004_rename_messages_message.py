# Generated by Django 5.0.6 on 2024-06-04 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_social_media', '0003_messages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
    ]