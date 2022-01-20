from http import client


def get_database():
  from pymongo import MongoClient
  import pymongo

  connection_string = 'PLACE CONNECTION STRING HERE'
  client = MongoClient(connection_string)
  return client["restaurants"]


if __name__ == "__main__":
  dbname = get_database()