from django.urls import path

from measurement.views import SensorListCreateAPIView, SensorRetrieveAPIView, MeasurementCreateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('sensors/<pk>/', SensorRetrieveAPIView.as_view()),
    path('measur/', MeasurementCreateAPIView.as_view()),
]
