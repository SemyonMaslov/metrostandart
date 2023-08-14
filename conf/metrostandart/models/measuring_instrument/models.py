from django.db import models


class MeasuringInstrument(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название средства измерения')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'metrostandart'
        db_table = 'MeasuringInstrument'
        verbose_name = 'Средство измерений'
        verbose_name_plural = 'Средства измерений'
