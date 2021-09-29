import MySQLdb
class mymysql(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '123456',
            db = 'xtp3')

    def insert_sql(self,temp,data):
        cur = self.conn.cursor()
        try:
            cur.executemany(temp,data)
            self.conn.commit()
        except:
            self.conn.rollback()

        finally:
            cur.close()