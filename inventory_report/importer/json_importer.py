from inventory_report.importer.importer import Importer
from inventory_report.utils.json_reader import reader_json


class JsonImporter(Importer):
    def import_data(self):
        if self.endswith('.json'):
            return reader_json(self)
        else:
            raise ValueError('Arquivo inválido')
