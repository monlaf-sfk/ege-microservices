import time
from fastapi import FastAPI , Request
from tortoise.contrib.fastapi import register_tortoise
from api_service.src.config import settings
from api_service.src.routes import users, scores
from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)
app = FastAPI(title="EGE Scoring API")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    logger.info(f"Incoming Request: {request.method} {request.url.path}")

    try:
        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        logger.info(f"Completed: {response.status_code} | Time: {process_time:.2f}ms")
        return response
    except Exception as e:
        logger.exception("Request failed")
        raise e

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
    logger.debug("Health check called")
    return {"status": "ok", "db": "connected"}