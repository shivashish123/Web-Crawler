import os


def create_project(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_files(project_name, url):
    queue = project_name+"/queue.txt"
    crawled = project_name+"/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


def append_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')


def delete_file_contents(path):
    with open(path, 'w'):
        pass            # do nothing


def file_to_set(path):
    result = set()
    with open(path, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return result


def set_item_to_file(path, set_items):
    delete_file_contents(path)
    for link in sorted(set_items):
        append_file(path, link+'\n')



