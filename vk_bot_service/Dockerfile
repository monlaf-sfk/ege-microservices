FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY shared/pyproject.toml ./shared/
COPY api_service/pyproject.toml ./api_service/
COPY tg_bot_service/pyproject.toml ./tg_bot_service/
COPY vk_bot_service/pyproject.toml ./vk_bot_service/

RUN uv sync --frozen --no-dev --package vk-bot-service

COPY shared/src ./shared/src
COPY vk_bot_service/ ./vk_bot_service/

ENV PYTHONPATH=/app/shared/src
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "--package", "vk-bot-service", "python", "-m", "vk_bot.main"]