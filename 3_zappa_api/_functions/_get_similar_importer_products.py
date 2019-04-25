import json
import pymysql

if __name__ == "__main__":
    from secrets_db import hostname, user, password, database
else:
    from .secrets_db import hostname, user, password, database
    

def _get_similar_importer_products(importer_id):
    try:
        connection = pymysql.connect(host=hostname,
                                user=user,
                                password=password,
                                db=database ,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                                )

        with connection.cursor() as cursor:

            sql = """select ip.importer_id, ip.product_id
                from importers_products ip
                where ip.importer_id in (select d.similar_importer_id from distances d WHERE d.importer_id=%s)""" % str(importer_id)
            
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
    a = _get_similar_importer_products(3262)
    print(a)


