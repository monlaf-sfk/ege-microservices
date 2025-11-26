from fastapi import HTTPException
from api_service.src.models import Score, User
from ege_shared.schemas import ScoreCreate


async def add_score(data: ScoreCreate) -> Score:
    """
    Добавляет балл. Если балл по этому предмету уже был — обновляет его.
    """

    user = None
    if data.user_telegram_id:
        user = await User.get_or_none(telegram_id=data.user_telegram_id)
    elif data.user_vk_id:
        user = await User.get_or_none(vk_id=data.user_vk_id)

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден. Сначала зарегистрируйтесь.")

    score, _ = await Score.update_or_create(
        user=user,
        subject=data.subject,
        defaults={"score": data.score}
    )
    return score


async def get_user_scores(telegram_id: int = None, vk_id: int = None) -> list[Score]:
    """
    Получает баллы пользователя по TG ID или VK ID.
    """
    filter_kwargs = {}
    if telegram_id:
        filter_kwargs["telegram_id"] = telegram_id
    elif vk_id:
        filter_kwargs["vk_id"] = vk_id
    else:
        return []

    user = await User.get_or_none(**filter_kwargs)

    if not user:
        return []

    return await Score.filter(user=user).all()