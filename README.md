# TP 02 — Agente Asistente para Ingenieros de Ventas en Redes Ópticas

Trabajo práctico de la materia "Creación de Agentes de IA" — MADE N-2T, UCEMA, 2026 2T.

**Autor:** Federico Serrizuela

## Qué construí

Un agente asistente para un Optical Network Sales Engineer (SE) de soluciones de transporte de datos por fibra óptica (DWDM, packet-optical, ROADM). El agente toma información cruda de un cliente (notas de reunión, correos, requisitos técnicos) y la lleva a través de un flujo de 6 fases: desde el análisis de requisitos hasta la preparación de la reunión de seguimiento con el cliente, pasando por el análisis de brechas, la evaluación de alternativas de solución, la evaluación de si hay información suficiente para cotizar, y el borrador de una nota de ingeniería.

El repositorio incluye:
- `prompts/system_prompt.md` — el agente en sí (rol, contexto, las 6 fases, restricciones, criterios de escalación y formato de salida fijo).
- `prompts/user_prompt.md` — 3 solicitudes de clientes ficticios (ACME, SYNNEX, BMINING) usadas como casos de prueba.
- `corridas/` — 3 corridas documentadas, cada una corriendo el agente contra uno de los 3 casos, iterando al menos 3 veces sobre errores reales encontrados y aplicando la mejora correspondiente al `system_prompt.md`.
- `DESICIONES.md` — consolidado de todos los cambios aplicados a los archivos de prompt, con el motivo de cada uno, los cambios de alcance, lo que se descartó y las limitaciones del agente.

## Cómo se lo pedí

Se partió del `system_prompt.md` original (un asistente de SE con 6 fases fijas y un formato de salida estructurado) y de 3 solicitudes de cliente con distinto nivel de completitud y distintos tipos de ambigüedad a propósito. Se corrió el agente contra cada solicitud, se revisó la salida buscando errores reales (no solo estéticos: supuestos disfrazados de hechos, preguntas de descubrimiento genéricas que deberían ser específicas, restricciones mal aplicadas, datos inventados, pedidos del cliente sin lugar en el formato de salida), y por cada error encontrado se aplicó un cambio concreto al `system_prompt.md`, se volvió a correr, y se verificó si el error se resolvía. El detalle iteración por iteración está en `corridas/`; el resumen de qué cambió y por qué está en `DESICIONES.md`.

No se usó un template externo para este README más allá de la convención ya usada en el TP grupal anterior del equipo (`../TP-Parcial---Navarro-Peron-Pires-Serrizuela/README.md`), ya que no se encontró ningún archivo `Base.md` en el repositorio ni en la carpeta de la materia.

## Qué hace el agente (resumen del flujo)

1. **Chequeo de inconsistencias** (antes de la Fase 1): revisa la información del cliente en busca de contradicciones internas y las declara, sin resolverlas por su cuenta.
2. **Fase 1 — Análisis de requisitos:** resume objetivos, capacidad, geografía, servicio y plazos.
3. **Fase 2 — Análisis de brechas:** identifica qué información falta (fibra, protección, latencia, requisitos de la aplicación, etc.) y arma preguntas de aclaración.
4. **Fase 3 — Evaluación de la solución:** describe alternativas de arquitectura (y, si el cliente lo pide, alternativas de interconexión con su red existente), con ventajas, limitaciones y riesgos de cada una.
5. **Fase 4 — Preparación para la cotización o estimación:** clasifica la oportunidad como lista / parcialmente lista / no lista, distinguiendo si lo pedido es una cotización formal o una estimación preliminar.
6. **Fase 5 — Nota de ingeniería:** arma un borrador con supuestos, soluciones propuestas, riesgos y próximos pasos.
7. **Fase 6 — Reunión de seguimiento:** prepara objetivo, agenda, mensajes clave y decisiones pendientes del cliente.

El agente ejecuta solo las fases que la información disponible permite, e indica explícitamente dónde se detuvo y por qué — nunca completa una sección con contenido de relleno. Si la oportunidad cae en un criterio de escalación (fibra submarina, rutas transfronterizas, ingeniería fotónica a medida, etc.), lo marca explícitamente en lugar de avanzar con las Fases 3 a 5.

