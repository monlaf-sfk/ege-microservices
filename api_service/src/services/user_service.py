from api_service.src.models import User
from ege_shared.schemas import UserCreate


async def register_user(data: UserCreate) -> User:
    """
    Регистрирует пользователя
    """
    filter_kwargs = {}
    if data.telegram_id:
        filter_kwargs["telegram_id"] = data.telegram_id
    elif data.vk_id:
        filter_kwargs["vk_id"] = data.vk_id

    user, created = await User.get_or_create(
        defaults={
            "first_name": data.first_name,
            "last_name": data.last_name
        },
        **filter_kwargs
    )

    if not created:
        user.first_name = data.first_name
        if data.last_name:
            user.last_name = data.last_name
        await user.save()

    return user

async def get_user(telegram_id: int = None, vk_id: int = None) -> User | None:
    filter_kwargs = {}
    if telegram_id:
        filter_kwargs["telegram_id"] = telegram_id
    elif vk_id:
        filter_kwargs["vk_id"] = vk_id
    else:
        return None

    return await User.get_or_none(**filter_kwargs)