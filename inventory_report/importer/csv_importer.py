from inventory_report.importer.importer import Importer
from inventory_report.utils.csv_reader import reader_csv


class CsvImporter(Importer):
    def import_data(self):
        if self.endswith('.csv'):
            return reader_csv(self)
        else:
            raise ValueError('Arquivo inválido')
