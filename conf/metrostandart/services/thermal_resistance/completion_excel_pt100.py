import datetime
import os
import re

import openpyxl
import shutil

from django import forms
from service_objects.services import Service
from PyPDF2 import PdfReader

from conf.settings import BASE_DIR
from metrostandart.models import Document


class CompletionThermalResistancePT100Service(Service):
    file = forms.FileField()
    registry = forms.CharField()

    def process(self):
        self.coppy_excel_file()
        self.completion_excel_file()
        self._create_document()
        return self.cleaned_data['path']

    def coppy_excel_file(self):
        source_path = os.path.join(BASE_DIR, 'data\\pressure_sensor\\Преобразователь давления пустой в.3.xlsx')
        self.cleaned_data['path'] = os.path.join(BASE_DIR,
                                                 f"uploads\\pressure_sensor\\pressure_sensor_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx")
        shutil.copy(source_path, self.cleaned_data['path'])

    def completion_excel_file(self):
        book = openpyxl.open(self.cleaned_data['path'])
        sheet = book.active
        data = self.colection_data
        sheet['C5'].value = data['verification']
        sheet['G5'].value = data['date'][1]
        sheet['E6'].value = data['measuring_instrument']
        sheet['C7'].value = data['factory_number']
        sheet['H7'].value = data['registry']
        sheet['D9'].value = data['accordance']
        sheet['C14'].value = data['facts']
        sheet['E36'].value = data['verification']
        sheet['C38'].value = data['verifier']
        book.save(self.cleaned_data['path'])

    @property
    def colection_data(self):
        text = PdfReader(self.cleaned_data['file']).pages[0].extract_text()
        data = {
            'date': re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text),
            'verification': re.findall(r"(?<=СВИДЕТЕЛЬСТВО О ПОВЕРКЕ).*?(?=\nДействительно)", text)[0][1:],
            'verifier': re.findall(r"(?<=Поверитель ).*?(?=_)", text)[0],
            'measuring_instrument': re.findall(r"(?<=; ).*?(?=Рег)", text)[0].split(";")[-2].strip(),
            'registry': self.cleaned_data['registry'],
            'factory_number': re.findall(r"(?<=заводской номер).*?(?=_)", text)[0],
            'accordance': re.findall(r"(?<=в соответствии с).*?(?=_)", text)[0],
            'facts': re.findall(r"(?<=факторов:).*?(?=_)", text)[0].strip(),
        }
        return data

    def _create_document(self):
        return Document.objects.create(
            pdf_file=self.cleaned_data['file'],
            excel_file=self.cleaned_data['path']
        )
