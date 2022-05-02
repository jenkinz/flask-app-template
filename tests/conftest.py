"""This module provides text fixtures that each test will use."""
import os
import tempfile

import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask.testing import FlaskCliRunner
from flaskr import create_app
from flaskr.db import get_db
from flaskr.db import init_db

with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf-8")


@pytest.fixture
def app():
    """Test fixture to call the application factory and pass `test_config` to
    configure the application and database for testing (instead of using the
    local development configuration)."""
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({"TESTING": True, "DATABASE": db_path})

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Test fixture to create a test client. Tests will use the returned client
    to make requests to the application without running the server.

    :param app: The application object created by the `app` fixture.
    :return: The test client to use to make requests to the application.
    """
    return app.test_client()


@pytest.fixture
def runner(app: Flask) -> FlaskCliRunner:
    """Test fixture to create a runner that can call the Click commands
    registered with the application.

    :param app: The application object created by the `app` fixture.
    :return: The runner to use to test registered Click commands.
    """
    return app.test_cli_runner()
