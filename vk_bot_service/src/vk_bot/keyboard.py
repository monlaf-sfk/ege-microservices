from ege_shared.consts import SUBJECT_NAMES
from vkbottle import Keyboard, Text, KeyboardButtonColor
from ege_shared.schemas import SubjectEnum


def get_menu_kb():
    return (
        Keyboard(one_time=False)
        .add(Text("Регистрация"), color=KeyboardButtonColor.PRIMARY)
        .row()
        .add(Text("Добавить баллы"), color=KeyboardButtonColor.POSITIVE)
        .add(Text("Мои баллы"), color=KeyboardButtonColor.SECONDARY)
    )


def get_subjects_kb():
    kb = Keyboard(one_time=True)
    for subject in SubjectEnum:
        kb.add(Text(SUBJECT_NAMES[subject]))
        kb.row()
    return kb