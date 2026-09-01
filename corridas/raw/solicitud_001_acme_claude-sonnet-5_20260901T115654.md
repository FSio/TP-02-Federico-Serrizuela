<!--
Caso: solicitud_001_acme.md
Modelo: claude-sonnet-5
Fecha: 2026-09-01T11:56:54
Tokens de entrada: 4544
Tokens de salida: 8133
Costo estimado de esta corrida (USD): 0.0904
-->

# Resumen de la oportunidad
Tipo de entregable solicitado por el cliente: No especificado (ACME solicita "una propuesta" en 3 semanas; no se aclara si es cotización formal o estimación presupuestaria preliminar)
Urgencia declarada por el cliente: "Desea recibir una propuesta en 3 semanas"

# Inconsistencias detectadas
Ninguna detectada en la información proporcionada hasta el momento.

# Requisitos del cliente

- Conectar dos centros de datos separados por aproximadamente 120 km.
- Capacidad total requerida: 400G, con expansión prevista a 800G en un plazo de 2 años.
- Requisito de sobrevivencia ante corte de una sola fibra (mecanismo de protección no especificado; SLA no especificado).
- Routers Cisco existentes en ambos extremos (dato del cliente, no recomendación del asistente); interfaces ópticas utilizadas no identificadas.
- Plazo deseado: propuesta en 3 semanas.

# Clasificación de la información

**Hechos:**
- Distancia aproximada entre sitios: ~120 km.
- Capacidad inicial requerida: 400G.
- Capacidad objetivo a 2 años: 800G.
- Existencia de routers Cisco en ambos extremos.
- Requisito declarado de sobrevivencia a corte de fibra única.
- Plazo solicitado por el cliente: 3 semanas.

**Supuestos:**
- Ninguno aplicado en esta fase; se evita asumir mecanismo de protección, disponibilidad de fibra o tipo de interfaces ópticas.

**Recomendaciones:**
- Ninguna aún; se requiere cerrar brechas de información antes de recomendar una arquitectura específica (ver Fase 3, presentada como alternativas, no como recomendación única).

# Información faltante

- Ubicaciones exactas de los dos centros de datos (direcciones o coordenadas), más allá de la distancia declarada.
- Disponibilidad de fibra: ¿el cliente ya posee o tiene contratada fibra oscura entre los sitios, o requiere que se la provea el proveedor de servicios/carrier?
- Diversidad física de ruta: ¿existen (o pueden contratarse) dos rutas de fibra físicamente diversas entre los sitios? Esto es crítico dado el requisito de sobrevivencia a corte de fibra única.
- Características de la fibra existente (tipo de fibra, atenuación, PMD/CD, edad, número de hilos disponibles, presencia de amplificación existente).
- Mecanismo de protección deseado (no debe asumirse: podría ser protección óptica de línea, restauración fotónica, protección/agregación en el equipo cliente, etc.).
- SLA específico de disponibilidad y tiempo de restauración ante falla.
- Infraestructura existente en ambos sitios (¿hay ya equipos DWDM/ROADM desplegados?, espacio en rack, alimentación DC/AC disponible, capacidad de refrigeración).
- Interfaces ópticas exactas de los routers Cisco (velocidad, form factor, tipo de módulo) y protocolos utilizados (Ethernet nativo, OTN, otros).
- Expectativas de crecimiento más allá de 800G (para dimensionar escalabilidad del sistema fotónico).
- Requisitos de latencia máxima tolerada.
- Restricciones de espacio y energía en los sitios.
- Requisitos de la aplicación que consumirá el servicio (modo de replicación síncrono/asíncrono, tolerancia a latencia, ventanas de corte permitidas para mantenimiento).
- Presupuesto de referencia o rango esperado por el cliente.
- Alcance exacto solicitado: ¿el cliente busca solo el equipo de transporte óptico, o también el servicio de fibra oscura/longitud de onda gestionada?

# Preguntas de aclaración

