from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # 图片墙
    path('<int:id>/<int:page>.html', album, name='album')
]