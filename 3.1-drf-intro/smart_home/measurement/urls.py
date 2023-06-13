from django.urls import path

from measurement.views import SensorListCreateAPIView, MeasurementCreateAPIView, SensorRetrieveAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('sensors/<pk>/', SensorRetrieveAPIView.as_view()),
    path('measur/', MeasurementCreateAPIView.as_view()),
]
