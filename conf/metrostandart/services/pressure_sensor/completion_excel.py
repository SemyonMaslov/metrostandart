import datetime
import os

import openpyxl
import shutil

from django import forms
from service_objects.services import Service
from PyPDF2 import PdfReader

from metrostandart.models import Document
from metrostandart.utils import collection_data


class CompletionPressureSensorExcelService(Service):
    file = forms.FileField()
    registry = forms.CharField()

    def process(self):
        self.text = PdfReader(self.cleaned_data['file']).pages[
            0].extract_text().replace('\n', ' ').replace('_', '')
        self.coppy_excel_file()
        self.completion_excel_file()
        self._create_document()
        return self.cleaned_data['path']

    def coppy_excel_file(self):
        source_path = os.path.join(os.path.dirname(__file__), '..', '..', '..',
                                   'data', 'pressure_sensor',
                                   'Преобразователь давления пустой в.3.xlsx')
        self.cleaned_data['path'] = os.path.join(os.path.dirname(__file__),
                                                 '..', '..', '..', 'uploads',
                                                 'pressure_sensor',
                                                 f'pressure_sensor{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.xlsx',
                                                 )
        shutil.copy(source_path, self.cleaned_data['path'])

    def completion_excel_file(self):
        book = openpyxl.open(self.cleaned_data['path'])
        sheet = book.active
        data = collection_data(self.text)
        sheet['C5'].value = data['verification']
        sheet['G5'].value = data['date'][1]
        sheet['E6'].value = data['measuring_instrument']
        sheet['C7'].value = data['factory_number']
        sheet['H7'].value = self.cleaned_data['registry']
        sheet['D9'].value = data['accordance']
        sheet['C14'].value = data['facts']
        sheet['E36'].value = data['verification']
        sheet['C38'].value = data['verifier']
        book.save(self.cleaned_data['path'])

    def _create_document(self):
        return Document.objects.create(
            pdf_file=self.cleaned_data['file'],
            excel_file=self.cleaned_data['path']
        )
