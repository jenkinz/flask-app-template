"""This module tests the database."""
import sqlite3

import pytest
from flask import Flask
from flaskr.db import get_db


def test_get_close_db(app: Flask) -> None:
    """Tests that `get_db` returns the same connection each time it's
    called.

    :param app: The application to test."""
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute("SELECT 1")

    assert "closed" in str(e.value)


def test_init_db_command(runner, monkeypatch) -> None:
    """Test the `init-db` command (should call init_db function and output as
    message). This test uses pytest's monkeypatch test fixture to replace the
    init_db function with one that records that it's been called. The runner
    fixture in conftest.py is used to call the `init-db` command by name.

    :param runner: The CLI test runner.
    :param monkeypatch: pytest monkeypatch test fixture
    """

    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr("flaskr.db.init_db", fake_init_db)
    result = runner.invoke(args=["init-db"])
    assert "Initialized" in result.output
    assert Recorder.called
