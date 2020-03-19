from django.urls import path
from . import views


urlpatterns = [
    path('', views.numlet, name='num-let'),
]
