from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.username} {self.phone_number}'

    class Meta:
        app_label = 'metrostandart'
        db_table = 'User'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
