<!--
Caso: solicitud_002_synnex.md
Modelo: claude-sonnet-5
Fecha: 2026-09-01T11:59:56
Tokens de entrada: 4622
Tokens de salida: 12611
Costo estimado de esta corrida (USD): 0.1354
-->

# Resumen de la oportunidad
**Cliente:** SYNNEX Corp
**Fecha de la reunión:** 11 de agosto de 2026
**Tipo de entregable solicitado por el cliente:** Estimación presupuestaria preliminar ("primera propuesta presupuestaria" — no se solicitó explícitamente una cotización formal en firme).
**Urgencia declarada por el cliente:** "en una semana" (a partir del 11-ago-2026).

Nota: el cliente indica que esta reunión incluyó adiciones y cambios respecto a una solicitud inicial. No se nos proporcionó el contenido de esa solicitud inicial, por lo que no es posible verificar consistencia entre ambas versiones. Se trata como información faltante (ver Fase 2), no como inconsistencia confirmada.

# Requisitos del cliente
- Interconectar las 2 oficinas principales del cliente para replicación de Bases de Datos.
- Transporte sobre fibra oscura, distancia aproximada de 58 km.
- Arquitectura con 2 rutas de fibra física/lógicamente independientes.
- La solución debe seguir operando con una sola ruta disponible en caso de corte de fibra (mecanismo de protección no especificado, SLA no especificado).
- Routers Cisco existentes en ambos extremos.
- Velocidad de interfaz óptica no confirmada (1G, 10G o 100G).
- Plazo solicitado: primera propuesta presupuestaria en 1 semana.

# Clasificación de la información
**Hechos:**
- Distancia aproximada entre oficinas: 58 km.
- Medio de transporte solicitado: fibra oscura.
- Requisito de 2 rutas independientes.
- Requisito de continuidad de operación con una sola ruta disponible.
- Existencia de routers Cisco en ambos extremos.
- Plazo solicitado de 1 semana para la primera propuesta presupuestaria.

**Supuestos (a validar, no adoptados como definitivos):**
- Que ambas oficinas cuentan o pueden contratar fibra oscura disponible para 2 rutas físicamente diversas.
- Que "58 km" corresponde a la distancia de la ruta principal y no necesariamente a ambas rutas por igual.
- Que el requisito de sobrevivencia se refiere a continuidad del servicio de replicación, no a un SLA de conmutación específico.

**Recomendaciones:**
- Ninguna recomendación de solución definitiva en esta etapa; se presentan alternativas en la Fase 3, condicionadas a la validación de la información faltante.

# Información faltante
- Ubicaciones/direcciones exactas de ambos sitios.
- Confirmación de disponibilidad de fibra oscura para 2 rutas **físicamente** diversas (no solo lógicamente diversas — trayectos, ductos y postes independientes).
- Distancia y presupuesto óptico (atenuación) de **cada una** de las 2 rutas.
- Características de la fibra (tipo G.652/G.655, empalmes, conectores).
- Infraestructura existente en cada sitio (espacio en rack, energía, puntos de entrada de fibra, paneles de distribución).
- Mecanismo de protección deseado (protección óptica automática, agregación de enlaces en los routers, protocolo de capa 3, etc.) — el cliente mencionó sobrevivencia a fallas pero no el mecanismo.
- SLA / tiempo de conmutación objetivo ante corte de fibra.
- Modelo y capacidad de los routers Cisco existentes; tipo y disponibilidad de ópticas actuales.
- Velocidad(es) real(es) de interfaz requerida(s) y cantidad de circuitos a transportar.
- Expectativas de crecimiento de capacidad a futuro.
- Requisitos de la aplicación de replicación de BD: modo síncrono/asíncrono, tolerancia a latencia, ventanas de mantenimiento permitidas.
- Restricciones de espacio y energía disponibles para equipo de transporte óptico en cada sitio.
- Contenido de la "solicitud inicial" referenciada por el cliente, para verificar consistencia con los cambios comunicados el 11-ago.

