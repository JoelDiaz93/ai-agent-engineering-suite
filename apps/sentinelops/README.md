# SentinelOps AI

Orquestador multiagente para triage de alertas de seguridad.

## Objetivo

Esta es una implementación propia orientada a portafolio. El dominio está desacoplado del proveedor LLM para permitir pruebas locales.

## Arquitectura

```text
Alert → normalize IOCs → enrichment → verdict → severity/mitigation → human gate → notification.
```

## Alcance MVP

- Normalizar alertas.
- Enriquecer IOC mediante adaptadores.
- Clasificar señal de forma explicable.
- Proponer mitigación.
- Mantener auditoría del flujo.

## Ejecutar

Desde la raíz del repositorio:

```bash
python -m apps.sentinelops.main
```

## Evolución

1. Sustituir adaptadores demo por integraciones reales.
2. Añadir persistencia PostgreSQL/pgvector.
3. Exponer FastAPI.
4. Añadir autenticación, observabilidad y evaluaciones.
5. Construir UI y demo pública.

## Seguridad

No usar documentos, correos, CV, credenciales ni incidentes reales en el repositorio. Los ejemplos deben ser sintéticos.
