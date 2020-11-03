import pymongo

from data.mod1 import fe1, be1
from data.mod2 import fe2, be2
from data.mod3 import fe3, be3
from data.combined import combined
from data.community import community

settings = {
    'host': 'localhost:27017',
    'database': 'flask_api_development',
}

mod1_doc = {
    "mod1": {
        "FE": fe1,
        "BE": be1
    }
}

mod2_doc = {
    "mod2": {
        "FE": fe2,
        "BE": be2
    }
}

mod3_doc = {
    "mod3": {
        "FE": fe3,
        "BE": be3
    }
}

mod4_doc = {
    "mod4": combined
}

community_doc = {
    "community": community
}

try:
    conn = pymongo.MongoClient("mongodb://{host}/{database}".format(**settings))
except Exception as ex:
    print("Error:"), ex
    exit('Failed to connect, terminating.')

db = conn.flask_api_development

print('Now seeding database.')
db.community.insert_one(community_doc)
db.mod1.insert_one(mod1_doc)
db.mod2.insert_one(mod2_doc)
db.mod3.insert_one(mod3_doc)
db.mod4.insert_one(mod4_doc)
print('Seeding complete.')
