from click.testing import CliRunner

from gpiozero_mqtt_robot.main import main


def test_main_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
