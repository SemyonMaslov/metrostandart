import re
from functools import lru_cache

from PyPDF2 import PdfReader
from django import forms
from service_objects.services import Service

from metrostandart.models import Registry
from metrostandart.services.pressure_sensor.completion_excel import CompletionPressureSensorExcelService
from metrostandart.services.thermal_resistance.completion_excel_pt100 import CompletionThermalResistancePT100Service


class MainService(Service):
    file = forms.FileField()

    def process(self):
        self.validate_file_type()
        self.registry_exists()
        return self.run_service()

    def run_service(self):
        measuring_instrument = self.registry_exists().measuring_instrument.name
        if measuring_instrument == 'ДАТЧИК ДАВЛЕНИЯ':
            return CompletionPressureSensorExcelService.execute({'registry': self._get_registry}, {'file': self.cleaned_data['file']})
        elif measuring_instrument == 'ТЕРМОМЕТР СОПРОТИВЛЕНИЯ':
            type = self._get_type_thermal_resistance
            if type == 'Pt100':
                return CompletionThermalResistancePT100Service.execute({'registry': self._get_registry}, {'file': self.cleaned_data['file']})
            elif type == '100П':
                ...


    @property
    @lru_cache()
    def _get_registry(self):
        text = PdfReader(self.cleaned_data['file']).pages[0].extract_text()
        registry = re.findall(r"\d{4,}-\d{2,}", text)[0]
        return registry

    @property
    def _get_type_thermal_resistance(self):
        text = PdfReader(self.cleaned_data['file']).pages[0].extract_text()
        buff = re.findall(r"(?<=сопротивления;).*?(?=\d{4,}-\d{2,})", text)[0]
        type_thermal = buff.replace('Рег. №___наименование и обозначение типа, модификация (при наличии) средства измерений, регистрационный номер в', '')
        return type_thermal.split(';')[-2].split(' ')[-1][1:-1]

    def validate_file_type(self):
        if self.cleaned_data['file'].content_type.split('/')[-1] != 'pdf':
            raise Exception('Неверный тип файла, используйте pdf')

    @lru_cache()
    def registry_exists(self):
        registry = Registry.objects.select_related('measuring_instrument').filter(number=self._get_registry)
        if not registry.exists():
            raise Exception('Номер реестра отсутствует в БД')
        return registry.first()
