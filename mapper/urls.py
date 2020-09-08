from django.urls import path
from mapper import views

urlpatterns = [
    path('', views.home, name='home')
]