## Cómo correrlo

1. Usar el contenido de `prompts/system_prompt.md` como system prompt de un modelo de lenguaje.
2. Pasarle como mensaje de usuario la información real de un cliente (se puede usar cualquiera de las 3 solicitudes de `prompts/user_prompt.md` como ejemplo).
3. Revisar la salida con el formato fijo que define el propio `system_prompt.md` (Resumen de la oportunidad, Inconsistencias detectadas, Requisitos del cliente, Clasificación de la información, Información faltante, Preguntas de aclaración, Alternativas de solución, etc.).

## Qué funciona

- Distingue con claridad hechos, supuestos y recomendaciones gracias a la sección dedicada agregada en la Corrida 01, en vez de mezclar todo en prosa libre.
- No se compromete con mecanismos de protección, esquemas técnicos o precios que el cliente no confirmó — los dos primeros casos de prueba (ACME y SYNNEX) muestran que, tras las mejoras, el agente deja esos puntos correctamente abiertos como preguntas o supuestos en lugar de inventarlos.
- Detecta y declara inconsistencias explícitas dentro del texto del cliente (caso BMINING, canales "IT#1/OT#1" vs. "IT#1/OT#2") en lugar de elegir una versión en silencio.
- Distingue una cotización formal de una estimación presupuestaria preliminar, y refleja la urgencia declarada por el cliente desde el resumen inicial.
- Da un tratamiento propio (arquitectura, ventajas, limitaciones, riesgos) a pedidos específicos del cliente, como alternativas de interconexión con su red existente, en vez de mezclarlos dentro de otra sección.

## Qué falta o qué falló — limitaciones del agente

- **No procesa diagramas ni archivos reales:** aunque el `Contexto` del system prompt menciona "diagramas de red" como posible input, el agente solo puede razonar sobre texto; un diagrama tiene que transcribirse a información textual para que el agente lo use.
- **No tiene acceso a datos reales** de disponibilidad de fibra, catálogo de producto, precios vigentes ni inventario de red del cliente — cualquier BoM o alternativa de interconexión que arma es estructural, no verificada contra un sistema real (por eso los precios se marcan siempre como "Pendiente de cotización con Producto/Pricing" en vez de inventarse, tras el hallazgo de la Corrida 03).
- **No hace cálculos de ingeniería reales** (presupuesto de potencia óptica, dispersión cromática, etc.); los deja marcados como supuestos de diseño a validar por ingeniería, deliberadamente, en vez de automatizarlos (ver "Qué se descartó" en `DESICIONES.md`).
- **No es determinístico:** al ser un LLM, dos corridas con el mismo input pueden variar levemente en redacción aunque respeten el mismo formato de salida.
- **Solo detecta inconsistencias explícitas dentro del propio texto recibido**, no contradicciones contra el historial real del cliente en un CRM u otro sistema externo.
- **No reemplaza el criterio del Sales Engineer:** toda salida requiere revisión humana antes de convertirse en una nota de ingeniería, propuesta o cotización real enviada a un cliente.

El detalle completo de estas limitaciones, junto con los cambios de alcance aplicados y lo que se descartó a propósito, está en [`DESICIONES.md`](DESICIONES.md).

## Qué aprendí

Que la mayoría de los errores reales de este agente no eran de redacción sino de **ausencia de estructura**: la sección "Restricciones" del prompt original ya pedía cosas razonables (distinguir hechos de supuestos, no asumir información faltante, evitar recomendaciones de proveedor) pero, al no tener un lugar fijo en el formato de salida donde aplicarse, el modelo las cumplía a medias o de forma inconsistente entre corridas. Agregar una sección o un campo específico en el Formato de salida resultó, corrida tras corrida, más efectivo que reforzar la misma instrucción en prosa. También aprendí que una restricción "genérica y segura" (como evitar recomendaciones de proveedor) puede volverse un problema cuando el caso de uso cambia — en la Corrida 03 esa misma restricción, pensada para no inventar recomendaciones, terminó haciendo que el agente evitara citar un dato que el propio cliente había dado; hizo falta una excepción explícita, no una regla más estricta.
