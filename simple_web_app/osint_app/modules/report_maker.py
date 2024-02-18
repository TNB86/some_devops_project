import csv
import threading


from ..modules.search_subdomains import parse_collection, collect_data, DATE

LOCK = threading.RLock()
HEADER = ['Domain', 'IP', 'Comments', 'Sources']


def structure(domain, ip, comments='', sources=''):
    struct = dict()
    struct['Domain'] = domain
    struct['IP'] = ip
    struct['Comments'] = comments
    struct['Sources'] = sources
    return struct


def make_single_record(item, writer):
    domain = item[0]
    ip = item[1]
    row = structure(domain, ip)
    with LOCK:
        writer.writerow(row)


def make_report(domain):
    data = parse_collection(collect_data(domain))
    with open(f'./reports/{domain}-{DATE}.csv', mode='w', encoding='utf-8') as w_file:
        writer = csv.DictWriter(w_file, fieldnames=HEADER, delimiter=';', lineterminator='\r')
        writer.writeheader()
    threads = list()
    with open(f'./reports/{domain}-{DATE}.csv', mode='a', encoding='utf-8') as w_file:
        writer = csv.DictWriter(w_file, fieldnames=HEADER, delimiter=';', lineterminator='\r')
        for item in data:
            x = threading.Thread(target=make_single_record, args=(item, writer,))
            x.start()
            threads.append(x)
        for thread in threads:
            thread.join()


if __name__ == '__main__':
    pass