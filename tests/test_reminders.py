import os
import tempfile

import pytest

from reminders import app

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_basic_fetch(client):
    """Basic get should list reminders."""

    res = client.get('/')
    assert b'All Your Reminders' in res.data


def test_save_check_data(client):
    """Save should require a reminder message."""

    res = client.post('/save', data="")
    assert b'This field is required' in res.data
