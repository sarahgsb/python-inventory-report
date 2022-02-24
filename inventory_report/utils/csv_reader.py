import csv


def serialize_csv(path):
    with open(path) as file:
        csv_reader = csv.DictReader(file, delimiter=",")
        csv_content = []
        for row in csv_reader:
            csv_content.append(row)
    return csv_content
