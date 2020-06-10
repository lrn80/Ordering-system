from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # 留言板
    path('<int:id>/<int:page>.html', board, name='board')
]