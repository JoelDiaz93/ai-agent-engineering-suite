# SupportPilot AI

Helpdesk con RAG y escalamiento humano.

## Objetivo

Esta es una implementación propia orientada a portafolio. El dominio está desacoplado del proveedor LLM para permitir pruebas locales.

## Arquitectura

```text
Ticket → classify → retrieve knowledge → confidence gate → AI response OR human review → resolution.
```

## Alcance MVP

- Crear tickets.
- Clasificar consultas.
- Usar conocimiento recuperado.
- Escalar por baja confianza.
- Registrar resolución.

## Ejecutar

Desde la raíz del repositorio:

```bash
python -m apps.supportpilot.main
```

## Evolución

1. Sustituir adaptadores demo por integraciones reales.
2. Añadir persistencia PostgreSQL/pgvector.
3. Exponer FastAPI.
4. Añadir autenticación, observabilidad y evaluaciones.
5. Construir UI y demo pública.

## Seguridad

No usar documentos, correos, CV, credenciales ni incidentes reales en el repositorio. Los ejemplos deben ser sintéticos.
