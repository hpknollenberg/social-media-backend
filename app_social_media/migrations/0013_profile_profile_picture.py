# Generated by Django 5.0.6 on 2024-06-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social_media', '0012_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
