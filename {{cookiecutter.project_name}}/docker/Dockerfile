ARG PYTHON_VERSION=3.8
FROM mcr.microsoft.com/vscode/devcontainers/python:${PYTHON_VERSION}

WORKDIR /project

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /project/

RUN poetry install --no-root

COPY . /project/

RUN poetry install