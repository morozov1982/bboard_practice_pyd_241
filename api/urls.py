from django.urls import path

from api.views import bbs

urlpatterns = [
    path('bbs/', bbs),
]
