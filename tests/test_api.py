import os
import tempfile
import json
import pytest

from reminders import app

proto_reminder = {
    'message': 'this is a reminder'
}


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    os.environ["DBTYPE"] = "mem"

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_basic_fetch(client):
    """Basic get should list reminders."""

    res = client.get('/api/reminders')
    assert res.status_code == 200
    assert res.content_type == 'application/json'


def test_save_works(client):
    """Save should work."""

    proto_reminder['message'] = 'test_save_works'
    res = client.post('/api/reminders', json=proto_reminder)
    assert res.status_code == 201
    assert res.content_type == 'application/json'
    assert proto_reminder['message'].encode() in res.data


def test_save_check_data(client):
    """Save should require a reminder message."""

    del proto_reminder['message']
    res = client.post('/api/reminders', json=proto_reminder)
    assert res.status_code == 400


def test_delete_works(client):
    """Delete should remove the item."""

    # Create one
    proto_reminder['message'] = 'test_delete_works'
    res = client.post('/api/reminders', json=proto_reminder)
    print("Got response:", res.data)
    reminder = json.loads(res.data)
    print("Got response:",  reminder)
    # Delete it
    res = client.delete('/api/reminders/{}'.format(reminder['guid']))
    assert res.status_code == 200
    assert res.content_type == 'application/json'
    # Get and ensure it's not there
    res = client.get('/api/reminders')
    print("Got response:", json.loads(res.data))
    assert proto_reminder['message'].encode() not in res.data
