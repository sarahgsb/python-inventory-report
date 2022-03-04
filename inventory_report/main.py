from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

import sys


def main():
    obj = None

    if len(sys.argv) == 3:
        path = sys.argv[1]
        report_type = sys.argv[2]
        if path.endswith('.csv'):
            obj = InventoryRefactor(CsvImporter)
        elif path.endswith('.json'):
            obj = InventoryRefactor(JsonImporter)
        elif path.endswith('.xml'):
            obj = InventoryRefactor(XmlImporter)
        return print(obj.import_data(path, report_type), end="")
    else:
        sys.stderr.write('Verifique os argumentos\n')
