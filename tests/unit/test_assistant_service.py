import pytest

from app.services.assistant_service import (
    BootstrapAssistantService,
)


@pytest.mark.asyncio
async def test_returns_known_answer() -> None:
    """T-01: el servicio responde correctamente a una pregunta conocida."""

    service = BootstrapAssistantService()

    response = await service.answer(
        "¿Qué es FastAPI?"
    )

    assert (
        response.provider
        == "bootstrap-local"
    )

    assert (
        "framework"
        in response.answer.lower()
    )


@pytest.mark.asyncio
async def test_returns_fallback_answer_for_unknown_question() -> None:
    service = BootstrapAssistantService()

    response = await service.answer(
        "¿Cuál es la capital de Francia?"
    )

    assert response.provider == "bootstrap-local"
    assert "LLM" in response.answer
