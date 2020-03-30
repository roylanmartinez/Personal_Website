from django.urls import path
from . import views


urlpatterns = [
    path('', views.numlet, name='num-let'),
    path('ES/', views.numletES, name='num-letES'),
    path('calcular/<typpe>/', views.calcular, name='num-let-c'),
]
