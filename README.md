# AI Agent Engineering Suite

Reimplementación profesional y educativa de los conceptos trabajados en un curso de LangChain, LangGraph, RAG y agentes de IA.

> Este repositorio no pretende ser una copia del material del curso. Los ejemplos fueron reorganizados y reescritos como una suite propia para estudiar arquitectura de sistemas de IA, mantener un portafolio técnico y evolucionar los módulos hacia productos reales.

## Mapa del repositorio

| Módulo | Objetivo | Conceptos principales |
|---|---|---|
| `labs/` | Laboratorio progresivo | tools, estado, routing, memoria, RAG |
| `apps/memorymesh/` | Asistente con memoria híbrida | memoria corta, persistente y semántica |
| `apps/meetflow/` | Inteligencia de reuniones | transcripción, extracción, workflows |
| `apps/knowledgeops/` | Plataforma documental | ingestión, embeddings, retrieval, RAG |
| `apps/supportpilot/` | Helpdesk inteligente | RAG, confianza, Human-in-the-Loop |
| `apps/inboxpilot/` | Automatización de correo | clasificación, drafts, aprobación humana |
| `apps/sentinelops/` | Operaciones de seguridad | supervisor, agentes, enriquecimiento, incidentes |

## Orden recomendado de estudio

1. `labs/01-tools`
2. `labs/02-langgraph`
3. `labs/03-memory`
4. `labs/04-rag`
5. `apps/memorymesh`
6. `apps/meetflow`
7. `apps/knowledgeops`
8. `apps/supportpilot`
9. `apps/inboxpilot`
10. `apps/sentinelops`

## Requisitos

- Python 3.12+
- Git
- Docker (recomendado para las aplicaciones)
- Una API key de un proveedor LLM cuando se active integración real

Cada aplicación tiene su propio README, arquitectura y variables de entorno. Los ejemplos base funcionan sin credenciales usando adaptadores locales/deterministas donde sea posible.

## Filosofía de arquitectura

El dominio no depende directamente de LangChain, LangGraph ni OpenAI. Las integraciones externas se colocan detrás de interfaces/adaptadores. Esto permite cambiar proveedor, probar la lógica sin gastar tokens y mantener responsabilidades separadas.

## GitHub

Consulta [`docs/GITHUB.md`](docs/GITHUB.md) para inicializar el repositorio, crear el primer commit y publicarlo. Consulta [`docs/ROADMAP.md`](docs/ROADMAP.md) para la evolución hacia portafolio/producto.
