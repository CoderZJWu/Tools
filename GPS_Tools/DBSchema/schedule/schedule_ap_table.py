import cx_Oracle
import time
from datetime import datetime
import pandas as pd
import json
import schedule


def sjcx():
    print('start')
    conn = cx_Oracle.connect('zhangsan', 'root123', '127.0.0.1:1521/booksales')
    v_sql = "SELECT * FROM mytable"
    cursor = conn.cursor()
    cursor.execute(v_sql)
    data = cursor.fetchall()
    print(data)
    cursor.close()
    conn.close()
    print('end')

    json_data = []
    for row in data:
        result = {}
        result['userCode'] = row[0]
        result['userName'] = row[1]
        json_data.append(result)

    with open('output.json', 'w') as f:
        json.dump(json_data, f)


schedule.every(1).minutes.do(sjcx)  # 每分钟执行

while True:
    schedule.run_pending()
