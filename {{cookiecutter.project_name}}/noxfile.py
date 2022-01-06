import sys

import nox
from nox_poetry import Session, session

CODE_DIRECTORIES = ["{{cookiecutter.project_slug}}", "tests"]
CODE_DIRECTORIES_WITH_NOTEBOOKS = CODE_DIRECTORIES + ["notebooks"]
DEFAULT_PYTHON_VERSION = False
DEFAULT_VENV_BACKEND = "none"
MINIMAL_CODE_COVERAGE = 70

# Specify default tasks
nox.options.sessions = (
    "Check Code Format",
    "Import Checking",
    "Lint Checking",
    "Type Checking",
    "Unit Tests",
)


@session(
    name="Check Code Format",
    python=DEFAULT_PYTHON_VERSION,
    venv_backend=DEFAULT_VENV_BACKEND,
)
def format_checking(session: Session) -> None:
    session.run("black", "--check", *CODE_DIRECTORIES_WITH_NOTEBOOKS)


@session(
    name="Import Checking",
    python=DEFAULT_PYTHON_VERSION,
    venv_backend=DEFAULT_VENV_BACKEND,
)
def import_checking(session: Session) -> None:
    session.run("isort", "--check-only", *CODE_DIRECTORIES)


@session(
    name="Lint Checking",
    python=DEFAULT_PYTHON_VERSION,
    venv_backend=DEFAULT_VENV_BACKEND,
)
def import_checking(session: Session) -> None:
    session.run("flake8", *CODE_DIRECTORIES)


@session(
    name="Unit Tests", python=DEFAULT_PYTHON_VERSION, venv_backend=DEFAULT_VENV_BACKEND
)
def unit_test(session: Session) -> None:
    session.run(
        "pytest",
        "--cov={{cookiecutter.project_slug}}",
        f"--cov-fail-under={MINIMAL_CODE_COVERAGE}",
        "-n",
        "auto",
        *session.posargs,
    )


@session(
    name="Type Checking",
    python=DEFAULT_PYTHON_VERSION,
    venv_backend=DEFAULT_VENV_BACKEND,
)
def type_checking(session: Session) -> None:
    args = session.posargs or CODE_DIRECTORIES
    session.run("mypy", f"--python-executable={sys.executable}", *args)


@session(
    name="Build Docs", python=DEFAULT_PYTHON_VERSION, venv_backend=DEFAULT_VENV_BACKEND
)
def build_docs(session: Session) -> None:
    session.run("mkdocs", "build", *session.posargs)


@session(
    name="Serve Docs", python=DEFAULT_PYTHON_VERSION, venv_backend=DEFAULT_VENV_BACKEND
)
def serve_docs(session: Session) -> None:
    session.run("mkdocs", "serve", *session.posargs)
