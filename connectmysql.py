import pymysql
# สร้าง function เชื่อ


def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='pythondb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


# print(connectdb())
