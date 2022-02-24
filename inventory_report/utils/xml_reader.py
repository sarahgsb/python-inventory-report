from xml.etree import cElementTree as ET


def reader_xml(path):
    with open(path) as file:
        tree = ET.parse(file)
        root = tree.getroot()
        xml_content = []

        for child in root:
            product = {}
            for element in child:
                product[element.tag] = element.text
            xml_content.append(product)
    return xml_content
