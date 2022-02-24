from utils.csv_reader import serialize_csv
from abc import ABC
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory(ABC):
    def __init__(self, report, type):
        self.report = serialize_csv(report)
        self.type = type

    def import_data(self):
        if self.type == 'simples':
            return SimpleReport.generate(self.report)
        else:
            return CompleteReport.generate(self.report)
