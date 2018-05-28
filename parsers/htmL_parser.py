from html.parser import HTMLParser
import re


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag {}".format(tag))
        pass

    def handle_endtag(self, tag):
        # print("Encountered an end tag {}".format(tag))
        pass

    def handle_data(self, data):
        # print("The extracted data are {}".format(data))
        pattern_name = 'HResult\\\"\:\\\"(.*?)\\\"'
        search_pattern(data, pattern_name)
        if not hasattr(self, 'ret'):
            self.ret = []
        self.ret.append(data)

    def get_rets(self):
        return self.ret


def search_pattern(file_name, re_pattern):
    matches = re.findall(re_pattern, file_name)
    if matches:
        print(matches)


if __name__ == '__main__':
    file = "test.html"
    file_obj = open(file)
    html_raw_data = file_obj.read()
    pattern = 'HResult\\\"\\\"(.*?)\\\"'
    search_pattern(html_raw_data, pattern)

    myParser = MyHTMLParser()
    myParser.feed(html_raw_data)
