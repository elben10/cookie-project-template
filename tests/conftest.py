from typing import Generator

import pytest

from pytest_cookies.plugin import Cookies, Result

from tests.utils import inside_dir


@pytest.fixture(scope="session")
def project(cookies_session: Cookies) -> Generator[Result, None, None]:
    result = cookies_session.bake()
    with inside_dir(result.project_path):
        yield result
