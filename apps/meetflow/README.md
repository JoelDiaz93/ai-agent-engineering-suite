# MeetFlow AI

Procesador inteligente de reuniones.

## Objetivo

Esta es una implementación propia orientada a portafolio. El dominio está desacoplado del proveedor LLM para permitir pruebas locales.

## Arquitectura

```text
Audio/Text → transcription adapter → participants → topics → decisions/actions → minutes → executive summary.
```

## Alcance MVP

- Procesar texto de reunión sin proveedor externo en demo.
- Extraer participantes, temas y acciones.
- Generar minuta y resumen.
- Preparado para añadir Whisper y Calendar/Jira.

## Ejecutar

Desde la raíz del repositorio:

```bash
python -m apps.meetflow.main
```

## Evolución

1. Sustituir adaptadores demo por integraciones reales.
2. Añadir persistencia PostgreSQL/pgvector.
3. Exponer FastAPI.
4. Añadir autenticación, observabilidad y evaluaciones.
5. Construir UI y demo pública.

## Seguridad

No usar documentos, correos, CV, credenciales ni incidentes reales en el repositorio. Los ejemplos deben ser sintéticos.
