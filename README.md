# AI Knowledge Assistant — Bootstrap API

Primer incremento funcional del asistente empresarial de conocimiento.
Mini-proyecto evaluable — Módulo 0 (Preparación del entorno de Ingeniería de IA).

> **Importante:** este incremento **no** integra ningún proveedor LLM real.
> El `provider` devuelto por el chat es `bootstrap-local`, una implementación
> local que demuestra los contratos, la validación y la separación de
> responsabilidades sobre la que se conectará un LLM en un módulo posterior.

## 1. Requisitos

- Python 3.12 o superior
- pip

## 2. Instalación

```bash
# 1. Crear el entorno virtual
python3 -m venv .venv

# 2. Activarlo
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# 3. Instalar el proyecto en modo editable + dependencias de desarrollo
pip install -e ".[dev]"
```

## 3. Ejecutar la API

```bash
fastapi dev app/main.py
```

La API queda disponible en `http://127.0.0.1:8000`.
Documentación interactiva (Swagger UI): `http://127.0.0.1:8000/docs`.

## 4. Endpoints

| Método | Ruta              | Descripción                                   |
|--------|-------------------|------------------------------------------------|
| GET    | `/health`         | Estado de la aplicación.                       |
| POST   | `/api/v1/chat`    | Envía una pregunta y recibe una respuesta bootstrap. |
| GET    | `/api/v1/info`    | Metadatos básicos del proyecto.                |

### Ejemplo manual con curl

```bash
curl http://127.0.0.1:8000/health

curl -X POST http://127.0.0.1:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "¿Qué es FastAPI?"}'

curl http://127.0.0.1:8000/api/v1/info

# Entrada inválida (menos de 3 caracteres) -> HTTP 422
curl -X POST http://127.0.0.1:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "a"}'
```

## 5. Demostraciones asíncronas (`scripts/`)

```bash
# Concurrencia con AsyncIO (no requiere servidor corriendo)
python scripts/asyncio_demo.py

# Cliente HTTPX asíncrono (requiere la API corriendo en otra terminal)
python scripts/httpx_demo.py
```

## 6. Pruebas

```bash
python -m pytest -q
```

Incluye pruebas unitarias (`tests/unit/`) sobre la capa de servicio y
pruebas de integración (`tests/integration/`) que invocan la aplicación
FastAPI directamente vía `ASGITransport`, sin necesidad de un servidor
externo en ejecución.

## 7. Estructura del proyecto

```
ai-knowledge-assistant/
├── app/
│   ├── main.py                  # Punto de entrada FastAPI
│   ├── api/routes/               # Capa HTTP (routers)
│   │   ├── health.py
│   │   ├── chat.py
│   │   └── info.py
│   ├── schemas/                  # Contratos Pydantic (request/response)
│   │   ├── chat.py
│   │   ├── health.py
│   │   └── info.py
│   └── services/                 # Lógica de negocio, independiente del router
│       └── assistant_service.py
├── scripts/                      # Demostraciones de AsyncIO/HTTPX
├── tests/
│   ├── unit/
│   └── integration/
├── .gitignore
├── pyproject.toml
└── README.md
```

## 8. Flujo de trabajo Git

1. `main` contiene el estado estable del proyecto.
2. El desarrollo del incremento se hizo en la rama `feat/bootstrap-api`.
3. Commits pequeños y coherentes (ver historial con `git log --oneline`).
4. Integración a `main` mediante Pull Request.

## 9. Próximos módulos

Este incremento está preparado para evolucionar sin romper sus contratos:
en módulos posteriores se conectará un proveedor LLM real, RAG, agentes y
observabilidad, reemplazando la implementación interna de
`BootstrapAssistantService` sin tener que modificar el router ni los
schemas expuestos.
