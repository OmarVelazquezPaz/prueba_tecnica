import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'temp_records'
username = 'postgres'
pwd = 'hibah'
port_id = 5432
conn = None


def db_conn(exc, values=None,select=False):
    try:
        with psycopg2.connect(host=hostname,port=port_id,database=database, user=username,password=pwd) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(exc,values)
                if select:
                    return (record for record in cur.fetchall())
    except Exception as e:
        print(e)
    finally:
        
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    DROP_TABLE = 'DROP TABLE IF EXISTS todos2'
    create_script = ''' CREATE TABLE IF NOT EXISTS todos2 (
                                    id int PRIMARY KEY,
                                    name varchar(40) NOT NULL,
                                    description varchar(40) NOT NULL)'''
    db_conn(DROP_TABLE)
    # db_conn(create_script)


    # insert_script = 'INSERT INTO todos2 (id, name, description) values(%s,%s,%s)'
    # insert_values = [(1, 'Go to','Laura'),(2, 'Go to','heaven'),(3, 'Go to','Car'),]

    # for record in insert_values:
    #     db_conn(insert_script,record)