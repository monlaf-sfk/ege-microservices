from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from tg_bot.states import RegistrationState, ScoreState
from tg_bot.client import APIClient
from tg_bot.keyboards import get_subjects_kb
from ege_shared.schemas import SubjectEnum

router = Router()

async def ensure_registered(message: Message, api_client: APIClient) -> bool:
    is_registered = await api_client.check_user_exists(telegram_id=message.from_user.id)
    if not is_registered:
        await message.answer("⛔️ Сначала нужно зарегистрироваться! Нажмите /register")
        return False
    return True


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот для учета баллов ЕГЭ.\n"
        "Доступные команды:\n"
        "/register - Зарегистрироваться\n"
        "/enter_scores - Добавить баллы\n"
        "/view_scores - Посмотреть мои баллы"
    )



@router.message(Command("register"))
async def cmd_register(message: Message, state: FSMContext):
    await message.answer("Введите ваше Имя и Фамилию (например: Иван Иванов):")
    await state.set_state(RegistrationState.waiting_for_name)


@router.message(RegistrationState.waiting_for_name)
async def process_name(message: Message, state: FSMContext, api_client: APIClient):
    parts = message.text.split()
    first_name = parts[0]
    last_name = parts[1] if len(parts) > 1 else None

    try:
        user = await api_client.register_user(
            telegram_id=message.from_user.id,
            first_name=first_name,
            last_name=last_name
        )
        await message.answer(f"✅ Успешно! Вы зарегистрированы как {user.first_name}.")
    except Exception as e:
        await message.answer(f"❌ Ошибка регистрации: {e}")

    await state.clear()


@router.message(Command("enter_scores"))
async def cmd_enter_scores(message: Message, state: FSMContext , api_client: APIClient):
    if not await ensure_registered(message, api_client):
        return

    await message.answer("Выберите предмет:", reply_markup=get_subjects_kb())
    await state.set_state(ScoreState.waiting_for_subject)


@router.message(ScoreState.waiting_for_subject)
async def process_subject(message: Message, state: FSMContext):
    try:
        selected_subject = next(s for s in SubjectEnum if s.value == message.text)

        await state.update_data(subject=selected_subject.name.lower())
        await state.update_data(subject=selected_subject.value)

        await message.answer("Введите балл (0-100):", reply_markup=ReplyKeyboardRemove())
        await state.set_state(ScoreState.waiting_for_score)
    except StopIteration:
        await message.answer("❌ Пожалуйста, выберите предмет кнопкой.")


@router.message(ScoreState.waiting_for_score)
async def process_score(message: Message, state: FSMContext, api_client: APIClient):
    if not message.text.isdigit():
        await message.answer("Введите число!")
        return

    score = int(message.text)
    if not (0 <= score <= 100):
        await message.answer("Балл должен быть от 0 до 100.")
        return

    data = await state.get_data()
    subject = data['subject']

    try:
        await api_client.add_score(
            telegram_id=message.from_user.id,
            subject=subject,
            score=score
        )
        await message.answer(f"✅ Балл по предмету '{subject}' сохранен: {score}")
    except Exception as e:
        await message.answer(f"❌ Ошибка API: {e}")

    await state.clear()


@router.message(Command("view_scores"))
async def cmd_view_scores(message: Message, api_client: APIClient):
    if not await ensure_registered(message, api_client):
        return
    try:
        scores = await api_client.get_my_scores(telegram_id=message.from_user.id)

        if not scores:
            await message.answer("У вас пока нет сохраненных баллов.")
            return

        text = "📊 <b>Ваши баллы:</b>\n\n"
        total = 0
        for s in scores:
            text += f"• {s.subject.value}: <b>{s.score}</b>\n"
            total += s.score

        text += f"\n🏆 Сумма: <b>{total}</b>"
        await message.answer(text, parse_mode="HTML")

    except Exception as e:
        await message.answer(f"❌ Не удалось получить данные: {e}")