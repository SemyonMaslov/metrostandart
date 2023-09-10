from PyPDF2 import PdfReader
from django import forms
from service_objects.services import Service

from metrostandart.services.gas_meter.completion_excel_G10 import (
    CompletionGasMeterG10Service
)
from metrostandart.services.gas_meter.completion_excel_G16 import (
    CompletionGasMeterG16Service
)
from metrostandart.services.gas_meter.completion_excel_G25 import (
    CompletionGasMeterG25Service
)
from metrostandart.services.gas_meter.completion_excel_G4 import (
    CompletionGasMeterG4Service
)
from metrostandart.services.gas_meter.completion_excel_G6 import (
    CompletionGasMeterG6Service
)
from metrostandart.utils import collection_data

SERVICES_DICT = {
    'G4': CompletionGasMeterG4Service,
    'G6': CompletionGasMeterG6Service,
    'G10': CompletionGasMeterG10Service,
    '1,6': CompletionGasMeterG16Service,
    '2,5': CompletionGasMeterG25Service,
}


class MainGasMeterService(Service):
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
        measuring_instrument = data['measuring_instrument'].split(';')[-2]
        if ' ' in measuring_instrument[1:]:
            return measuring_instrument.split(' ')[-1]
        return measuring_instrument.split('-')[-1]
