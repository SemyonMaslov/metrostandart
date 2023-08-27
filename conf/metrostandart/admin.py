from django.contrib import admin

from metrostandart.models import Document, MeasuringInstrument, Registry, User


# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    ...


@admin.register(MeasuringInstrument)
class MeasuringInstrumentAdmin(admin.ModelAdmin):
    ...


@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
    list_display = ('number', 'measuring_instrument')
    list_filter = ('measuring_instrument',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...
