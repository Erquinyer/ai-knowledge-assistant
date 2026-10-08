from fastapi import APIRouter

from app.schemas.info import AppInfo


router = APIRouter(
    prefix="/api/v1/info",
    tags=["info"],
)


@router.get(
    "",
    response_model=AppInfo,
)
async def info() -> AppInfo:
    return AppInfo(
        name="AI Knowledge Assistant",
        version="0.1.0",
        environment="development",
        llm_enabled=False,
    )