# Preguntas de aclaración
1. ¿Cuál es la velocidad de interfaz requerida hoy (1G/10G/100G) y la proyectada a futuro?
2. ¿Las 2 rutas de fibra oscura tienen trayectos físicamente independientes (ductos, postes, derechos de vía distintos), o solo son lógicamente distintas?
3. ¿Cuál es la distancia y el presupuesto óptico estimado de la segunda ruta? ¿Es igual a 58 km o distinta?
4. ¿Qué mecanismo de protección se espera (conmutación óptica automática, agregación de enlaces del lado del router, convergencia de protocolo de enrutamiento)? ¿Existe un tiempo máximo de conmutación aceptable?
5. ¿Cuál es el modelo de los routers Cisco existentes y qué tipo de interfaz óptica soportan actualmente?
6. ¿La replicación de bases de datos es síncrona o asíncrona? ¿Cuál es la tolerancia a latencia de la aplicación?
7. ¿Qué espacio en rack y energía (DC/AC, capacidad en Watts) hay disponible en cada sitio para equipo de transporte óptico?
8. ¿Existen ventanas de mantenimiento permitidas para las pruebas de corte/conmutación?
9. ¿Existe algún rango presupuestario referencial que el cliente tenga en mente?
10. ¿Podría el cliente compartir la solicitud inicial para verificar consistencia con los cambios comunicados en esta reunión?

# Alternativas de solución

## Opción 1 — Óptica gris punto a punto directa sobre fibra oscura
**Descripción:** Conectar las interfaces ópticas de los routers Cisco existentes directamente sobre cada una de las 2 fibras oscuras mediante ópticas grises (SFP/SFP+/QSFP), sin equipo de línea óptica intermedio. Una ruta operaría como primaria y la otra como respaldo (o ambas activas, según capacidad de los routers).
**Ventajas:** Baja complejidad, menor costo inicial, implementación rápida, sin necesidad de plataforma óptica dedicada.
**Limitaciones:** Escalabilidad limitada (cada ruta soporta una sola longitud de onda/interfaz); sin capacidad de agregar servicios adicionales sobre la misma fibra sin nuevas ópticas o pares de fibra dedicados.
**Riesgos técnicos:** A 100G, muchas ópticas grises no alcanzan 58 km sin amplificación; el alcance real depende del presupuesto óptico de cada ruta (pendiente de confirmar). Riesgo de incompatibilidad si la distancia real de alguna ruta excede el alcance soportado por la óptica.
**Riesgos operativos:** La conmutación entre rutas dependería de la convergencia de un protocolo de enrutamiento o mecanismo de link aggregation en los routers Cisco; el tiempo de convergencia no está definido y podría no cumplir con las necesidades de continuidad de la replicación de BD (especialmente si es síncrona).

## Opción 2 — Plataforma de transporte óptico (packet-optical/DWDM) con protección
**Descripción:** Desplegar equipos de transporte óptico (transponder/muxponder) en ambos extremos, interconectados con los routers Cisco mediante interfaces grises hacia el equipo de transporte, el cual se conecta a la fibra oscura en cada una de las 2 rutas. Permite escalabilidad futura (múltiples longitudes de onda/servicios) y mecanismos de protección óptica entre rutas (esquema específico —1+1, OLP, SNCP u otro— pendiente de definir con el cliente).
**Ventajas:** Mayor escalabilidad para crecimiento futuro de capacidad; permite agregar servicios adicionales sin tender nuevas fibras; opciones de protección óptica con tiempos de conmutación típicamente rápidos (a validar según el esquema que se elija); gestión y monitoreo centralizados del enlace óptico.
**Limitaciones:** Mayor costo de equipo e implementación; requiere espacio y energía adicionales en ambos sitios; mayor complejidad de ingeniería y puesta en marcha.
**Riesgos técnicos:** Pendiente validar el presupuesto óptico total de cada ruta para determinar si se requiere amplificación a 58 km, dependiendo del tipo de fibra y pérdidas por empalme/conector.
**Riesgos operativos:** Mayor necesidad de personal capacitado para operar y mantener equipo óptico especializado.

**Consideraciones de implementación (ambas opciones):** coordinación de ventanas de mantenimiento para instalación y pruebas de corte de fibra; pruebas de aceptación end-to-end junto con el equipo responsable de la aplicación de replicación de BD; validación de compatibilidad de ópticas/transceivers con los routers Cisco existentes.

# Evaluación de la preparación para la cotización o estimación
**Estado:** Parcialmente listo.
**Justificación:** Existe información suficiente para plantear arquitecturas alternativas de alto nivel y estructurar una estimación presupuestaria preliminar (ROM) bajo supuestos claramente etiquetados (por ejemplo, escenarios de interfaz 1G/10G/100G). Sin embargo, no hay información suficiente para una cotización formal ni para un BoM confiable: faltan la velocidad de interfaz real, la distancia y presupuesto óptico de cada ruta, la confirmación de diversidad física de las 2 rutas, el mecanismo de protección esperado y las restricciones de espacio/energía en sitio. Se recomienda presentar la ROM como rangos por escenario, dejando explícito que está sujeta a validación de estos puntos pendientes.

# Borrador de la nota de ingeniería
*(Pendiente de revisión y aprobación explícita del Sales Engineer — L3. No usar en pasos posteriores sin esa aprobación.)*

