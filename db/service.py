from db.calendars import db
from googleapiclient import discovery
from oauth2client import client
import httplib2
import json
import datetime

saved_credentials = list(db.tokens.find({}))[0] # SMC
del saved_credentials['_id']
saved_credentials = json.dumps(saved_credentials)

refreshed_credentials = client.OAuth2Credentials.from_json(saved_credentials) # SMD

db.tokens.drop()
db.tokens.insert_one(json.loads(refreshed_credentials.to_json()))

http_auth = refreshed_credentials.authorize(httplib2.Http())
calendar_service = discovery.build('calendar', 'v3', http=http_auth)

be1 = ['casimircreative.com_59k8msrrc2ddhcv787vubvp0s4@group.calendar.google.com', 'fe1_doc']
fe1 = ['casimircreative.com_m6bndqol81h6jdlnpo0a6raot0@group.calendar.google.com', 'be1_doc']
be2 = ['casimircreative.com_rps2hg1nfqjih4rcl3gl6s4lpk@group.calendar.google.com', 'fe2_doc']
fe2 = ['casimircreative.com_cjiffoqvtajq43n5mn290cp744@group.calendar.google.com', 'be2_doc']
be3 = ['casimircreative.com_e9k9b6n7bok174ilmqbfdr0sc4@group.calendar.google.com', 'fe3_doc']
fe3 = ['casimircreative.com_krb9p35ck35m4uoji5d2715844@group.calendar.google.com', 'be3_doc']
combined = ['casimircreative.com_c1s3vspg5v09vh5cnnh88dn2nc@group.calendar.google.com', 'combined_doc']
community = ['casimircreative.com_ronr9dk92ndvlhsk03kf8jd2ro@group.calendar.google.com', 'community_events_doc']

event_calendars = [be1, fe1, be2, fe2, be3, fe3, combined, community]

start_today = datetime.date.today().isoformat() + 'T15:00:00.000000Z'
end_today = datetime.date.today().isoformat() + 'T23:00:00.000000Z'

events_doc = {
    'fe1_doc': [],
    'be1_doc': [],
    'fe2_doc': [],
    'be2_doc': [],
    'fe3_doc': [],
    'be3_doc': [],
    'combined_doc': [],
    'community_events_doc': [] }

for calendar in event_calendars:
    calendar_id = calendar[0]
    calendar_doc = calendar[1]

    events_result = calendar_service.events().list(calendarId=calendar_id, timeMin=start_today,
                                        timeMax=end_today, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        try:
            start = event['start'].get('dateTime', event['start'].get('date'))
        except KeyError:
            start = None
        try:
            end_time = event['end'].get('dateTime', event['end'].get('date'))
        except KeyError:
            end_time = None
        try:
            summary = event['summary']
        except KeyError:
            summary = None
        try:
            htmlLink = event['htmlLink']
        except KeyError:
            htmlLink = None
        try:
            description = event['description']
        except KeyError:
            description = None
        try:
            str = "https://turingschool.zoom.us/j/"
            if str not in event['location']:
                location = None
            else:
                location = event['location']
        except KeyError:
            location = None

        doc = { "start": start,
                "end": end_time,
                "location": location,
                "summary": summary,
                "htmlLink": htmlLink }

        events_doc[calendar_doc].append(doc)

mod1_doc = {
    "mod1": {
        "FE": events_doc['fe1_doc'],
        "BE": events_doc['be1_doc']
    }
}

mod2_doc = {
    "mod2": {
        "FE": events_doc['fe2_doc'],
        "BE": events_doc['be2_doc']
    }
}

mod3_doc = {
    "mod3": {
        "FE": events_doc['fe3_doc'],
        "BE": events_doc['be3_doc']
    }
}

mod4_doc = {
    "mod4": events_doc['combined_doc']
}

community_doc = {
    "community": events_doc['community_events_doc']
}

db.community.drop()
db.mod1.drop()
db.mod2.drop()
db.mod3.drop()
db.mod4.drop()

db.community.insert_one(community_doc)
db.mod1.insert_one(mod1_doc)
db.mod2.insert_one(mod2_doc)
db.mod3.insert_one(mod3_doc)
db.mod4.insert_one(mod4_doc)
