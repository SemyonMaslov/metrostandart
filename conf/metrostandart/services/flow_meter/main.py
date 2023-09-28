from PyPDF2 import PdfReader
from django import forms
from service_objects.services import Service

from metrostandart.services.flow_meter.pramer.completion_excel_D25 import \
    CompletionFlowMeterD25Pramer4Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D10 import \
    CompletionFlowMeterVzletD104Service
from metrostandart.utils import collection_data

VZLET = 'ВЗЛЁТ'

PRAMER = 'ПРАМЕР'

VZLET_LIST = ['ДУ-10', 'ДУ-15', 'ДУ-20', 'ДУ-25', 'ДУ-32', 'ДУ-40', 'ДУ-50',
              'ДУ-65', 'ДУ-60']

FLOWMETER_LIST = [VZLET, 'ПИТЕРФЛОУ', 'ПРЭМ', PRAMER]

SERVICES_DICT = {
    VZLET: {
        'ДУ-10': CompletionFlowMeterVzletD104Service
    },
    PRAMER: {
        'ДУ-25': CompletionFlowMeterD25Pramer4Service
    }
}


class MainFlowMeterService(Service):
    file = forms.FileField()
    registry = forms.CharField()

    def process(self):
        self.text = PdfReader(self.cleaned_data['file']).pages[
            0].extract_text().replace('\n', ' ').replace('_', '')
        return self.run_service()

    def run_service(self):
        data = collection_data(self.text)
        measuring_instrument = data['measuring_instrument'].split(';')[-2]
        for item in FLOWMETER_LIST:
            if item in measuring_instrument.upper():
                for element in VZLET_LIST:
                    if element in measuring_instrument.upper():
                        return SERVICES_DICT[item][element].execute(
                            {'registry': self.cleaned_data['registry']},
                            {'file': self.cleaned_data['file']}
                        )
                        break
