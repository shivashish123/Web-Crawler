from urllib.request import urlopen

from first import *
from link_finder import LinkFinder


class Spider:
    # shared among all objects(spiders)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.domain_name = domain_name
        Spider.base_url = base_url
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project(Spider.project_name)
        create_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name+' crawling ' + page_url)
            print('Queue length = ' + str(len(Spider.queue)))
            print('Crawled length = ' + str(len(Spider.crawled)))
            Spider.add_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_link(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):    # ensures url is html not .exe or pdf file
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")      # gets binary html code and decode to string
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error occurred \n')
            return set()
        return finder.page_links()

    @staticmethod
    def add_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:  # restricts spider to that website
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_item_to_file(Spider.queue_file, Spider.queue)
        set_item_to_file(Spider.crawled_file, Spider.crawled)

