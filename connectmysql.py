import pymysql
# สร้าง function เชื่อ


def connectdb():
    # connection = pymysql.connect(
    #     host='localhost',
    #     user='root',
    #     password='',
    #     db='pythondb',
    #     port=3306,
    #     cursorclass=pymysql.cursors.DictCursor

    connection = pymysql.connect(
        host='bmaygliauqa8j5ri1pk4-mysql.services.clever-cloud.com',
        user='u0q3n3evgyrm4ca4',
        password='ph4aMdMqWvmD7hIFGDhH',
        db='bmaygliauqa8j5ri1pk4',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


# print(connectdb())


