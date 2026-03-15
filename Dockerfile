FROM python:3.14.0rc-slim
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml README.md /app/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
COPY src /app/src
CMD ["python", "-m", "bot.main", "run"]
