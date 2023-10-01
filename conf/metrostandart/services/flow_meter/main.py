from PyPDF2 import PdfReader
from django import forms
from service_objects.services import Service

from metrostandart.services.flow_meter.piterflow.completion_excel_D100 import CompletionFlowMeterD100Piterflow4Service
from metrostandart.services.flow_meter.piterflow.completion_excel_D15 import CompletionFlowMeterD15Piterflow4Service
from metrostandart.services.flow_meter.piterflow.completion_excel_D20 import CompletionFlowMeterD20Piterflow4Service
from metrostandart.services.flow_meter.piterflow.completion_excel_D32 import CompletionFlowMeterD32Piterflow4Service
from metrostandart.services.flow_meter.piterflow.completion_excel_D40 import CompletionFlowMeterD40Piterflow4Service
from metrostandart.services.flow_meter.piterflow.completion_excel_D50 import CompletionFlowMeterD50Piterflow4Service
from metrostandart.services.flow_meter.piterflow.completion_excel_D65 import CompletionFlowMeterD65Piterflow4Service
from metrostandart.services.flow_meter.piterflow.completion_excel_D80 import CompletionFlowMeterD80Piterflow4Service
from metrostandart.services.flow_meter.pramer.completion_excel_D100 import CompletionFlowMeterD100Pramer4Service
from metrostandart.services.flow_meter.pramer.completion_excel_D15 import CompletionFlowMeterD15Pramer4Service
from metrostandart.services.flow_meter.pramer.completion_excel_D20 import CompletionFlowMeterD20Pramer4Service
from metrostandart.services.flow_meter.pramer.completion_excel_D25 import CompletionFlowMeterD25Pramer4Service
from metrostandart.services.flow_meter.pramer.completion_excel_D32 import CompletionFlowMeterD32Pramer4Service
from metrostandart.services.flow_meter.pramer.completion_excel_D40 import CompletionFlowMeterD40Pramer4Service
from metrostandart.services.flow_meter.pramer.completion_excel_D50 import CompletionFlowMeterD50Pramer4Service
from metrostandart.services.flow_meter.pramer.completion_excel_D65 import CompletionFlowMeterD65Pramer4Service
from metrostandart.services.flow_meter.pramer.completion_excel_D80 import CompletionFlowMeterD80Pramer4Service
from metrostandart.services.flow_meter.prem.completion_excel_D100 import CompletionFlowMeterD100Prem4Service
from metrostandart.services.flow_meter.prem.completion_excel_D15 import CompletionFlowMeterD15Prem4Service
from metrostandart.services.flow_meter.prem.completion_excel_D20 import CompletionFlowMeterD20Prem4Service
from metrostandart.services.flow_meter.prem.completion_excel_D32 import CompletionFlowMeterD32Prem4Service
from metrostandart.services.flow_meter.prem.completion_excel_D40 import CompletionFlowMeterD40Prem4Service
from metrostandart.services.flow_meter.prem.completion_excel_D50 import CompletionFlowMeterD50Prem4Service
from metrostandart.services.flow_meter.prem.completion_excel_D65 import CompletionFlowMeterD65Prem4Service
from metrostandart.services.flow_meter.prem.completion_excel_D80 import CompletionFlowMeterD80Prem4Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D10 import CompletionFlowMeterVzletD10Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D15 import CompletionFlowMeterVzletD15Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D20 import CompletionFlowMeterVzletD20Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D25 import CompletionFlowMeterVzletD25Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D32 import CompletionFlowMeterVzletD32Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D40 import CompletionFlowMeterVzletD40Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D50 import CompletionFlowMeterVzletD50Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D65 import CompletionFlowMeterVzletD65Service
from metrostandart.services.flow_meter.vzlet.completion_excel_D80 import CompletionFlowMeterVzletD80Service
from metrostandart.utils import collection_data

VZLET = 'ВЗЛЁТ'

