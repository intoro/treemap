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
     for trees in cursor:
      named_trees = {
       'latitude': trees[0],
       'longitude': trees[1],
       'date': datetime.datetime.strftime(trees[2], '%Y- %m-%d'),
       'category': trees[3],
       'description': trees[4]
      }
      named_trees.append(named_trees)
     return named_trees
    finally:
     connection.close()
