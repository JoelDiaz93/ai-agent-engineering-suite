# Arquitectura de la suite

## Principios

1. **Core independiente del proveedor:** el dominio consume interfaces, no SDKs concretos.
2. **Human-in-the-Loop en acciones sensibles:** enviar correo, resolver tickets o responder a incidentes requiere políticas explícitas.
3. **Grounding:** las aplicaciones RAG deben conservar fuente/metadata de la evidencia.
4. **Datos sintéticos:** demos públicas nunca incluyen información real del curso, clientes o usuarios.
5. **Observabilidad:** cada workflow debe poder explicar nodos ejecutados, latencia, modelo y resultado.

## Relación entre proyectos

```text
                  shared contracts/adapters
                         │
        ┌────────────────┼─────────────────┐
        │                │                 │
   MemoryMesh       KnowledgeOps       Agent patterns
                         │                 │
                  ┌──────┴──────┐     ┌────┴─────┐
               SupportPilot  MeetFlow InboxPilot SentinelOps
```

No se plantea un microservicio por cada clase o agente. Los límites se definen por capacidad de negocio.
