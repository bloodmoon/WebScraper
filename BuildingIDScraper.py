from abc import ABC
import requests
from html.parser import HTMLParser
from Utils import cleanup_text


class IDParse(HTMLParser, ABC):
    lastTag = False
    outputFile = open("buildingIDList", 'w')

    def handle_starttag(self, tag, attrs):
        if tag == "strong":
            self.lastTag = True

    def handle_endtag(self, tag):
        self.lastTag = False

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self.lastTag:
            if not any(char.isdigit() for char in data):
                self.outputFile.write(cleanup_text(data)+"\n")
                print(data)


r = requests.get('https://www.osu.edu/map/buildingindex.php')
print("OSU Building ID List")
p = IDParse()
test = p.feed(r.text)


