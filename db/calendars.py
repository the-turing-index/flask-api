from pymongo import MongoClient
from config.settings import MONGODB_CONNECTION

client = MongoClient(MONGODB_CONNECTION)
db = client.flask_api_development

community_events = db.community.find( {} )
mod1_events = db.mod1.find( {} )
mod2_events = db.mod2.find( {} )
mod3_events = db.mod3.find( {} )
mod4_events = db.mod4.find( {} )

community = list(community_events)[0]
del community['_id']
mod1 = list(mod1_events)[0]
del mod1['_id']
mod2 = list(mod2_events)[0]
del mod2['_id']
mod3 = list(mod3_events)[0]
del mod3['_id']
mod4 = list(mod4_events)[0]
del mod4['_id']

all_events = {
    **community,
    **mod1,
    **mod2,
    **mod3,
    **mod4
}
