from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from ege_shared.schemas import SubjectEnum


def get_subjects_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    for subject in SubjectEnum:
        builder.button(text=subject.value)

    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)