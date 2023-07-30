# Theory
from pymongo import *
from pymongo.errors import CollectionInvalid
from collections import OrderedDict
db = MongoClient("mongodb://localhost:27017")['Student']
user_schema = {
    #theory and practical

    'name': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'roll': {
        'type': 'int',
        'required': True,

    },
    'department': {
        'type': 'string',
        'required': True,
    },
    'sem': {
        'type': 'int',
        'required': True,
    },

    'ca1': {
        'type': 'int',
        'required': True,
    },

    'marks1': {
        'type': 'int',
        'required': True,
    },

    'attendence1': {
        'type': 'int',
        'required': True,
    },
    'ca2': {
        'type': 'int',
        'required': True,
    },

    'marks2': {
        'type': 'int',
        'required': True,
    },

    'attendence2': {
        'type': 'int',
        'required': True,
    },
    'ca3': {
        'type': 'int',
        'required': True,
    },

    'marks3': {
        'type': 'int',
        'required': True,
    },

    'attendence3': {
        'type': 'int',
        'required': True,
    },
    'ca4': {
        'type': 'int',
        'required': True,
    },

    'marks4': {
        'type': 'int',
        'required': True,
    },
    'attendence4': {
        'type': 'int',
        'required': True,
    },

    'pca1': {
        'type': 'int',
        'required': True,
    },
    'pcamarks1': {
        'type': 'int',
        'required': True,
    },
    'pca2': {
        'type': 'int',
        'required': True,
    },
    'pcamarks2': {
        'type': 'int',
        'required': True,
    },

    'credit1': {
        'type': 'double',
        'required': True
    },

    'points1': {
        'type': 'double',
        'required': True
    },

    'creditpoints1': {
        'type': 'double',
        'required': True
    },
    'credit2': {
        'type': 'double',
        'required': True
    },

    'points2': {
        'type': 'double',
        'required': True
    },

    'creditpoints2': {
        'type': 'double',
        'required': True
    },
    'credit3': {
        'type': 'double',
        'required': True
    },

    'points3': {
        'type': 'double',
        'required': True
    },

    'creditpoints3': {
        'type': 'double',
        'required': True
    },

    'credit4': {
        'type': 'double',
        'required': True
    },

    'points4': {
        'type': 'double',
        'required': True
    },

    'creditpoints4': {
        'type': 'double',
        'required': True
    },

    'credit5': {
        'type': 'double',
        'required': True
    },

    'points5': {
        'type': 'double',
        'required': True
    },

    'creditpoints5': {
        'type': 'double',
        'required': True
    },
    'credit6': {
        'type': 'double',
        'required': True
    },

    'points6': {
        'type': 'double',
        'required': True
    },

    'creditpoints6': {
        'type': 'double',
        'required': True
    },

    'sgpa': {
        'type': 'double',
        'required': True
    }
}
collection = 'StudentTheory'
validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
print(db.StudentTheory.create_index("roll"))
required = []
for field_key in user_schema:
    field = user_schema[field_key]
    properties = {'bsonType': field['type']}
    minimum = field.get('minlength')
    if type(minimum) == int:
        properties['minimum'] = minimum
    if field.get('required') is True:
        required.append(field_key)
    validator['$jsonSchema']['properties'][field_key] = properties
if len(required) > 0:
    validator['$jsonSchema']['required'] = required
query = [('collMod', collection),
         ('validator', validator)]

try:
    db.create_collection(collection)
except CollectionInvalid:
    pass
command_result = db.command(OrderedDict(query))

# if __name__ == '__main__':


#     db.StudentTheory.insert_one({
#     "name": "shoal",
#     "roll": 20,
#     "department": "IT",
#   "sem": 3,
#   "ca1": 22,
#   "marks1": 40,
#   "attendence1": 5,
#   "ca2": 20,
#   "marks2": 50,
#   "attendence2": 5,
#   "ca3": 21,
#   "marks3": 56,
#   "attendence3": 4,
#   "ca4": 23,
#   "marks4": 70,
#   "attendence4": 3,
#   "pca1": 30,
#   "pcamarks1": 55,
#   "pca2": 40,
#   "pcamarks2": 60,
#   "credit1": 1.0,
#   "points1": 5.6,
#   "creditpoints1": 22.6,
#    "credit2": 1.6,
#   "points2": 5.6,
#   "creditpoints2": 22.6,
#  "credit3": 1.6,
#   "points3": 5.6,
#   "creditpoints3": 22.6,
#  "credit4": 1.6,
#   "points4": 5.6,
#   "creditpoints4": 22.6,
#  "credit5": 1.6,
#   "points5": 5.6,
#   "creditpoints5": 22.6,
#  "credit6": 1.6,
#   "points6": 5.6,
#   "creditpoints6": 22.6,
#   "sgpa":5.62

#     })
