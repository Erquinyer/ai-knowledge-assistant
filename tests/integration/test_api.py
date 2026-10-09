import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_health() -> None:
    """T-02: GET /health retorna HTTP 200."""

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.get(
            "/health"
        )

    assert response.status_code == 200

    assert (
        response.json()["status"]
        == "ok"
    )


@pytest.mark.asyncio
async def test_chat_ok() -> None:
    """T-03: POST /api/v1/chat con pregunta válida retorna HTTP 200."""

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.post(
            "/api/v1/chat",
            json={
                "question":
                    "Explícame Pydantic"
            },
        )

    assert response.status_code == 200

    assert (
        response.json()["provider"]
        == "bootstrap-local"
    )


@pytest.mark.asyncio
async def test_chat_rejects_short_question() -> None:
    """T-04: pregunta demasiado corta retorna HTTP 422."""

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.post(
            "/api/v1/chat",
            json={
                "question": "a"
            },
        )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_info() -> None:
    """T-05: GET /api/v1/info retorna HTTP 200 y llm_enabled = false."""

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.get(
            "/api/v1/info"
        )

    assert response.status_code == 200

    body = response.json()

    assert body["llm_enabled"] is False
    assert body["name"] == "AI Knowledge Assistant"
