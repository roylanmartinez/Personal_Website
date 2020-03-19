from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pag-en'),
    path('es/', views.homees, name='pag-es')
]