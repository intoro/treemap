from flask import Flask
from flask import render_template
from flask import request
import json
import dbconfig
import datetime
import dateparser
import string
if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper

app = Flask(__name__)
DB = DBHelper()
categories = ['Orange', 'Lemon', 'Lime', 'Grapefruit', 'Bannana', 'Tangerine', 'Avocado']

@app.route("/")
def home(error_message=None):
    trees = DB.get_all_trees()
    trees = json.dumps(trees)
    return render_template("home.html", trees=trees, categories=categories, error_message=error_message)

# @app.route("/add", methods=["POST"])
# def add():
#   try:
#     data = request.form.get("userinput")
#     DB.add_input(data)
#   except Exception as e:
#     print e
#   return home()
#
# @app.route("/clear")
# def clear():
#   try:
#     DB.clear_all()
#   except Exception as e:
#     print e
#   return home()

@app.route("/submittree", methods=['POST'])
def submittree():
  category = request.form.get("category")
  if category not in categories:
      return home()
  date = request.form.get("date")

  try:
    latitude = float(request.form.get("latitude"))
    longitude = float(request.form.get("longitude"))
  except ValueError:
    return home()
  description = request.form.get("description")
  description = sanitize_string(request.form.get("description"))
  DB.add_tree(category, date, latitude, longitude, description)
  return home()

def format_date(userdate):
  date = dateparser.parse(userdate)
  try:
      return datetime.datetime.strftime(date, "%Y-%m-%d")
  except TypeError:
      return None

def sanitize_string(userinput):
    whitelist = string.letters + string.digits + " !?$.,;:-'()&"
    return filter(lambda x: x in whitelist, userinput)






if __name__ == '__main__':
  app.run(port=5000, debug=True)
