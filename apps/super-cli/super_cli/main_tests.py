import json

from typer.testing import CliRunner

from super_cli.main import app

runner = CliRunner()


def test_health_prints_ok() -> None:
    result = runner.invoke(app, ["health"])

    assert result.exit_code == 0
    assert json.loads(result.output) == {"status": "ok"}
