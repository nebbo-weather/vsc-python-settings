FROM --platform=linux/x86_64 python:3.11-buster

ARG POETRY_VERSION="1.4.2"
ARG POETRY_CACHE_DIR="/tmp/poetry_cache"
ARG TEST_GROUP="test"
ARG VENV_PATH="/.venv"

# Install the apt packages
RUN apt-get update && \
    apt-get install -y vim git curl wget unzip

# Install poetry
RUN pip install --upgrade pip && \
    pip install poetry==${POETRY_VERSION}

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=${POETRY_CACHE_DIR} \ 
    TEST_GROUP=${TEST_GROUP}

COPY pyproject.toml ./

# Install pip dependencies
RUN poetry install --no-root --with ${TEST_GROUP} && \
    rm -rf ${POETRY_CACHE_DIR}

# Add the virtual environment to the path.
ENV PATH="${VENV_PATH}/bin:$PATH" \
    VIRTUAL_ENV=${VENV_PATH}