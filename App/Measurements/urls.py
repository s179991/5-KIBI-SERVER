from django.urls import path
from . import views

urlpatterns = [
    path('measurement/<str:T>/<str:RH>/<str:p>/<str:P>/<str:O>/<str:CO2>/', views.DeviceMeasurement),
]