**Resumen de la oportunidad:** SYNNEX Corp solicita una estimación presupuestaria preliminar para interconectar sus 2 oficinas principales (~58 km) mediante fibra oscura en 2 rutas independientes, para soportar replicación de bases de datos, con continuidad operativa ante corte de una ruta. Existen routers Cisco en ambos extremos. Plazo solicitado: 1 semana.

**Requisitos del cliente:** ver sección "Requisitos del cliente" arriba.

**Supuestos de diseño:** Disponibilidad de fibra oscura contratable/propia en 2 rutas; 58 km como referencia de la ruta principal (a confirmar para la segunda ruta); routers Cisco existentes compatibles con ópticas estándar del mercado (a confirmar modelo).

**Solución(es) propuesta(s):** Dos alternativas de arquitectura evaluadas en Fase 3 (óptica gris directa vs. plataforma de transporte óptico con protección), sin recomendación definitiva hasta validar velocidad de interfaz, diversidad física de rutas y mecanismo de protección esperado.

**Cuestiones pendientes:** ver "Información faltante".

**Riesgos:**
- Técnico: viabilidad de alcance óptico a 58 km dependiendo de la velocidad de interfaz final (crítico en escenario 100G con ópticas grises).
- Técnico: diversidad física real de las 2 rutas no confirmada, lo que podría comprometer el objetivo de resiliencia.
- Operativo: mecanismo y tiempo de conmutación ante corte no definidos, con posible impacto en la aplicación de replicación de BD si es síncrona.
- Comercial: plazo de 1 semana es ajustado dado el volumen de información pendiente; se recomienda alinear expectativas con el cliente sobre el nivel de precisión posible en esta primera entrega.

**Próximos pasos recomendados:** Enviar preguntas de aclaración al cliente; obtener confirmación de velocidad de interfaz y diversidad de rutas; preparar escenarios de ROM basados en los supuestos declarados; agendar reunión de seguimiento dentro del plazo solicitado.

# Reunión de seguimiento con el cliente
*(Borrador — nivel de autonomía L2: para revisión del SE antes de coordinar con el cliente.)*

**Objetivo:** Validar con SYNNEX Corp la información crítica pendiente (velocidad de interfaz, mecanismo de protección, diversidad y distancia de las 2 rutas, disponibilidad de fibra oscura) y presentar alternativas de arquitectura a alto nivel para alinear expectativas antes de emitir la estimación presupuestaria preliminar.

**Orden del día:**
1. Repaso de los requisitos capturados el 11-ago-2026.
2. Revisión de preguntas de aclaración pendientes.
3. Presentación de las 2 alternativas de arquitectura a alto nivel.
4. Discusión sobre mecanismo de protección deseado y expectativa de SLA de conmutación.
5. Acuerdo de próximos pasos y cronograma para la entrega de la estimación presupuestaria.

**Temas clave de discusión:**
- La velocidad de interfaz (1G/10G/100G) determina la viabilidad técnica de una conexión directa por óptica gris a 58 km.
- El requisito de "seguir funcionando con una sola ruta" requiere definir el mecanismo de protección para dimensionar correctamente el diseño.
- Necesidad de confirmar diversidad física real de las 2 rutas para garantizar la resiliencia esperada.

**Decisiones requeridas del cliente:**
- Velocidad(es) de interfaz requerida(s) actual y futura.
- Preferencia por protección óptica automática vs. convergencia a nivel de red (routers).
- Confirmación de disponibilidad y diversidad física de las 2 rutas de fibra oscura.
- Modo de replicación de BD (síncrono/asíncrono) y tolerancia a latencia.

**Información que aún se requiere:** ver sección "Información faltante".

**Resultados esperados:** Cliente confirma los datos críticos pendientes; se acuerda fecha de entrega de la estimación presupuestaria preliminar con escenarios claramente etiquetados como supuestos.

# Próximas acciones recomendadas
- El SE debe revisar y aprobar explícitamente las Fases 3, 4 y 5 (nivel L3) antes de usarlas en cualquier paso siguiente, incluyendo la preparación de la reunión de seguimiento.
- Enviar al cliente la lista de preguntas de aclaración antes o durante la próxima reunión.
- Solicitar al cliente la "solicitud inicial" referenciada para verificar consistencia con los cambios comunicados el 11-ago-2026.
- Una vez validados los datos críticos, actualizar la estimación presupuestaria preliminar con escenarios específicos (1G/10G/100G) en lugar de rangos genéricos.
- Agendar la reunión de seguimiento dentro del plazo de 1 semana solicitado por el cliente.