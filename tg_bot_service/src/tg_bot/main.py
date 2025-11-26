import asyncio
import logging
from aiogram import Bot, Dispatcher
from tg_bot.config import settings
from tg_bot.handlers import router
from tg_bot.client import APIClient


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()

    api_client = APIClient(base_url=settings.API_BASE_URL)

    dp["api_client"] = api_client

    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")