import xml.etree.ElementTree as ET


class XMLParser:
    def __init__(self, file):
        self.root = None
        if file:
            tree = ET.parse(file)
            self.root = tree.getroot()

    def get_element_text(self, element):
        results = self.root.iter(element)
        ret = []
        for child in results:
            ret.append(child.text)
        return ret

    def get_attr_list_from_element(self, element):
        results = self.root.iter(element)
        ret = []
        for child in results:
            ret.append(child.attrib)
        return ret

    @staticmethod
    def get_attr_from_element(element, attr):
        if attr in element:
            return element[attr]
        raise Exception("attr cannot be found")

