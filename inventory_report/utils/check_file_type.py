from inventory_report.utils.csv_reader import reader_csv
from inventory_report.utils.json_reader import reader_json
from inventory_report.utils.xml_reader import reader_xml


def check_file_type(path):
    if path.endswith('.csv'):
        path = reader_csv(path)
        return path
    elif path.endswith('.json'):
        path = reader_json(path)
        return path
    elif path.endswith('.xml'):
        path = reader_xml(path)
        return path
