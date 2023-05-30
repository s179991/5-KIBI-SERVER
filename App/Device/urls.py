from django.urls import path
from .views import DeviceConnect, DeviceDisconnect

"""Configuration of http link calls for connecting devices
    /connected -> describes calling the DeviceConnected function from the Device.views module
    /disconnected -> describes calling the DeviceDisconnected function from the Device.views module
"""
urlpatterns = [
    path('connect', DeviceConnect),
    path('disconnect', DeviceDisconnect),
]

