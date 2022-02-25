from inventory_report.importer.importer import Importer
from inventory_report.utils.xml_reader import reader_xml


class XmlImporter(Importer):
    def import_data(self):
        if self.endswith('.xml'):
            return reader_xml(self)
        else:
            raise ValueError('Arquivo inválido')
