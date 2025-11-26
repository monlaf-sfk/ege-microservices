from fastapi import APIRouter, HTTPException, Query

from api_service.src.services import user_service
from ege_shared.schemas import UserResponse, UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponse)
async def register(user_in: UserCreate):
    try:
        user_in.validate_ids()
        return await user_service.register_user(user_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/check", response_model=UserResponse)
async def check_user(
    telegram_id: int | None = Query(None),
    vk_id: int | None = Query(None)
):
    user = await user_service.get_user(telegram_id=telegram_id, vk_id=vk_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user