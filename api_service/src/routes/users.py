from fastapi import APIRouter, HTTPException

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