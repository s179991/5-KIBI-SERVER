from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Dashboard.urls')),
    path('admin', admin.site.urls, name='admin'),

    path('device/', include('Device.urls')),
    path('device/', include('Measurements.urls')),
    path('device/', include('Logs.urls')),
    path('docs', include('docs.urls')),
]
