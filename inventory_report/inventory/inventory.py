from abc import ABC
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.utils.csv_reader import reader_csv


class Inventory(ABC):
    def import_data(path, type):
        if type == 'simples':
            return SimpleReport.generate(reader_csv(path))
        else:
            return CompleteReport.generate(reader_csv(path))
