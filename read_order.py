import pymysql
from pymysql import cursors
from dbpackage import ConnectMySQL as con


def read_order():
    connection = con.connectdb()
    cursor = connection.cursor()
    sql = "SELECT * FROM orders LIMIT 10"

    try:
        cursor.execute(sql)
        connection.commit()
        # loop data
        for row in cursor:
            print("ORDER_ID", row['order_id'])
            print("CUSTOMER_ID", row['customer_id'])
            print("SHIP_NAME", row['ship_name'])
            print("POSTAL_CODE", row['ship_postal_code'])
            print("-----------------------------")
    except pymysql.err:
        print(pymysql.err)


read_order()
