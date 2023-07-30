
from pymongo import *
db = MongoClient("mongodb://localhost:27017")['Student']
g = input('Enter the key: ')
f = input('Enter the data:  ')

print(db.StudentTheory.find_one({g:f}))
