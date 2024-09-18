from .views import CarsAPIView
from django.urls import path

urlpatterns = [
  path('api/v1/',CarsAPIView.as_view()),
 ]