PRAMER = 'ПРАМЕР'

PITERFLOW = 'ПИТЕРФЛОУ'

PREM = 'ПРЭМ'

DY_LIST = ['ДУ-10', 'ДУ-15', 'ДУ-20', 'ДУ-25', 'ДУ-32', 'ДУ-40', 'ДУ-50',
           'ДУ-65', 'ДУ-80', 'ДУ-100']

FLOWMETER_LIST = [VZLET, PITERFLOW, PREM, PRAMER]

SERVICES_DICT = {
    VZLET: {
        'ДУ-10': CompletionFlowMeterVzletD10Service,
        'ДУ-15': CompletionFlowMeterVzletD15Service,
        'ДУ-20': CompletionFlowMeterVzletD20Service,
        'ДУ-25': CompletionFlowMeterVzletD25Service,
        'ДУ-32': CompletionFlowMeterVzletD32Service,
        'ДУ-40': CompletionFlowMeterVzletD40Service,
        'ДУ-50': CompletionFlowMeterVzletD50Service,
        'ДУ-65': CompletionFlowMeterVzletD65Service,
        'ДУ-80': CompletionFlowMeterVzletD80Service,
    },
    PRAMER: {
        'ДУ-15': CompletionFlowMeterD15Pramer4Service,
        'ДУ-20': CompletionFlowMeterD20Pramer4Service,
        'ДУ-25': CompletionFlowMeterD25Pramer4Service,
        'ДУ-32': CompletionFlowMeterD32Pramer4Service,
        'ДУ-40': CompletionFlowMeterD40Pramer4Service,
        'ДУ-50': CompletionFlowMeterD50Pramer4Service,
        'ДУ-65': CompletionFlowMeterD65Pramer4Service,
        'ДУ-80': CompletionFlowMeterD80Pramer4Service,
        'ДУ-100': CompletionFlowMeterD100Pramer4Service
    },
    PITERFLOW: {
        'ДУ-15': CompletionFlowMeterD15Piterflow4Service,
        'ДУ-20': CompletionFlowMeterD20Piterflow4Service,
        'ДУ-32': CompletionFlowMeterD32Piterflow4Service,
        'ДУ-40': CompletionFlowMeterD40Piterflow4Service,
        'ДУ-50': CompletionFlowMeterD50Piterflow4Service,
        'ДУ-65': CompletionFlowMeterD65Piterflow4Service,
        'ДУ-80': CompletionFlowMeterD80Piterflow4Service,
        'ДУ-100': CompletionFlowMeterD100Piterflow4Service,
    },
    PREM: {
        'ДУ-15': CompletionFlowMeterD15Prem4Service,
        'ДУ-20': CompletionFlowMeterD20Prem4Service,
        'ДУ-32': CompletionFlowMeterD32Prem4Service,
        'ДУ-40': CompletionFlowMeterD40Prem4Service,
        'ДУ-50': CompletionFlowMeterD50Prem4Service,
        'ДУ-65': CompletionFlowMeterD65Prem4Service,
        'ДУ-80': CompletionFlowMeterD80Prem4Service,
        'ДУ-100': CompletionFlowMeterD100Prem4Service,
    }
}


class MainFlowMeterService(Service):
    file = forms.FileField()
    registry = forms.CharField()

    def process(self):
        self.text = PdfReader(
            self.cleaned_data['file']
        ).pages[0].extract_text().replace('\n', ' ').replace('_', '')
        return self.run_service()

    def run_service(self):
        data = collection_data(self.text)
        measuring_instrument = data['measuring_instrument']
        for item in FLOWMETER_LIST:
            if item in measuring_instrument.upper():
                for element in DY_LIST:
                    if element in measuring_instrument.upper():
                        return SERVICES_DICT[item][element].execute(
                            {'registry': self.cleaned_data['registry']},
                            {'file': self.cleaned_data['file']}
                        )
                        break
