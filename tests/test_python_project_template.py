from python_project_template import __version__
from python_project_template.math import multiply_two_numbers

TEST_STRING = (
    "This is a very long string to test auto reformatting with "
    "black. It should get reformatted automatically...."
)


def test_version():
    assert __version__ == "0.1.0"


def test_multiply_two_numbers():
    result = multiply_two_numbers(2, 3)
    assert result == 6
