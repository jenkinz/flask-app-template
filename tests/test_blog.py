"""This module tests blog views and uses authentication. Call auth.login() and
subsequent requests from the client will be logged in as the `test` user.
"""
import pytest
from flask.testing import FlaskClient
from flaskr.db import get_db

from .conftest import AuthActions


def test_index(client: FlaskClient, auth: AuthActions) -> None:
    """Test the index view."""
    # test logged-out view
    response = client.get("/")
    assert b"Log In" in response.data
    assert b"Register" in response.data

    # test logged-in view
    auth.login()
    response = client.get("/")
    assert b"Log Out" in response.data
    assert b"test title" in response.data
    assert b"by test on 2018-01-01" in response.data
    assert b"test\nbody" in response.data
    assert b'href="/1/update"' in response.data
