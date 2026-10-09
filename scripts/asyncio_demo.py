"""Demostración de concurrencia con AsyncIO.

Compara ejecutar tres tareas de E/S simulada de forma secuencial
(await una a una) contra ejecutarlas de forma concurrente con
asyncio.gather. No depende de la API ni de un servidor en marcha.

Ejecución: python scripts/asyncio_demo.py
"""

import asyncio
import time


async def simulated_request(name: str, seconds: int) -> str:
    print(f"Inicio: {name}")

    await asyncio.sleep(seconds)

    print(f"Fin: {name}")

    return name


async def sequential() -> None:
    await simulated_request("LLM", 1)
    await simulated_request("Vector DB", 1)
    await simulated_request("Metadata API", 1)


async def concurrent() -> None:
    await asyncio.gather(
        simulated_request("LLM", 1),
        simulated_request("Vector DB", 1),
        simulated_request("Metadata API", 1),
    )


async def main() -> None:
    start = time.perf_counter()

    await sequential()

    print(
        f"Secuencial: "
        f"{time.perf_counter() - start:.2f} segundos"
    )

    start = time.perf_counter()

    await concurrent()

    print(
        f"Concurrente: "
        f"{time.perf_counter() - start:.2f} segundos"
    )


if __name__ == "__main__":
    asyncio.run(main())