1. ¿Cuáles son las direcciones específicas de ambos centros de datos?
2. ¿ACME ya cuenta con fibra oscura propia o contratada entre los dos sitios, o se requiere que el proveedor la suministre?
3. ¿Existen (o se pueden obtener) dos rutas de fibra físicamente diversas entre los sitios? Esto determina si la sobrevivencia a corte de fibra se puede resolver a nivel de ruta óptica.
4. Respecto al requisito "debe sobrevivir a un corte en una sola fibra": ¿qué mecanismo de protección tienen en mente (protección óptica de línea, restauración automática, protección en capa de cliente) y cuál es el tiempo máximo de restauración aceptable (SLA)?
5. ¿Qué modelo y tipo de interfaces ópticas tienen instaladas actualmente los routers Cisco en cada extremo (velocidad, form factor)?
6. ¿Existe ya infraestructura DWDM/ROADM desplegada en alguno de los sitios, o esta sería una implementación desde cero?
7. ¿Cuál es el espacio en rack y la capacidad de energía disponible en cada sitio?
8. ¿Cuáles son los requisitos de latencia máxima para la aplicación que usará este enlace?
9. ¿Qué tipo de aplicación consumirá este servicio (por ejemplo, replicación de almacenamiento síncrona/asíncrona) y qué ventanas de mantenimiento son aceptables?
10. ¿El entregable solicitado es una cotización formal con lista de materiales y precios, o una estimación presupuestaria preliminar (ROM)?
11. ¿Existe un presupuesto de referencia o rango esperado para este proyecto?
12. ¿El alcance de la propuesta debe incluir el servicio de fibra oscura/longitud de onda, o solo el equipamiento de transporte óptico?

# Alternativas de solución

Nota: dado que aún no se ha confirmado la diversidad física de ruta ni el mecanismo de protección deseado, las siguientes opciones se presentan como alternativas conceptuales de alto nivel, no como una recomendación definitiva. La elección final depende de las respuestas a las preguntas de aclaración anteriores.

## Opción 1 — Sistema DWDM punto a punto con protección de ruta óptica (requiere rutas de fibra físicamente diversas)
**Descripción:** Sistema DWDM/ROADM desplegado en ambos extremos con dos trayectos de fibra físicamente separados entre los sitios; en caso de corte en una fibra, el tráfico se conmuta o restaura automáticamente por la ruta alterna a nivel óptico.

**Ventajas:**
- Protección a nivel de capa óptica, transparente para el equipo de cliente (routers Cisco).
- Tiempos de restauración típicamente muy rápidos si se usa protección óptica dedicada (1+1).
- Escalable de 400G a 800G añadiendo longitudes de onda o incrementando velocidad por canal, sujeto a la capacidad calificada de la plataforma.

**Limitaciones:**
- Requiere disponibilidad confirmada de dos rutas de fibra físicamente diversas; si no existen, esta opción no es viable sin obra civil adicional.
- Mayor costo relativo (duplicación de fibra/equipos de línea).

**Riesgos:**
- Riesgo técnico: sin confirmación de diversidad física real (no solo lógica), el "corte de fibra única" podría dejar sin protección si ambas rutas comparten un mismo ducto o derecho de vía.
- Riesgo operativo: dependencia de terceros (proveedor de fibra) para garantizar y mantener la diversidad de ruta a largo plazo.

## Opción 2 — Sistema DWDM punto a punto con protección en capa de cliente (sobre una única ruta de fibra o rutas no confirmadas como diversas)
**Descripción:** Sistema DWDM desplegado sobre la(s) ruta(s) de fibra disponible(s), con el mecanismo de resiliencia implementado a nivel de los routers Cisco existentes (por ejemplo, enlaces redundantes lógicos, balanceo/failover a nivel L2/L3), en lugar de protección óptica dedicada.

