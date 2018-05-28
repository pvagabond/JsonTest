from parsers import xml_parser
from os import listdir
from os.path import isfile, join


def parse_xml(file_name, print_result=False):
    xp = xml_parser.XMLParser(file_name)
    prefix = "{http://microsoft.com/schemas/VisualStudio/TeamTest/2010}"
    attr = "outcome"
    elements = xp.get_attr_list_from_element("{0}{1}".format(prefix, "UnitTestResult"))
    for element in elements:
        print(xp.get_attr_from_element(element, attr))

    if print_result:
        # get test results
        test_results = xp.get_element_text("{0}{1}".format(prefix, "StdOut"))
        print("\n".join(test_results))


def parse_all_files():
    path = r"C:\Users\yans\Desktop\wd_cy_test_logs"
    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        parse_xml(file, True)
        break


def main():
    parse_all_files()


if __name__ == '__main__':
    main()

