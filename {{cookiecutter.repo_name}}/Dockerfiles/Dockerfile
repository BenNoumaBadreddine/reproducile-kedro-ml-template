FROM python:3.9-bullseye

RUN apt-get update

# Install poetry
ENV PATH="${PATH}:/root/.local/bin/poetry" 
RUN curl -sSL https://install.python-poetry.org | python3 -

# install project requirements
COPY poetry.lock pyproject.toml ./
RUN /root/.local/bin/poetry config virtualenvs.create false && \
    /root/.local/bin/poetry install --no-interaction --no-root --no-ansi --with pipelines,training,azure && \
    rm poetry.lock pyproject.toml
