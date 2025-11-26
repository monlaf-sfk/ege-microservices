from vkbottle.bot import BotLabeler, Message
from vk_bot.states import ScoreState
from vk_bot.loader import api_client, bot, ctx
from vk_bot.keyboard import get_menu_kb, get_subjects_kb
from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, level="INFO")

labeler = BotLabeler()

async def ensure_registered(message: Message) -> bool:
    is_registered = await api_client.check_user_exists(vk_id=message.from_id)
    if not is_registered:
        await message.answer("⛔️ Сначала нажмите кнопку 'Регистрация'!", keyboard=get_menu_kb())
        return False
    return True


@labeler.message(text="Добавить баллы")
async def start_score(message: Message):
    if not await ensure_registered(message):
        return

    await message.answer("Выберите предмет:", keyboard=get_subjects_kb())
    await bot.state_dispenser.set(message.peer_id, ScoreState.SUBJECT)


@labeler.message(state=ScoreState.SUBJECT)
async def process_subject(message: Message):
    ctx.set(message.peer_id, {"subject": message.text})
    await message.answer("Введите балл (0-100):")
    await bot.state_dispenser.set(message.peer_id, ScoreState.SCORE)


@labeler.message(state=ScoreState.SCORE)
async def process_score_value(message: Message):
    if not message.text.isdigit():
        await message.answer("Введите число!")
        return

    score = int(message.text)
    data = ctx.get(message.peer_id)
    subject = data.get("subject")

    try:
        await api_client.add_score(message.from_id, subject, score)
        logger.info(f"Score added for {message.from_id}: {subject} - {score}")
        await message.answer(f"✅ Балл сохранен!", keyboard=get_menu_kb())
    except Exception as e:
        logger.error(f"Failed to add score for {message.from_id}: {e}")
        await message.answer(f"❌ Ошибка: {e}", keyboard=get_menu_kb())

    await bot.state_dispenser.delete(message.peer_id)



@labeler.message(text="Мои баллы")
async def view_scores(message: Message):
    if not await ensure_registered(message):
        return

    try:
        scores = await api_client.get_my_scores(message.from_id)
        if not scores:
            await message.answer("Баллов пока нет.", keyboard=get_menu_kb())
            return

        text = "📊 Ваши баллы:\n"
        for s in scores:
            text += f"• {s.subject.value}: {s.score}\n"
        await message.answer(text, keyboard=get_menu_kb())
    except Exception as e:
        await message.answer(f"Ошибка: {e}", keyboard=get_menu_kb())