import json
import pymysql
import datetime

if __name__ == "__main__":
    from secrets_db import hostname, user, password, database
else:
    from .secrets_db import hostname, user, password, database


def _get_importer(importer_id):
    try:
        connection = pymysql.connect(host=hostname,
                                user=user,
                                password=password,
                                db=database ,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                                )

        with connection.cursor() as cursor:
            sql = """SELECT i.* 
                    FROM importers i
                    WHERE i.importer_id=%s""" % str(importer_id)
            
            cursor.execute(sql)
            result = cursor.fetchone()
            
        with connection.cursor() as cursor:
            sql = """SELECT city, province, postalcode
            FROM importers_addresses
            WHERE importer_id=%s""" % str(importer_id)
            
            cursor.execute(sql)
            result["importer_addresses"] = cursor.fetchall()

        result = json.dumps(result)

    except Exception as e:
        result = e
    finally:
        if connection:
            connection.close()

    return result


if __name__ == "__main__":
    a = _get_importer(3262)
    print(a)


