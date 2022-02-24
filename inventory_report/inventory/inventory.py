from abc import ABC
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.utils.check_file_type import check_file_type


class Inventory(ABC):
    def import_data(path, type):
        if type == 'simples':
            return SimpleReport.generate(check_file_type(path))
        else:
            return CompleteReport.generate(check_file_type(path))
