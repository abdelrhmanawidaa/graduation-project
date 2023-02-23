from django.urls import path
from . import views




urlpatterns = [
path('', views.home, name='home'),
path('early-result/', views.result, name='early-result'),
#path('scan-result/', views.scan11, name='scan-result'),
path('scan/', views.scan, name='scan'),
]