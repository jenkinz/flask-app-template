"""This module tests the application factory in flaskr/__init__.py."""
from flaskr import create_app


def test_config() -> None:
    """Test creation of an application by varying the test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client) -> None:
    """Test the hello endpoint.

    :param client: The test client used to make requests to the application."""
    response = client.get("/hello")
    assert response.data == b"Hello, World!"
