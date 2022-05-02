"""This module tests authentication."""
from typing import Union

import pytest
from flask import Flask
from flask import g
from flask import session
from flask.testing import FlaskClient
from flaskr.db import get_db

from .conftest import AuthActions


def test_register(client: FlaskClient, app: Flask) -> None:
    """Test the `register` view.

    :param client: The client runner.
    :param app: The application.
    """
    assert client.get("/auth/register").status_code == 200
    response = client.post(
        "/auth/register", data={"username": "a", "password": "a"}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert (
            get_db()
            .execute(
                "SELECT * FROM user WHERE username = 'a'",
            )
            .fetchone()
            is not None
        )


"""pytest.mark.parameterize tells pytest to run the same test function with
different arguments. We use it here to test different invalid input and error
messages without writing the same code three times."""


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("", "", b"Username is required."),
        ("a", "", b"Password is required."),
        ("test", "test", b"already registered"),
    ),
)
def test_register_validate_input(
    client: FlaskClient,
    username: str,
    password: str,
    message: Union[str, bytes],
) -> None:
    """Test the `register` view with input data validation."""
    response = client.post(
        "/auth/register", data={"username": username, "password": password}
    )
    assert message in response.data


def test_login(client: FlaskClient, auth: AuthActions) -> None:
    """Test login and that `user_id` gets set in session after logging in."""
    assert client.get("/auth/login").status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    # Using client in a `with` block allows accessing context variables such as
    # `session` after the response is returned. Normally, accessing `session`
    # outside of a request would raise an error.
    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user["username"] == "test"


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("a", "test", b"Incorrect username"),
        ("test", "a", b"Incorrect password"),
    ),
)
def test_login_validate_input(
    auth: AuthActions, username: str, password: str, message: Union[str, bytes]
) -> None:
    """Test login with invalid inputs."""
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client: Flask, auth: AuthActions) -> None:
    """Test logging out."""
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session
