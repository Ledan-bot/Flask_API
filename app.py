from flask import Flask
from db import connection


app = Flask(__name__)

@app.route('/')
def index():
  return "hello world"

@app.route('/api/restaurants/all')
def all_restuarants():
  client = connection.get_database()
  collection = client["restuarants"]
  restaurants = collection.find()
  for place in restaurants:
    print(place)
  return "fetched"

@app.route('/api/restuarants/create')
def create_restuarant():
  return "created"


if __name__ == '__main__':
  app.run(debug=True)