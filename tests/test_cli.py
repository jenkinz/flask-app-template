from click.testing import CliRunner
from python_project_template.cli import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["--count=3", "--name=Brian"])
    assert result.exit_code == 0
    assert result.output == "Hello Brian!\nHello Brian!\nHello Brian!\n"
