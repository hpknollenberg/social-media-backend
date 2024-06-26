# Generated by Django 5.0.6 on 2024-06-06 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social_media', '0013_profile_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_to_comment_set', to='app_social_media.profile')),
                ('likes', models.ManyToManyField(related_name='likes_to_comment', to='app_social_media.profile')),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_to_comment_set', to='app_social_media.message')),
            ],
        ),
    ]
