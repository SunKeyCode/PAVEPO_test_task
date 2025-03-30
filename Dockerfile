FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY backend /backend
COPY pyproject.toml /backend
COPY uv.lock /backend

WORKDIR /backend

RUN uv sync --frozen

ENV PYTHONPATH=/backend/src

CMD uv run alembic upgrade head \
&& uv run python src/bootstrap \
&& uv run uvicorn src.main:create_app --factory --host=0.0.0.0
