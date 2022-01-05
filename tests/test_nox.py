from pytest_cookies.plugin import Result

from tests.utils import run_command


def test_formatting(project: Result) -> None:
    assert run_command("nox -s 'Check Code Format'") == 0


def test_unit_testing(project: Result) -> None:
    assert run_command("nox -s 'Unit Testing'") == 0
