from django.urls import path
from . import views

urlpatterns = [
    path('', views.our_talents, name='our_talents'),
]