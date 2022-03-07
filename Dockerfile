FROM python:3.8-buster

RUN mkdir -p /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./ /app/

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
COPY ./pyproject.toml  /app/
ENV PATH=/root/.poetry/bin:${PATH}
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8000

VOLUME [ "/app/public/media" ]
VOLUME [ "/app/public/static" ]

RUN chmod 755 /app/public/static

CMD [ "gunicorn", "--workers", "12", "--max-requests", "1000", "--timeout", "200", "--bind", "0.0.0.0:8000", "config.wsgi:application" ]
