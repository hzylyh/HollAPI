# -*- coding:utf-8 -*-
#缺少异常捕获，待后续添加#

import pymysql, configparser
from . import anaXML

def ana_dbconf(filename):
    """
    :param filename: db的配置文件
    :return: host, port, user, passwd, DBName, charset
    """
    config = configparser.ConfigParser()
    config.read(filename)
    section = str.upper(config.sections()[0])
    host = config.get(section, 'host')
    port = int(config.get(section, 'port'))
    user = config.get(section, 'user')
    passwd = config.get(section, 'passwd')
    DBName = config.get(section, 'db')
    charset = config.get(section, 'charset')
    return host, port, user, passwd, DBName, charset


def excute_sql(id):
    """
    :param sql: sql语句
    :return: 执行结果(元组)
    """
    host, port, user, passwd, db, charset = ana_dbconf('../conf/db.properties')
    sql = anaXML.get_sql('../conf/sql.xml', id)
    print(sql)
    db = pymysql.connect(host=host, port=port, user=user, passwd=passwd,
                         db=db, charset=charset)
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    db.close()
    return results

if __name__ == '__main__':
    excute_sql()