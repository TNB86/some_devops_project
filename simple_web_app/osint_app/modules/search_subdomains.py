import json
from datetime import datetime
from ..modules import connection_to_services
import requests


DATE = datetime.now().strftime('%d_%m_%Y')


def collect_data(domain):
    response = requests.get(connection_to_services.URL + f'{domain}/subdomains?limit=1000',
                            headers=connection_to_services.HEADERS)
    with open(f'./simple_web_app/logs/{domain}-{DATE}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)
    return response


def get_json(filename):
    with open(f'./simple_web_app/logs/{filename}.json', 'r', encoding='utf-8') as file:
        json_res = json.load(file)
    return json_res


def parse_collection(response):
    if type(response) is dict:
        data = response['data']
    else:
        data = response.json()['data']
    res = []
    for item in data:
        id = item.get('id')  # Домен
        atr = item.get('attributes')  # В атрибуте лежит last_dns_records
        dns = atr.get('last_dns_records')  # В last_dns_records лежит value c ip (ip есть только у type = A)
        for dnss in dns:
            type_name = dnss.get('type')
            if type_name == 'A':
                ip = dnss.get('value')
                res.append([id, ip])
    return res


if __name__ == '__main__':
    pass
