import json
import pymysql
import datetime

if __name__ == "__main__":
    from secrets_db import hostname, user, password, database
else:
    from .secrets_db import hostname, user, password, database


def _get_product(product_id):
    try:
        connection = pymysql.connect(host=hostname,
                                user=user,
                                password=password,
                                db=database ,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                                )

        with connection.cursor() as cursor:
            sql = """SELECT p.* 
                    FROM products p
                    WHERE p.product_id=%s""" % str(product_id)
            
            cursor.execute(sql)
            result = cursor.fetchone()
            
        result = json.dumps(result)

    except Exception as e:
        result = e
    finally:
        if connection:
            connection.close()

    return result


if __name__ == "__main__":
    a = _get_product("220850")
    print(a)


