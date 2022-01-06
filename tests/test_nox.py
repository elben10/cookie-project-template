from pytest_cookies.plugin import Result

from tests.utils import run_command


def test_formatting(project: Result) -> None:
    assert run_command("nox -s 'Check Code Format'") == 0


def test_unit_testing(project: Result) -> None:
    assert run_command("nox -s 'Unit Tests'") == 0


def test_type_checking(project: Result) -> None:
    assert run_command("nox -s 'Type Checking'") == 0


def test_lint_checking(project: Result) -> None:
    assert run_command("nox -s 'Lint Checking'") == 0


def test_import_checking(project: Result) -> None:
    assert run_command("nox -s 'Import Checking'") == 0


def test_build_docs(project: Result) -> None:
    assert run_command("nox -s 'Build Docs'") == 0