**Ventajas:**
- Menor costo de infraestructura óptica (no requiere necesariamente ruta física diversa a nivel de línea, si el cliente asume el riesgo o gestiona la resiliencia en otra capa).
- Aprovecha capacidades ya existentes en los routers Cisco del cliente.

**Limitaciones:**
- No resuelve por sí sola el requisito de "sobrevivir a un corte en una sola fibra" si toda la capacidad transita por una única traza física; en ese caso, cualquier protección en capa de cliente sería inútil ante un corte físico del único trayecto.
- Depende de que el equipo Cisco tenga las interfaces y licencias adecuadas para implementar el mecanismo elegido.

**Riesgos:**
- Riesgo técnico alto: esta opción solo es válida si existe una segunda ruta física independiente en algún punto de la red del cliente (no solo protección lógica en un único ducto).
- Riesgo operativo: mayor complejidad de coordinación entre la capa óptica y la capa de cliente para garantizar el failover esperado.

**Nota importante:** No se debe seleccionar ninguna de estas opciones como definitiva hasta confirmar con el cliente la disponibilidad de rutas físicamente diversas y el mecanismo de protección deseado (Pregunta de aclaración #3 y #4).

# Evaluación de la preparación para la cotización o estimación

**Estado:** No listo

**Justificación:**
La información actual no permite avanzar ni siquiera hacia una estimación presupuestaria preliminar confiable, debido a:
- Ausencia de datos sobre disponibilidad y diversidad física de fibra (elemento crítico dado el requisito de sobrevivencia a corte de fibra única).
- Mecanismo de protección no definido.
- Interfaces ópticas de los routers Cisco no identificadas (necesarias para dimensionar transpondedores/muxponders y form factors).
- No se conoce el alcance exacto solicitado (solo equipo de transporte vs. equipo + servicio de fibra).
- No hay confirmación de infraestructura existente en los sitios (espacio, energía) que pueda condicionar la arquitectura.

Sin estos datos, cualquier BoM o estimación de precio sería especulativo y podría generar expectativas incorrectas en el cliente, especialmente dado el plazo ajustado de 3 semanas.

# Borrador de la nota de ingeniería

**Resumen de la oportunidad**
ACME Corp solicita una solución de transporte óptico para interconectar dos centros de datos separados por ~120 km, con una capacidad inicial de 400G y crecimiento planificado a 800G en 2 años. El cliente requiere sobrevivencia ante corte de una sola fibra (mecanismo y SLA no especificados). Existen routers Cisco en ambos extremos con interfaces ópticas aún no identificadas. El cliente solicita una propuesta en 3 semanas.

**Requisitos del cliente**
- Conectividad DC-a-DC, ~120 km.
- Capacidad: 400G inicial → 800G en 2 años.
- Resiliencia ante corte de fibra única (detalle pendiente).
- Compatibilidad con routers Cisco existentes.
- Plazo de propuesta: 3 semanas.

**Supuestos de diseño**
Ninguno aplicado aún; el diseño técnico detallado está pendiente de la resolución de las brechas de información identificadas en la Fase 2.

**Solución(es) propuesta(s)**
Se presentan dos alternativas conceptuales (protección de ruta óptica vs. protección en capa de cliente), ninguna seleccionada como definitiva, condicionadas a la confirmación de diversidad física de fibra y mecanismo de protección esperado por el cliente (ver Fase 3 para detalle completo).

**Cuestiones pendientes**
- Confirmación de disponibilidad/diversidad de fibra.
- Definición de mecanismo de protección y SLA.
- Identificación de interfaces ópticas en routers Cisco.
- Confirmación de infraestructura de sitio (espacio, energía).
- Confirmación del alcance exacto del entregable (equipo vs. equipo + fibra/lambda).
- Confirmación de tipo de entregable (cotización formal vs. ROM).

**Riesgos**
- Riesgo técnico: seleccionar una arquitectura de protección antes de confirmar diversidad física de fibra podría no cumplir el requisito real del cliente.
- Riesgo técnico: interfaces del router Cisco desconocidas podrían requerir transpondedores adicionales no contemplados en un ROM temprano.
- Riesgo operativo: plazo de 3 semanas es ajustado dado el volumen de información pendiente; existe riesgo de no poder emitir una cotización formal completa en ese plazo si las brechas no se cierran rápidamente.
- Riesgo operativo: sin SLA definido, no es posible comprometer un tiempo de restauración específico en la propuesta.

**Próximos pasos**
1. Enviar al cliente las preguntas de aclaración (Fase 2) a la brevedad, dado el plazo de 3 semanas.
2. Solicitar diagramas de red existentes y detalles de los routers Cisco (modelo, interfaces).
3. Solicitar información sobre rutas de fibra disponibles (propia o de carrier) y su diversidad física.
4. Una vez recibidas las respuestas, reevaluar las Fases 3 y 4 con la información completa.

*Nota de gobierno: este borrador requiere revisión y aprobación explícita del Sales Engineer antes de ser utilizado en cualquier paso posterior (Fase 3, 4 y 5 son L3).*

# Reunión de seguimiento con el cliente

**Objetivo**
Cerrar las brechas de información críticas identificadas para poder avanzar hacia una propuesta técnica y comercial viable dentro del plazo de 3 semanas solicitado por ACME.

**Orden del día**
1. Revisión conjunta del alcance solicitado (equipo de transporte vs. equipo + servicio de fibra).
2. Discusión sobre disponibilidad y diversidad física de fibra entre los dos centros de datos.
3. Aclaración del mecanismo de protección esperado y SLA de restauración.
4. Levantamiento de detalles técnicos de los routers Cisco existentes (interfaces, protocolos).
5. Revisión de infraestructura de sitio (espacio, energía, disponibilidad en ambos DCs).
6. Confirmación de requisitos de la aplicación (latencia, modo de replicación, ventanas de mantenimiento).
7. Alineación sobre tipo de entregable esperado (cotización formal vs. estimación preliminar) y cronograma realista dado el plazo de 3 semanas.

**Temas clave de discusión**
- La sobrevivencia a corte de fibra única depende críticamente de contar con rutas físicamente diversas; sin esa confirmación, no se puede garantizar el requisito declarado.
- El crecimiento de 400G a 800G en 2 años debe considerarse en el dimensionamiento inicial de la plataforma fotónica para evitar reemplazos prematuros.
- El plazo de 3 semanas es ajustado; se debe alinear expectativas sobre si es viable una cotización formal completa o si se entregará primero una estimación preliminar.

**Decisiones requeridas del cliente**
- Confirmar si dispone de fibra propia/contratada o si se requiere que el proveedor la suministre.
- Definir el mecanismo de protección deseado y el SLA asociado.
- Confirmar el alcance exacto del entregable solicitado.
- Confirmar si el plazo de 3 semanas es para una cotización formal o una estimación preliminar.

**Información que aún se requiere**
Ver sección "Información faltante" (Fase 2) — se recomienda solicitarla formalmente antes o durante esta reunión.

**Resultados esperados**
- Obtener las respuestas a las preguntas de aclaración críticas (diversidad de fibra, mecanismo de protección, interfaces Cisco).
- Confirmar el alcance y tipo de entregable esperado.
- Establecer un cronograma realista para la entrega de la propuesta, ajustado a la disponibilidad de información.

# Próximas acciones recomendadas

1. El SE debe revisar y aprobar este análisis antes de compartir cualquier contenido con el cliente (gobierno L2/L3 según fase).
2. Enviar a ACME las preguntas de aclaración de la Fase 2 lo antes posible, dado el plazo ajustado de 3 semanas.
3. Agendar la reunión de seguimiento propuesta en la Fase 6.
4. Una vez recibida la información faltante, reevaluar las Fases 3 y 4 con datos completos antes de avanzar hacia una cotización o nota de ingeniería final.