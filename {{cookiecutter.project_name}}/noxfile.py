import sys
from pathlib import Path

from nox_poetry import Session, session

CODE_DIRECTORIES = ["src/{{cookiecutter.project_name}}", "tests"]
CODE_DIRECTORIES_WITH_NOTEBOOKS = CODE_DIRECTORIES + ["notebooks"]
PYTHON_VERSIONS = ("3.8",)
DEFAULT_PYTHON_VERSION = False
DEFAULT_SESSIONS = (
    "Check Code Format",
    "Import Checking",
    "Unit Tests",
    "Type Checking",
    "Lint Checking",
)
MINIMAL_CODE_COVERAGE = 70


@session(
    name="Check Code Format",
    python=DEFAULT_PYTHON_VERSION,
)
def format_checking(session: Session) -> None:
    session.install("black")
    session.run("black", "--check", *CODE_DIRECTORIES_WITH_NOTEBOOKS)


@session(name="Import Checking", python=DEFAULT_PYTHON_VERSION)
def import_checking(session: Session) -> None:
    session.install("isort")
    session.run("isort", "--check-only", *CODE_DIRECTORIES)


@session(name="Lint Checking", python=DEFAULT_PYTHON_VERSION)
def import_checking(session: Session) -> None:
    session.install("flake8")
    session.run("flake8", *CODE_DIRECTORIES)


@session(name="Unit Tests", python=PYTHON_VERSIONS)
def unit_test(session: Session) -> None:
    session.run_always("poetry", "install", external=True)
    session.run(
        "pytest",
        "--cov=src/{{cookiecutter.project_name}}",
        f"--cov-fail-under={MINIMAL_CODE_COVERAGE}",
        "-n",
        "auto",
        *session.posargs,
    )


@session(name="Type Checking", python=DEFAULT_PYTHON_VERSION)
def type_checking(session: Session) -> None:
    session.run_always("poetry", "install", external=True)
    args = session.posargs or CODE_DIRECTORIES
    session.run("mypy", f"--python-executable={sys.executable}", *args)


@session(name="Build Docs", python=DEFAULT_PYTHON_VERSION)
def build_docs(session: Session) -> None:
    session.install("mkdocs", "mkdocs-material")
    session.run("mkdocs", "build", *session.posargs)


@session(name="Serve Docs", python=DEFAULT_PYTHON_VERSION)
def serve_docs(session: Session) -> None:
    session.install("mkdocs", "mkdocs-material")
    session.run("mkdocs", "serve", *session.posargs)
