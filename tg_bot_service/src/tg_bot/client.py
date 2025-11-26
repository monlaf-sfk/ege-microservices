import aiohttp
from typing import List
from ege_shared.schemas import UserCreate, UserResponse, ScoreCreate, ScoreResponse

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def _post(self, endpoint: str, data: dict):
        """Внутренний метод для POST запросов"""
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{endpoint}"
            async with session.post(url, json=data) as resp:
                resp.raise_for_status()
                return await resp.json()

    async def _get(self, endpoint: str, params: dict = None):
        """Внутренний метод для GET запросов"""
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{endpoint}"
            async with session.get(url, params=params) as resp:
                resp.raise_for_status()
                return await resp.json()



    async def register_user(self, telegram_id: int, first_name: str, last_name: str | None) -> UserResponse:
        payload = UserCreate(
            telegram_id=telegram_id,
            first_name=first_name,
            last_name=last_name
        )

        data = await self._post("/users/register", payload.model_dump(mode='json'))
        return UserResponse(**data)

    async def add_score(self, telegram_id: int, subject: str, score: int) -> ScoreResponse:
        payload = ScoreCreate(
            user_telegram_id=telegram_id,
            subject=subject,
            score=score
        )
        data = await self._post("/scores/", payload.model_dump(mode='json'))
        return ScoreResponse(**data)

    async def get_my_scores(self, telegram_id: int) -> List[ScoreResponse]:
        data = await self._get("/scores/", params={"telegram_id": telegram_id})

        return [ScoreResponse(**item) for item in data]