from ..modules import report_maker
import json


def main(name, domain):
    # domain = input('Enter scanning domain like test.test: ')
    report_maker.make_report(domain)
    print('Report successfully created!')
