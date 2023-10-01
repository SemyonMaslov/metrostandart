from django import forms
from service_objects.services import Service

from metrostandart.services.heat_meter.completion_excel import CompletionHeatMeterService
from metrostandart.services.heat_meter.completion_excel_2811204 import CompletionHeatMeter2811204Service
from metrostandart.services.heat_meter.completion_excel_2811209 import CompletionHeatMeter2811209Service
from metrostandart.services.heat_meter.completion_excel_2811214 import CompletionHeatMeter2811214Service
from metrostandart.services.heat_meter.completion_excel_3872308 import CompletionHeatMeter3872308Service
from metrostandart.services.heat_meter.completion_excel_4502410 import CompletionHeatMeter45024410Service
from metrostandart.services.heat_meter.completion_excel_4931812 import CompletionHeatMeter4931812Service
from metrostandart.services.heat_meter.completion_excel_5544013 import CompletionHeatMeter5544013Service
from metrostandart.services.heat_meter.completion_excel_5545713 import CompletionHeatMeter5545713Service
from metrostandart.services.heat_meter.completion_excel_5800314 import CompletionHeatMeter5800314Service
from metrostandart.services.heat_meter.completion_excel_6309316 import CompletionHeatMeter6309316Service
from metrostandart.services.heat_meter.completion_excel_6549816 import CompletionHeatMeter6549816Service
from metrostandart.services.heat_meter.completion_excel_7181218 import CompletionHeatMeter7181218Service

SERVICE_DICT = {
    '28112-04': CompletionHeatMeter2811204Service,
    '28112-09': CompletionHeatMeter2811209Service,
    '28112-14': CompletionHeatMeter2811214Service,
    '38723-08 61983-15 61877-15 25335-13 25335-03 25335-08': CompletionHeatMeter3872308Service,
    '45024-10 71374-18 65782-16 78403-20': CompletionHeatMeter45024410Service,
    '49318-12': CompletionHeatMeter4931812Service,
    '55440-13 65137-16': CompletionHeatMeter5544013Service,
    '55457-13': CompletionHeatMeter5545713Service,
    '58003-14': CompletionHeatMeter5800314Service,
    '63093-16 61496-15': CompletionHeatMeter6309316Service,
    '65498-16': CompletionHeatMeter6549816Service,
    '71812-18 65853-16 63444-16 66855-17 58595-14': CompletionHeatMeter7181218Service
}


class MainHeatMeterService(Service):
    file = forms.FileField()
    registry = forms.CharField()

    def process(self):
        return self.run_service()

    def run_service(self):
        for key in SERVICE_DICT.keys():
            if self.cleaned_data['registry'] in key:
                return SERVICE_DICT[key].execute(
                    {'registry': self.cleaned_data['registry']},
                    {'file': self.cleaned_data['file']}
                )
                break
        return CompletionHeatMeterService.execute(
            {'registry': self.cleaned_data['registry']},
            {'file': self.cleaned_data['file']}
        )
