from django.db import models


# модели датчика (Sensor) и измерения (Measurement)

#  Датчики
class Sensor(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=128,
        verbose_name='Описание',
        blank=True,
    )

    class Meta:
        db_table = "sensor"
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['id']

    def __str__(self):
        return str(f'{self.id}: {self.name}')


#  Измерения
class Measurement(models.Model):
    sensor_id = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        verbose_name='№ датчика',
        related_name='measurements',
    )
    temperature = models.SmallIntegerField(verbose_name='Температура')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        db_table = "measurement"
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['date']

    def __str__(self):
        return str(f'{self.sensor_id}: {self.temperature}°C | {self.date}')
