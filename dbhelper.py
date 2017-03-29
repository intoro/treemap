import pymysql
import dbconfig
import datetime


class DBHelper:

  def connect(self, database="treemap"):
    return pymysql.connect(host='localhost',
              user=dbconfig.db_user,
              passwd=dbconfig.db_password,
              db=database)

# add_crime ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
  def add_tree(self, category, date, latitude, longitude, description):
    connection = self.connect()
    try:
      query = "INSERT INTO trees (category, date, latitude, longitude, description) \
        VALUES (%s, %s, %s, %s, %s)"
      with connection.cursor() as cursor:
        cursor.execute(query, (category, date, latitude, longitude, description))
        connection.commit()
    except Exception as e:
      print(e)
    finally:
      connection.close()

# get_all_crimes )))))))))))))))))))))))))))))))))))))))))))))))))))))))))
  def get_all_trees(self):
    connection = self.connect()
    try:
     query = "SELECT latitude, longitude, date, category, description FROM trees;"
     with connection.cursor() as cursor:
      cursor.execute(query)
     named_trees = []
     for tree in cursor:
      named_tree = {
       'latitude': tree[0],
       'longitude': tree[1],
       'date': datetime.datetime.strftime(tree[2], '%Y- %m-%d'),
       'category': tree[3],
       'description': tree[4]
      }
      named_trees.append(named_tree)
     return named_trees
    finally:
     connection.close()
