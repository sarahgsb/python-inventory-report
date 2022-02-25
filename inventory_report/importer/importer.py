from abc import ABC, abstractmethod


class Importer(ABC):

    def __init__(self, export_file):
        self.export_file: export_file

    @abstractmethod
    def import_data(self):
        raise NotImplementedError
