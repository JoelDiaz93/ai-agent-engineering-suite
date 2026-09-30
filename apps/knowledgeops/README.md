# KnowledgeOps AI

Motor RAG reutilizable y multi-dominio.

## Objetivo

Esta es una implementación propia orientada a portafolio. El dominio está desacoplado del proveedor LLM para permitir pruebas locales.

## Arquitectura

```text
Document → loader → chunker → embedding/index → retriever → grounded generation → sources.
```

## Alcance MVP

- Ingestar documentos.
- Recuperar evidencia.
- Responder con fuentes.
- Soportar dominios legal, soporte y RRHH mediante configuración.

## Ejecutar

Desde la raíz del repositorio:

```bash
python -m apps.knowledgeops.main
```

## Evolución

1. Sustituir adaptadores demo por integraciones reales.
2. Añadir persistencia PostgreSQL/pgvector.
3. Exponer FastAPI.
4. Añadir autenticación, observabilidad y evaluaciones.
5. Construir UI y demo pública.

## Seguridad

No usar documentos, correos, CV, credenciales ni incidentes reales en el repositorio. Los ejemplos deben ser sintéticos.
