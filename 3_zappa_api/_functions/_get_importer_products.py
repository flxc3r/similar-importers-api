import json
import pymysql
import datetime

#from .secrets_db import hostname, user, password, database

if __name__ == "__main__":
    from secrets_db import hostname, user, password, database
else:
    from .secrets_db import hostname, user, password, database
    

def _get_importer_products(importer_id):
    try:
        connection = pymysql.connect(host=hostname,
                                user=user,
                                password=password,
                                db=database ,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                                )

        with connection.cursor() as cursor:
            sql = """SELECT p.product_id, p.product_name 
                    FROM importers_products ip
                    JOIN products p on p.product_id = ip.product_id
                    WHERE ip.importer_id=%s""" % str(importer_id)
            
            cursor.execute(sql)
            result = cursor.fetchall()
            
        
        result = json.dumps(result)

    except Exception as e:
        result = e
    finally:
        if connection:
            connection.close()

    return result


if __name__ == "__main__":
    a = _get_importer_products(3262)
    print(a)


