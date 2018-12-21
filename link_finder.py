from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):   # inherits from HTMLParser

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attributes, value) in attrs:
                if attributes == 'href':
                    url = parse.urljoin(self.base_url, value)  # if it is full url then do nothing else add base_url
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
