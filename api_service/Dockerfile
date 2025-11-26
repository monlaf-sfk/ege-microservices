FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY shared/pyproject.toml ./shared/
COPY api_service/pyproject.toml ./api_service/
COPY tg_bot_service/pyproject.toml ./tg_bot_service/
COPY vk_bot_service/pyproject.toml ./vk_bot_service/

RUN uv sync --frozen --no-dev --package ege-api

COPY shared/src ./shared/src
COPY api_service/ ./api_service/

ENV PYTHONPATH=/app/shared/src
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "--package", "ege-api", "uvicorn", "api_service.src.main:app", "--host", "0.0.0.0", "--port", "8000"]