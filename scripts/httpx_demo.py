"""Demostración de consumo asíncrono de la API con HTTPX.

Requiere que la API esté corriendo en http://127.0.0.1:8000
(por ejemplo con: fastapi dev app/main.py).

Ejecución: python scripts/httpx_demo.py
"""

import asyncio

import httpx


async def main() -> None:
    async with httpx.AsyncClient(
        base_url="http://127.0.0.1:8000",
        timeout=5.0,
    ) as client:

        health_response = await client.get(
            "/health"
        )

        print(
            "Health:",
            health_response.json(),
        )

        chat_response = await client.post(
            "/api/v1/chat",
            json={
                "question": "¿Qué es AsyncIO?"
            },
        )

        print(
            "Chat:",
            chat_response.json(),
        )

        info_response = await client.get(
            "/api/v1/info"
        )

        print(
            "Info:",
            info_response.json(),
        )


if __name__ == "__main__":
    asyncio.run(main())
