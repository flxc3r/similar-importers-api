import json
import pymysql
import datetime

if __name__ == "__main__":
    from secrets_db import hostname, user, password, database
else:
    from .secrets_db import hostname, user, password, database
    

def _get_importer_similar(importer_id):
    try:
        connection = pymysql.connect(host=hostname,
                                user=user,
                                password=password,
                                db=database ,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                                )

        with connection.cursor() as cursor:
            sql = """SELECT d.similar_importer_id as importer_id, i.importer_name, round(d.distance, 5) as distance
                    FROM distances d 
                    JOIN importers i on i.importer_id = d.similar_importer_id
                    WHERE d.importer_id=%s
                    ORDER BY d.distance ASC, i.importer_name ASC""" % str(importer_id)
            
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
    a = _get_importer_similar(3262)
    print(a)


