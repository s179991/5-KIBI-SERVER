from django.urls import path
from . import views

urlpatterns = [
    path('log/<str:level>/<str:text>/', views.RegisterLog),
]

