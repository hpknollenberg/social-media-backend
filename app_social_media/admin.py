from django.contrib import admin
from app_social_media.models import *

class ProfileAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)