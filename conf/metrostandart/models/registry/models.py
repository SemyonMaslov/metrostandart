from django.db import models


class Registry(models.Model):
    number = models.CharField(max_length=30, verbose_name='Номер реестра')
    measuring_instrument = models.ForeignKey('MeasuringInstrument', on_delete=models.CASCADE, verbose_name='Средство измерения')

    def __str__(self):
        return self.number

    class Meta:
        app_label = 'metrostandart'
        db_table = 'Registry'
        verbose_name = 'Номер реестра'
        verbose_name_plural = 'Номера реестра'
