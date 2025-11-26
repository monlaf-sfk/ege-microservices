from aiogram.fsm.state import StatesGroup, State

class RegistrationState(StatesGroup):
    waiting_for_name = State()

class ScoreState(StatesGroup):
    waiting_for_subject = State()
    waiting_for_score = State()