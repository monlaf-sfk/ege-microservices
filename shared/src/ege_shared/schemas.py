from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=255)
    last_name: str | None = Field(None, max_length=255)


class UserCreate(UserBase):
    telegram_id: int | None = None
    vk_id: int | None = None

    def validate_ids(self):
        if not self.telegram_id and not self.vk_id:
            raise ValueError("Нужен хотя бы один ID (Telegram или VK)")


class UserResponse(UserBase):
    id: int
    telegram_id: int | None
    vk_id: int | None

    model_config = ConfigDict(from_attributes=True)