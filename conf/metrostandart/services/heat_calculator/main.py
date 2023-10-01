from PyPDF2 import PdfReader
from django import forms
from service_objects.services import Service

from metrostandart.services.heat_calculator.completion_excel_CTD import CompletionHeatCalculatorCTDService
from metrostandart.services.heat_calculator.completion_excel_TB7 import CompletionHeatCalculatorTB7Service
from metrostandart.services.heat_calculator.completion_excel_TCPB023 import CompletionHeatCalculatorTCPB023Service
from metrostandart.services.heat_calculator.completion_excel_TCPB024 import CompletionHeatCalculatorTCPB024Service
from metrostandart.services.heat_calculator.completion_excel_TCPB024M import CompletionHeatCalculatorTCPB024MService
from metrostandart.services.heat_calculator.completion_excel_TCPB026M import CompletionHeatCalculatorTCPB026MService
from metrostandart.services.heat_calculator.completion_excel_TCPB033 import CompletionHeatCalculatorTCPB033Service
from metrostandart.services.heat_calculator.completion_excel_TCPB034 import CompletionHeatCalculatorTCPB034Service
from metrostandart.services.heat_calculator.completion_excel_TEM104 import CompletionHeatCalculatorTEM104Service
from metrostandart.services.heat_calculator.completion_excel_TEM106 import CompletionHeatCalculatorTEM106Service
from metrostandart.services.heat_calculator.completion_excel_VKT5 import CompletionHeatCalculatorVKT5Service
from metrostandart.services.heat_calculator.completion_excel_VKT7 import CompletionHeatCalculatorVKT7Service
from metrostandart.utils import collection_data

SERVICES_DICT = {
    'ВКТ-7': CompletionHeatCalculatorVKT7Service,
    'ВКТ': CompletionHeatCalculatorVKT5Service,
    'СТД': CompletionHeatCalculatorCTDService,
    'ТВ7': CompletionHeatCalculatorTB7Service,
    'ТСРВ-023': CompletionHeatCalculatorTCPB023Service,
    'ТСРВ-033': CompletionHeatCalculatorTCPB033Service,
    'ТСРВ-034': CompletionHeatCalculatorTCPB034Service,
    'ТСРВ-024': CompletionHeatCalculatorTCPB024Service,
    'ТСРВ-024м': CompletionHeatCalculatorTCPB024MService,
    'ТСРВ-026м': CompletionHeatCalculatorTCPB026MService,
    'ТЭМ-104': CompletionHeatCalculatorTEM104Service,
    'ТЭМ-106': CompletionHeatCalculatorTEM106Service,
}


class MainHeatCalculatorService(Service):
    file = forms.FileField()
    registry = forms.CharField()

    def process(self):
        self.text = PdfReader(self.cleaned_data['file']).pages[
            0].extract_text().replace('\n', ' ').replace('_', '')
        return self.run_service()

    def run_service(self):
        measuring_instrument_type = self.get_measuring_instrument_type
        return SERVICES_DICT[measuring_instrument_type].execute(
            {'registry': self.cleaned_data['registry']},
            {'file': self.cleaned_data['file']}
        )

    @property
    def get_measuring_instrument_type(self):
        data = collection_data(self.text)
        return data['measuring_instrument'].split(';')[-2].split(' ')[-1]
