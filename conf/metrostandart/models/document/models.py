from django.db import models


class Document(models.Model):
    pdf_file = models.FileField(upload_to='pdf/', verbose_name="PDF файлы")
    excel_file = models.FileField(upload_to='excel/', verbose_name="Excel файлы")

    def __str__(self):
        return f'{self.pdf_file} {self.excel_file}'

    class Meta:
        app_label = 'metrostandart'
        db_table = 'Document'
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
