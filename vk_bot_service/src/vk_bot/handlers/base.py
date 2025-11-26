from vkbottle.bot import BotLabeler, Message
from vk_bot.keyboard import get_menu_kb

labeler = BotLabeler()

@labeler.message(text=["Начать", "Start", "/start"])
async def start_handler(message: Message):
    await message.answer(
        "Привет! Я VK-бот для ЕГЭ.\nВыберите действие:",
        keyboard=get_menu_kb()
    )