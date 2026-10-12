
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_mpiangona, name='liste_mpiangona'),
]