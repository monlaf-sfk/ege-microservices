from vkbottle.bot import Bot
from vkbottle import CtxStorage
from vk_bot.config import settings
from vk_bot.client import APIClient


bot = Bot(token=settings.VK_BOT_TOKEN)

api_client = APIClient(base_url=settings.API_BASE_URL)

ctx = CtxStorage()