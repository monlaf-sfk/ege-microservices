from pydantic import BaseModel, ConfigDict, Field
from ege_shared.consts import SubjectEnum


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


class ScoreBase(BaseModel):
    subject: SubjectEnum
    score: int = Field(..., ge=0, le=100)

class ScoreCreate(ScoreBase):
    user_telegram_id: int | None = None
    user_vk_id: int | None = None

class ScoreResponse(ScoreBase):
    id: int
    model_config = ConfigDict(from_attributes=True)