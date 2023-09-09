from django import forms
from service_objects.services import Service

from metrostandart.services.heat_meter.completion_excel import (
    CompletionHeatMeterService
)
from metrostandart.services.heat_meter.completion_excel_2811204 import (
    CompletionHeatMeter2811204Service
)
from metrostandart.services.heat_meter.completion_excel_2811209 import (
    CompletionHeatMeter2811209Service
)
from metrostandart.services.heat_meter.completion_excel_2811214 import (
    CompletionHeatMeter2811214Service
)
from metrostandart.services.heat_meter.completion_excel_3872308 import (
    CompletionHeatMeter3872308Service
)
from metrostandart.services.heat_meter.completion_excel_4502410 import (
    CompletionHeatMeter45024410Service
)
from metrostandart.services.heat_meter.completion_excel_4931812 import (
    CompletionHeatMeter4931812Service
)
from metrostandart.services.heat_meter.completion_excel_5544013 import (
    CompletionHeatMeter5544013Service
)
from metrostandart.services.heat_meter.completion_excel_5545713 import (
    CompletionHeatMeter5545713Service
)
from metrostandart.services.heat_meter.completion_excel_5800314 import (
    CompletionHeatMeter5800314Service
)
from metrostandart.services.heat_meter.completion_excel_6309316 import (
    CompletionHeatMeter6309316Service
)
from metrostandart.services.heat_meter.completion_excel_6549816 import (
    CompletionHeatMeter6549816Service
)
from metrostandart.services.heat_meter.completion_excel_7181218 import (
    CompletionHeatMeter7181218Service
)


class MainHeatMeterService(Service):
    file = forms.FileField()
    registry = forms.CharField()

    def process(self):
        return self.run_service()

    def run_service(self):
        if self.cleaned_data['registry'] == '28112-04':
            return CompletionHeatMeter2811204Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] == '28112-09':
            return CompletionHeatMeter2811209Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] == '28112-14':
            return CompletionHeatMeter2811214Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] in ['38723-08', '61983-15',
                                               '61877-15', '25335-13',
                                               '25335-03', '25335-08']:
            return CompletionHeatMeter3872308Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] in ['45024-10', '71374-18',
                                               '65782-16', '78403-20']:
            return CompletionHeatMeter45024410Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] == '49318-12':
            return CompletionHeatMeter4931812Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] in ['55440-13', '65137-16']:
            return CompletionHeatMeter5544013Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] == '55457-13':
            return CompletionHeatMeter5545713Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] == '58003-14':
            return CompletionHeatMeter5800314Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] in ['63093-16', '61496-15']:
            return CompletionHeatMeter6309316Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] == '65498-16':
            return CompletionHeatMeter6549816Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        elif self.cleaned_data['registry'] in ['71812-18', '65853-16',
                                               '63444-16', '66855-17',
                                               '58595-14']:
            return CompletionHeatMeter7181218Service.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
        else:
            return CompletionHeatMeterService.execute(
                {'registry': self.cleaned_data['registry']},
                {'file': self.cleaned_data['file']}
            )
