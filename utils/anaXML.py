# -*- coding:utf-8 -*-
# author: John Holl

from lxml import etree
from xml.etree.ElementTree import parse

def get_sql(filename, id):
    tree = parse(filename)
    for child in tree.findall('sql'):
        if id == child.attrib['id']:
            sql = child.text.strip()
            break
    return sql

if __name__ == '__main__':
    get_sql('../conf/sql.xml', '1')