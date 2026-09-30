# Publicación en GitHub

## 1. Preparar el repositorio

```bash
git init
git add .
git commit -m "feat: initial AI engineering suite"
git branch -M main
```

## 2. Crear el repositorio remoto

En GitHub crea un repositorio vacío llamado `ai-agent-engineering-suite`. No agregues README ni `.gitignore` desde GitHub porque ya existen localmente.

```bash
git remote add origin <URL-DE-TU-REPOSITORIO>
git push -u origin main
```

## 3. Antes de cada push

```bash
python -m compileall apps labs shared
pytest
```

Nunca publiques `.env`, tokens, bases de datos locales, CV reales, contratos reales, correos ni información de incidentes. Usa únicamente datos sintéticos en demos.

## 4. Estrategia de ramas

- `main`: versión estable.
- `feature/<nombre>`: funcionalidades.
- `fix/<nombre>`: correcciones.
- Pull Request para integrar cambios relevantes.

## 5. Releases

Usa SemVer: `v0.1.0` para MVP técnico, `v0.2.0` al incorporar una funcionalidad compatible y `v1.0.0` cuando exista una versión demostrable y documentada de extremo a extremo.
