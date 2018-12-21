from urllib.parse import urlparse


def get_domain_name(url):       # for ex - jane.com (last 2) considered as domain name
    try:
        results=get_sub_domain_name(url).split('.')
        return results[-2]+'.'+results[-1]
    except:
        return ''


def get_sub_domain_name(url):     # for ex - blog.jane.com
    try:
        return urlparse(url).netloc
    except:
        return ''
