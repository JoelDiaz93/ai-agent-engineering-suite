# InboxPilot AI

Asistente de operaciones de correo.

## Objetivo

Esta es una implementación propia orientada a portafolio. El dominio está desacoplado del proveedor LLM para permitir pruebas locales.

## Arquitectura

```text
Message → classify → priority → context → draft → human approval → provider adapter.
```

## Alcance MVP

- Clasificar mensajes.
- Priorizar.
- Generar borradores, nunca enviar automáticamente en el MVP.
- Conservar thread/reference metadata.

## Ejecutar

Desde la raíz del repositorio:

```bash
python -m apps.inboxpilot.main
```

## Evolución

1. Sustituir adaptadores demo por integraciones reales.
2. Añadir persistencia PostgreSQL/pgvector.
3. Exponer FastAPI.
4. Añadir autenticación, observabilidad y evaluaciones.
5. Construir UI y demo pública.

## Seguridad

No usar documentos, correos, CV, credenciales ni incidentes reales en el repositorio. Los ejemplos deben ser sintéticos.
