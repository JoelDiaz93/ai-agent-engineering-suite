# MemoryMesh AI

Asistente multiusuario con memoria híbrida.

## Objetivo

Esta es una implementación propia orientada a portafolio. El dominio está desacoplado del proveedor LLM para permitir pruebas locales.

## Arquitectura

```text
Session input → short-term window → semantic/persistent memory → context builder → model → memory extraction.
```

## Alcance MVP

- Mantener contexto por conversación.
- Persistir hechos útiles por usuario.
- Separar memoria conversacional de conocimiento documental.
- Permitir inspección/borrado de memoria.

## Ejecutar

Desde la raíz del repositorio:

```bash
python -m apps.memorymesh.main
```

## Evolución

1. Sustituir adaptadores demo por integraciones reales.
2. Añadir persistencia PostgreSQL/pgvector.
3. Exponer FastAPI.
4. Añadir autenticación, observabilidad y evaluaciones.
5. Construir UI y demo pública.

## Seguridad

No usar documentos, correos, CV, credenciales ni incidentes reales en el repositorio. Los ejemplos deben ser sintéticos.
