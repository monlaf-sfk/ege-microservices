
# 📚 EGE Scoring System (Microservices)

Микросервисная система для сбора и учета баллов ЕГЭ.
Проект реализует чистую архитектуру (Clean Architecture) с разделением на Backend API и Frontend (Telegram и VK Бот)

## 🚀 Особенности архитектуры

Проект построен как **Monorepo** с использованием пакетного менеджера **uv** и **Workspaces**.

  * **`api_service`**: REST API на **FastAPI**. Единая точка входа для всех данных.
  * **`tg_bot_service`**: Асинхронный бот на **aiogram 3.x**.
  * **`vk_bot_service`**: Асинхронный бот на **vkbottle**.
  * **`shared`**: Общая библиотека (Shared Kernel). Содержит Pydantic-схемы (DTO) и константы, используемые всеми сервисами.
  * **Database**: PostgreSQL + **Tortoise ORM**.
  * **Migrations**: Управление схемой БД через **Aerich**.

## 🛠 Технический стек

  * **Язык:** Python 3.11+
  * **Package Manager:** `uv` (c использованием Workspaces)
  * **Web Framework:** FastAPI
  * **Bots:** Aiogram 3 (Telegram), VKBottle (VK)
  * **Database:** PostgreSQL 15
  * **ORM:** Tortoise ORM (async)
  * **Migrations:** Aerich
  * **Containerization:** Docker, Docker Compose
  * **Testing:** Pytest, HTTPX (AsyncClient)
  * **Logging:** Loguru

-----

## 🐳 Быстрый запуск (Docker)

Для запуска всего стека (БД + API + Боты) требуется только Docker.

1.  **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/monlaf-sfk/ege-microservices.git
    cd ege-microservices
    ```

2.  **Создайте файл `.env`:**
    В корне проекта создайте файл `.env` и заполните его:

    ```env
    # Database
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_NAME=ege_db
    DB_HOST=db
    DB_PORT=5432

    # Telegram Bot
    BOT_TOKEN=your_telegram_bot_token

    # VK Bot
    VK_BOT_TOKEN=your_vk_community_token
    ```

3.  **Запустите через Docker Compose:**

    ```bash
    docker compose up --build
    ```

После запуска:

  * **API Docs (Swagger):** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
  * **Telegram Bot:** Запущен и готов к работе.
  * **VK Bot:** Запущен и слушает Long Poll.

-----

## 💻 Локальная разработка

Если вы хотите запустить сервисы без Docker (используя `uv`).

1.  **Установите зависимости:**

    ```bash
    uv sync --all-packages
    ```

2.  **Поднимите базу данных:**

    ```bash
    docker compose up -d db
    ```

3.  **Примените миграции:**

    ```bash
    uv run --package ege-api aerich -c api_service/pyproject.toml init-db
    ```

4.  **Запустите сервисы:**

      * **API:**

        ```bash
        PYTHONPATH=shared/src uv run --package ege-api uvicorn api_service.src.main:app --reload
        ```

      * **Telegram Bot:**

        ```bash
        PYTHONPATH=shared/src uv run --package tg-bot-service python -m tg_bot_service.src.main
        ```

      * **VK Bot:**

        ```bash
        PYTHONPATH=shared/src uv run --package vk-bot-service python -m vk_bot_service.src.main
        ```

-----

## 🧪 Тестирование

Проект покрыт интеграционными тестами

Запуск тестов:

```bash
PYTHONPATH=shared/src uv run --package ege-api pytest -c api_service/pyproject.toml
```

-----

## 📂 Структура проекта

```text
.
├── api_service/          # Бэкенд (FastAPI)
├── tg_bot_service/       # Интерфейс Telegram
├── vk_bot_service/       # Интерфейс ВКонтакте
├── shared/               # Общие Pydantic схемы и утилиты
├── docker-compose.yml    # Оркестрация
├── pyproject.toml        # Конфигурация Workspace
└── uv.lock               # Единый лок-файл зависимостей
```
