from nox_poetry import Session, session

PYTHON_VERSIONS = ("3.9",)
DEFAULT_PYTHON_VERSION = "3.9"
DEFAULT_SESSIONS = ("Check Code Format", "Unit Tests")


@session(name="Check Code Format", python=DEFAULT_PYTHON_VERSION)
def format(session: Session) -> None:
    session.install("black")
    session.run("black", "src/{{cookiecutter.project_name}}", "notebooks")


@session(name="Unit Tests", python=PYTHON_VERSIONS)
def unit_test(session: Session) -> None:
    session.install(".")
