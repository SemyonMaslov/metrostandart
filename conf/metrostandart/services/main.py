import re
from functools import lru_cache

from PyPDF2 import PdfReader
from django import forms
from service_objects.services import Service

from metrostandart.models import Registry
from metrostandart.services.flow_meter.main import MainFlowMeterService
from metrostandart.services.gas_meter.main import MainGasMeterService
from metrostandart.services.heat_calculator.main import MainHeatCalculatorService
from metrostandart.services.heat_meter.main import MainHeatMeterService
from metrostandart.services.pressure_gauge.completion_excel import CompletionPressureGaugeExcelService
from metrostandart.services.pressure_sensor.completion_excel import CompletionPressureSensorExcelService
from metrostandart.services.thermal_resistance.completion_excel_100p import CompletionThermalResistance100PService
from metrostandart.services.thermal_resistance.completion_excel_pt100 import CompletionThermalResistancePT100Service

SERVICES_DICT = {
    'ДАТЧИК ДАВЛЕНИЯ': CompletionPressureSensorExcelService,
    'ТЕРМОМЕТР СОПРОТИВЛЕНИЯ': {
        'Pt100': CompletionThermalResistancePT100Service,
        '100П': CompletionThermalResistance100PService,
    },
    'МАНОМЕТРЫ': CompletionPressureGaugeExcelService,
    'ТЕПЛОСЧЕТЧИК': MainHeatMeterService,
    'ТЕПЛОВЫЧИСЛИТЕЛЬ': MainHeatCalculatorService,
    'СЧЕТЧИК ГАЗА': MainGasMeterService,
    'РАСХОДОМЕР': MainFlowMeterService
}


class MainService(Service):
    file = forms.FileField()

    def process(self):
        self.validate_file_type()
        self.text = PdfReader(self.cleaned_data['file']).pages[
            0].extract_text().replace('\n', ' ').replace('_', '')
        self.registry_exists()
        return self.run_service()

    def run_service(self):
        measuring_instrument = self.registry_exists().measuring_instrument.name
        if measuring_instrument == 'ТЕРМОМЕТР СОПРОТИВЛЕНИЯ':
            type_of_measuring_instrument = self._get_type_thermal_resistance
            return SERVICES_DICT[measuring_instrument][
                type_of_measuring_instrument].execute(
                {'registry': self._get_registry},
                {'file': self.cleaned_data['file']}
            )
        else:
            return SERVICES_DICT[measuring_instrument].execute(
                {'registry': self._get_registry},
                {'file': self.cleaned_data['file']}
            )

    @property
    @lru_cache()
    def _get_registry(self):
        registry = re.findall(r"\d{4,}-\d{2,}", self.text)[0]
        return registry

    @property
    def _get_type_thermal_resistance(self):
        buff = re.findall(r"(?<=;).*?(?=Рег)", self.text)[0]
        type_thermal = buff.replace(
            'наименование и обозначение типа, модификация (при наличии) средства измерений, регистрационный номер в',
            '')
        return type_thermal.split(';')[-2].split(' ')[-1][1:-1]

    def validate_file_type(self):
        if self.cleaned_data['file'].content_type.split('/')[-1] != 'pdf':
            raise Exception('Неверный тип файла, используйте pdf')

    @lru_cache()
    def registry_exists(self):
        registry = Registry.objects.select_related(
            'measuring_instrument').filter(number=self._get_registry)
        if not registry.exists():
            raise Exception('Номер реестра отсутствует в БД')
        return registry.first()
