# необходимые обработчики ( generics APIView классы )
# ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorFullSerializer


# 1,4. Создать датчик. Получить список датчиков
class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# 2,5. Изменить датчик. Получить инфу по конкретному датчику
class SensorRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorFullSerializer


# 3. Добавить измерение
class MeasurementCreateAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
