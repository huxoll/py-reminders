import os
import tempfile

import pytest

from reminders import app

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            #init_db()
            print("Could init db.")
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_basic_fetch(client):
    """Basic get should list reminders."""

    rv = client.get('/')
    assert b'All Your Reminders' in rv.data


def test_save_check_data(client):
    """Save should require a reminder message."""

    rv = client.post('/save')
    # print("Got" + str(rv.data))
    assert b'This field is required' in rv.data
