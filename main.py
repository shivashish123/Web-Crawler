import threading
from queue import Queue
from spider import Spider
from domain import *
from first import *

PROJECT_NAME = 'Quora'
HOMEPAGE = 'https://www.quora.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NO_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def create_threads():
    for _ in range(NO_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True   # threads die when main exits
        t.start()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        create_jobs()


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


create_threads()
crawl()
