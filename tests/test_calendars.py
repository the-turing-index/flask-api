from flask import json
from app import app

def test_success():
    response = app.test_client().get(
        '/calendars',
        content_type = 'application/json',
    )

    data = json.loads(response.get_data(as_text=False))

    assert response.status_code == 200
    assert response.content_type == 'application/json'

    data = data['data']

    assert len(data) == 3
    assert data['id'] == None
    assert data['type'] == 'calendars'
    assert data['attributes']


    attributes = data['attributes']
    assert len(attributes) == 5

    mod1 = attributes[0]['mod1']
    assert mod1
    assert mod1['frontend']
    assert mod1['frontend'] == {'zoom_link': ''}
    assert mod1['backend']
    assert mod1['backend'] == {'zoom_link': ''}

    mod2 = attributes[1]['mod2']
    assert mod2
    assert mod2['frontend']
    assert mod2['frontend'] == {'zoom_link': ''}
    assert mod2['backend']
    assert mod2['backend'] == {'zoom_link': ''}

    mod3 = attributes[2]['mod3']
    assert mod3
    assert mod3['frontend']
    assert mod3['frontend'] == {'zoom_link': ''}
    assert mod3['backend']
    assert mod3['backend'] == {'zoom_link': ''}

    assert attributes[3]['mod4'] == {'zoom_link': ''}
    assert attributes[4]['community']  == {'zoom_link': ''}
