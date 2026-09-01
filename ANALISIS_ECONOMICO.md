# Análisis económico — TP 02

## Cómo se mide

`scripts/run_agent.py` es la única fuente de estos números: llama a la API de Anthropic con `prompts/system_prompt.md` como system prompt y un caso de `prompts/casos/` como input, y guarda `usage.input_tokens` / `usage.output_tokens` reales de la respuesta en la cabecera de cada archivo de `corridas/raw/`. No se estiman tokens contando palabras — el propio agente tiene la restricción de no inventar cifras (BoM), y este análisis sigue el mismo criterio: si no hay una corrida real que lo respalde, se deja marcado como pendiente en vez de inventarlo.

**Estado actual: pendiente de ejecución.** Este entorno no tiene una `ANTHROPIC_API_KEY` configurada, así que la tabla de abajo todavía no tiene datos reales. Para completarla:

```bash
pip install -r scripts/requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
python scripts/run_agent.py prompts/casos/solicitud_001_acme.md --model claude-sonnet-5
python scripts/run_agent.py prompts/casos/solicitud_002_synnex.md --model claude-sonnet-5
python scripts/run_agent.py prompts/casos/solicitud_003_bmining.md --model claude-sonnet-5
```

Repetir con `--model claude-haiku-4-5` para la comparación de modelo de la sección siguiente. Cada corrida imprime y guarda el costo real; completar la tabla con esos valores.

## Precios usados (API de Anthropic, USD por millón de tokens)

| Modelo | Input | Output |
| --- | --- | --- |
| `claude-haiku-4-5` | $1.00 | $5.00 |
| `claude-sonnet-5` | $2.00 | $10.00 |

## Costo por corrida

| Caso | Modelo | Tokens in | Tokens out | Costo (USD) |
| --- | --- | --- | --- | --- |
| Solicitud 001 (ACME) | `claude-sonnet-5` | *pendiente* | *pendiente* | *pendiente* |
| Solicitud 002 (SYNNEX) | `claude-sonnet-5` | *pendiente* | *pendiente* | *pendiente* |
| Solicitud 003 (BMINING) | `claude-sonnet-5` | *pendiente* | *pendiente* | *pendiente* |
| **Promedio** | `claude-sonnet-5` | *pendiente* | *pendiente* | *pendiente* |

## Elección de modelo — "el más chico que hace bien la tarea"

El criterio del curso pide el modelo más chico que resuelva la tarea, no el más capaz disponible. Este flujo (6 fases de análisis y redacción sobre texto, sin cálculo numérico ni tool-calling complejo) es candidato a un modelo más chico que Sonnet.

Plan de comparación (a ejecutar con el runner, mismo caso, mismo `system_prompt.md`, dos modelos):

1. Correr los 3 casos con `claude-haiku-4-5` y con `claude-sonnet-5`.
2. Revisar el output de Haiku con el mismo criterio que se usó en las 3 corridas documentadas en `corridas/`: ¿distingue hechos de supuestos?, ¿respeta las restricciones (no protección por defecto, no precios inventados, excepción de proveedor)?, ¿aplica bien los criterios de escalación?
3. Si Haiku sostiene la calidad en los 3 casos, es la elección justificada por el criterio del curso — es ~2-3× más barato que Sonnet en input/output. Si falla en algún punto de los ya verificados en las 3 corridas (los más propensos a fallar, según `DECISIONES.md`), se documenta acá cuál fue el fallo concreto y se justifica Sonnet como necesario, no como default.

*Pendiente de completar con el resultado real de esa comparación — no se asume de antemano cuál modelo gana.*

## Proyección de costo (semanal / anual)

**Supuesto de volumen** (a ajustar si no representa el caso real): un SE procesa aproximadamente **5 oportunidades nuevas por semana** que ameritan correr el flujo completo (Fases 1–6), más una cantidad similar de re-corridas por iteración dentro de la misma oportunidad (información que llega incompleta y se reprocesa) — estimar un **factor de 2 corridas por oportunidad**.

| Período | Corridas | Costo estimado (USD) |
| --- | --- | --- |
| Por semana | 5 oportunidades × 2 corridas = 10 | *pendiente* (= 10 × costo promedio por corrida) |
| Por año (48 semanas hábiles) | 480 | *pendiente* (= 480 × costo promedio por corrida) |

Esta proyección no incluye el costo de un eventual SE humano revisando cada salida (tiempo de revisión), que es el costo dominante del sistema en producción — el agente reduce el tiempo de primer borrador, no lo reemplaza (ver [`GOBIERNO.md`](GOBIERNO.md)).
