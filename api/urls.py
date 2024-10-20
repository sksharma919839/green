from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

servicerouter = DefaultRouter()
servicerouter.register(r"service", serviceView, basename="service")

urlpatterns = [path("", include(servicerouter.urls))]
