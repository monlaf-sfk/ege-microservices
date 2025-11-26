from vkbottle.bot import BotLabeler, Message
from vk_bot.states import RegistrationState
from vk_bot.loader import api_client, bot
from vk_bot.keyboard import get_menu_kb
from loguru import logger
import sys

labeler = BotLabeler()

logger.remove()
logger.add(sys.stderr, level="INFO")

@labeler.message(text="Регистрация")
async def start_reg(message: Message):
    logger.info(f"VK User {message.from_id} started registration")
    await message.answer("Введите ваше Имя и Фамилию:")
    await bot.state_dispenser.set(message.peer_id, RegistrationState.NAME)


@labeler.message(state=RegistrationState.NAME)
async def process_name(message: Message):
    parts = message.text.split()
    if len(parts) < 1:
        await message.answer("Нужно ввести хотя бы имя!")
        return

    first_name = parts[0]
    last_name = parts[1] if len(parts) > 1 else None

    try:
        user = await api_client.register_user(message.from_id, first_name, last_name)
        logger.success(f"User {message.from_id} registered successfully. ID: {user.id}")

        await message.answer(f"✅ Вы зарегистрированы как {user.first_name}!", keyboard=get_menu_kb())
    except Exception as e:
        logger.error(f"Registration failed for {message.from_id}: {e}")
        await message.answer(f"❌ Ошибка: {e}", keyboard=get_menu_kb())

    await bot.state_dispenser.delete(message.peer_id)