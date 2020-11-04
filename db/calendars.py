from pymongo import MongoClient
from config.settings import MONGODB_CONNECTION, ENVIRONMENT

client = MongoClient(MONGODB_CONNECTION)

if ENVIRONMENT == 'production': db = client.flask_api_production
if ENVIRONMENT == 'development': db = client.flask_api_development

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

# demo data

demo_community_events = db.demoCommunity.find( {} )
demo_mod1_events = db.demoMod1.find( {} )
demo_mod2_events = db.demoMod2.find( {} )
demo_mod3_events = db.demoMod3.find( {} )
demo_mod4_events = db.demoMod4.find( {} )

demo_community = list(demo_community_events)[0]
del demo_community['_id']
demo_mod1 = list(demo_mod1_events)[0]
del demo_mod1['_id']
demo_mod2 = list(demo_mod2_events)[0]
del demo_mod2['_id']
demo_mod3 = list(demo_mod3_events)[0]
del demo_mod3['_id']
demo_mod4 = list(demo_mod4_events)[0]
del demo_mod4['_id']

demo_all_events = {
    **demo_community,
    **demo_mod1,
    **demo_mod2,
    **demo_mod3,
    **demo_mod4
}
