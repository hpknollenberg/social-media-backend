"""
URL configuration for project_social_media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_social_media.views import *
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', get_profile),
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('create-user/', create_user),
    path('get-messages/', get_messages),
    path('create-message/', create_message),
    path('delete-message/', delete_message),
    path('update-likes/', update_likes),
    path('profile-picture/', update_profile_picture),
    path('other-profile/<int:pk>/', get_other_profile),
    path('create-comment/', create_comment),
    path('get-comments/', get_comments),
    path('delete-comment/', delete_comment),
    path('update-comment-likes/', update_comment_likes)
]

if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
