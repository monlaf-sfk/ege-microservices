from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from api_service.src.config import settings
from api_service.src.routes import users, scores


app = FastAPI(title="EGE Scoring API")

app.include_router(users.router, prefix="/api/v1")
app.include_router(scores.router, prefix="/api/v1")

register_tortoise(
    app,
    db_url=settings.DATABASE_URL,
    modules={"models": ["api_service.src.models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "db": "connected"}