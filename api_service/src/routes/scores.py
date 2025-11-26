from fastapi import APIRouter , HTTPException, Query
from typing import List
from ege_shared.schemas import ScoreCreate, ScoreResponse
from api_service.src.services import score_service

router = APIRouter(prefix="/scores", tags=["Scores"])

@router.post("/", response_model=ScoreResponse)
async def add_score(score_in: ScoreCreate):
    return await score_service.add_score(score_in)

@router.get("/", response_model=List[ScoreResponse])
async def get_scores(
    telegram_id: int | None = Query(None, description="ID пользователя в Telegram"),
    vk_id: int | None = Query(None, description="ID пользователя в VK")
):
    """
    Получить баллы. Нужно передать либо telegram_id, либо vk_id.
    """
    if not telegram_id and not vk_id:
        raise HTTPException(
            status_code=400,
            detail="Необходимо указать либо telegram_id, либо vk_id"
        )
    scores = await score_service.get_user_scores(telegram_id=telegram_id, vk_id=vk_id)
    return scores