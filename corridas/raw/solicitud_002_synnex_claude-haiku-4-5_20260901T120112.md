<!--
Caso: solicitud_002_synnex.md
Modelo: claude-haiku-4-5
Fecha: 2026-09-01T12:01:12
Tokens de entrada: 3472
Tokens de salida: 8499
Costo estimado de esta corrida (USD): 0.0460
-->

# Resumen de la oportunidad

**Tipo de entregable solicitado por el cliente:** Estimación presupuestaria preliminar  
**Urgencia declarada por el cliente:** Una semana (entrega esperada: ~18 de agosto de 2026)

---

# Inconsistencias detectadas

No se detectaron inconsistencias internas en la información proporcionada. Sin embargo, se observa que varios parámetros técnicos críticos no fueron especificados durante la reunión.

---

# Requisitos del cliente

## Objetivos comerciales
- Interconectar dos oficinas principales de SYNNEX Corp para replicación de bases de datos
- Establecer redundancia mediante dos rutas independientes de fibra óptica

## Requisitos técnicos
- **Distancia:** ~58 km
- **Infraestructura:** Fibra oscura (el cliente proporciona o gestiona la fibra)
- **Endpoints:** Routers Cisco existentes en ambos extremos
- **Resiliencia:** Operación continua con una sola ruta en caso de corte de fibra en la otra

## Requisitos de capacidad
- **Velocidad de interfaz:** No especificada (incertidumbre entre 1G, 10G o 100G)
- **Aplicación:** Replicación de bases de datos

## Requisitos de servicio
- **Protección contra fallas:** Especificada de forma general ("debe seguir funcionando con una sola ruta")
- **SLA:** No especificado

## Requisitos de plazo
- Estimación presupuestaria inicial dentro de una semana

---

# Clasificación de la información

**Hechos:**
- Dos oficinas principales (ubicación general, no coordenadas exactas)
- Distancia aproximada de 58 km
- Fibra oscura disponible entre los sitios
- Routers Cisco en ambos extremos
- Replicación de bases de datos como aplicación
- Dos rutas independientes de fibra requeridas
- Plazo para propuesta: ~7 días

**Supuestos:**
- La "fibra oscura" implica que el cliente dispone de acceso a infraestructura de fibra sin servicios gestionados previos
- Ambos sitios tienen espacio y suministro de energía para equipo óptico de transporte
- Las dos rutas de fibra son geográficamente diversas (no comparten ductos/derechos de paso)
- Los routers Cisco disponen de interfaces ópticas compatibles (o se requiere transpondedor)
- La replicación de bases de datos es síncroma o asíncrona, pero esto afecta la latencia requerida

**Recomendaciones:**
- Priorizar la confirmación de la velocidad de interfaz requerida antes de diseñar la solución
- Clarificar el SLA y la tolerancia a latencia para la replicación de datos
- Validar la disponibilidad y las características de ambas rutas de fibra

---

# Información faltante

| Aspecto | Impacto en la solución |
|--------|------------------------|
| **Velocidad de la interfaz óptica** (1G, 10G, 100G, etc.) | Crítico. Determina la plataforma de transporte, el tipo de transpondedor y el costo total |
| **Características de la fibra oscura** (tipo de fibra, distancia exacta por tramo, atenuación, dispersión, número de hilos disponibles) | Crítico. Necesario para el diseño de la línea fotónica y amplificación |
| **Requisitos de latencia** | Importante. Define si se requiere amplificación de línea o arquitectura simplificada |
| **SLA de disponibilidad / Objetivo de tiempo de recuperación (RTO)** | Importante. Influye en el tipo de protección (1+1, mesh, etc.) |
| **Ubicaciones exactas de los sitios** (ciudad, dirección, coordenadas) | Importante. Confirmar la ruta de fibra y validar derechos de paso |
| **Interfaces existentes en los routers Cisco** (modelo, tipo de interfaz, capacidad) | Importante. Determina si se necesita transpondedor o si hay interfaz óptica nativa |
| **Esquema de protección preferido** (1+1, SNCP a nivel ODU, mesh, etc.) | Importante. Afecta arquitectura y costo |
| **Existencia de equipo óptico previo o preferencias de proveedor** | Moderado. Influye en decisiones de arquitectura |
| **Presupuesto orientativo o restricciones de costo** | Moderado. Ayuda a priorizar soluciones |
| **Cronograma de implementación después de la propuesta** | Moderado. Afecta timeline de ingeniería y fabricación |

---

# Preguntas de aclaración

**Clarificación de requisitos técnicos:**

1. ¿Cuál es la velocidad exacta de interfaz óptica requerida entre los routers Cisco? (1G, 10G, 40G, 100G, u otra)

2. ¿Los routers Cisco en ambos sitios disponen de interfaces ópticas nativas, o se requiere un transpondedor externo para convertir la interfaz de datos?

3. ¿Cuáles son los requisitos de latencia máxima aceptable para la replicación de bases de datos? ¿Es síncrona o asíncrona?

**Clarificación de la infraestructura de fibra:**

4. ¿Quién proporciona la fibra oscura? ¿SYNNEX ya dispone de acceso a dos rutas de fibra física completamente independientes, o necesitan que se identifiquen/procuren?

5. ¿Cuáles son las características técnicas de la fibra disponible? (tipo: SMF-28, NZDF, etc.; longitud exacta; atenuación aproximada; información de dispersión)

6. ¿Existen amplificadores o regeneradores intermedios en la ruta, o se requiere un span continuo de 58 km?

**Clarificación de requisitos de resiliencia:**

7. Además de "seguir funcionando con una sola ruta en caso de corte", ¿existe un SLA específico de disponibilidad? (ej: 99.99%)

8. ¿Cuál es el Objetivo de Tiempo de Recuperación (RTO) esperado cuando ocurra una falla en una ruta?

9. ¿Se requiere conmutación automática de tráfico entre rutas, o es manual?

**Clarificación de ubicaciones y derechos de paso:**

10. ¿Cuáles son las ubicaciones exactas (ciudades, direcciones) de las dos oficinas principales?

11. ¿Ya existe confirmación de disponibilidad de dos rutas de fibra geográficamente independientes entre estos sitios, o requiere validación?

---

# Alternativas de solución

**Premisa de análisis:**  
Dado que la velocidad de interfaz no está confirmada, se presentan dos escenarios de solución principales (10G y 100G como los más probables en un contexto de replicación de datos corporativa). Ambas contemplan protección mediante dos rutas de fibra independientes.

---

## Opción 1: Arquitectura DWDM con protección 1+1 de ruta (Supuesto: interfaces 10G)

**Descripción:**

- Dos transpondedores 10G (uno en cada sitio) multiplexados en una única longitud de onda o en dos longitudes de onda (una por ruta).
- Ruta A: Transpondedor TX → Amplificador de línea (si es necesario por distancia/atenuación) → Ruta 1 de fibra → Amplificador de línea (si es necesario) → Transpondedor RX.
- Ruta B: Transpondedor TX → Amplificador de línea → Ruta 2 de fibra → Amplificador de línea → Transpondedor RX.
- Ambas rutas activas en paralelo con conmutación automática a nivel de transpondedor o router en caso de falla.
- Uso de DWDM: Multiplexación de la misma longitud de onda en ambas rutas, o asignación de longitudes de onda diferentes por ruta.

**Ventajas:**

- Redundancia geográfica completa (dos rutas físicamente independientes).
- Operación de ambas rutas en paralelo optimiza el uso del ancho de banda.
- Si la atenuación permite, puede evitarse amplificación de línea (operación en modo "transponder-only").
- Arquitectura escalable si se requieren capacidades adicionales en el futuro.
- Conmutación rápida en caso de falla de una ruta.

**Limitaciones:**

- A 58 km, dependiendo de la atenuación de la fibra, puede requerirse amplificación de línea (incrementa costo y complejidad).
- Requiere coordinación con el cliente para la gestión de dos rutas de fibra físicamente independientes.
- Si ambas rutas corren en el mismo municipio o derecho de paso, no hay protección contra fallas comunes (ej: corte de zanja).

**Riesgos técnicos:**

- **Riesgo de latencia:** Si se requiere amplificación de línea, el retardo puede incrementarse ligeramente pero sin ser crítico a 58 km.
- **Riesgo de falla de amplificadores:** Si se instalan amplificadores, es un punto de falla potencial; requiere redundancia de fuente de alimentación.
- **Riesgo de pérdida de sincronía:** La conmutación entre rutas puede afectar brevemente la sincronización de datos; necesita ser validada contra los requisitos de la aplicación.

**Riesgos operativos:**

- Aumento de la complejidad operativa (dos sistemas de amplificación, si aplica).
- Requiere capacitación del equipo de operaciones de SYNNEX.
- Necesidad de monitoreo y mantenimiento predictivo de ambas rutas.

---

## Opción 2: Arquitectura DWDM con protección 1+1 de ruta (Supuesto: interfaces 100G)

**Descripción:**

- Dos transpondedores 100G (uno en cada sitio).
- Arquitectura similar a Opción 1, pero con mayor capacidad.
- Ruta A y Ruta B con amplificación de línea (probable en 100G a 58 km, dependiendo de la calidad de la fibra).
- Ambas rutas activas con conmutación automática en caso de falla.

**Ventajas:**

- Proporciona capacidad significativamente mayor, permitiendo escalabilidad futura.
- Arquitectura moderna y estándar en redes corporativas de alto rendimiento.
- Protección geográfica completa.
- Potencial para servir múltiples aplicaciones en el futuro usando la misma infraestructura.

**Limitaciones:**

- A 100G, la amplificación de línea es casi con certeza necesaria (incrementa costo notable y complejidad).
- Mayor consumo de energía en ambos sitios.
- Requiere interfaces ópticas 100G en los routers Cisco (validar compatibilidad).
- Presupuesto capital significativamente mayor que Opción 1.

**Riesgos técnicos:**

- **Riesgo de amplificación de línea:** Requiere diseño de línea fotónica más sofisticado (gestión de ruido, dispersión, potencia óptica).
- **Riesgo de latencia:** Mayor cantidad de amplificadores puede introducir retardo; es crítico validar contra requisitos de replicación de datos.
- **Riesgo de interoperabilidad:** Confirmar compatibilidad entre transpondedores 100G y routers Cisco.

**Riesgos operativos:**

- Entrenamiento especializado requerido para operaciones y mantenimiento.
- Mayor demanda de repuestos y soporte técnico.

---

## Opción 3: Arquitectura simplificada sin DWDM (Supuesto: interfaces 10G, fibra de excelente calidad, distancia validada)

**Descripción:**

- Dos módulos SFP+ 10G de largo alcance (ER o ZR) instalados directamente en los routers Cisco.
- Cada módulo conectado a una ruta de fibra oscura independiente.
- Sin equipo DWDM intermedio.
- Conmutación manual o automática del router entre rutas en caso de falta.

**Ventajas:**

- Solución más simple y de menor costo.
- Menos componentes, menos puntos de falla.
- Menor consumo de energía.
- Implementación rápida si la infraestructura de fibra es de buena calidad.

**Limitaciones:**

- Requiere que ambas rutas de fibra sean de muy alta calidad (baja atenuación, bajo PMD).
- Rango máximo típico de módulos SFP+ ER/ZR es ~40 km en condiciones ideales; 58 km está en el límite o lo excede (puede no ser viable sin amplificación).
- No permite escalabilidad futura hacia mayor capacidad en la misma fibra.
- Si uno de los módulos SFP+ falla, el cambio requiere intervención manual o lógica de failover limitada en el router.

**Riesgos técnicos:**

- **Riesgo crítico de viabilidad:** 58 km muy probablemente excede la capacidad de módulos SFP+ ER/ZR estándar; requiere validación inmediata de características de fibra.
- **Riesgo de pérdida de señal:** Si la atenuación es alta, el BER (tasa de error de bits) puede ser inaceptable.

**Riesgos operativos:**

- Menor visibilidad operativa (sin monitoreo DWDM de línea fotónica).
- Diagnostico de fallas más limitado.

---

## Interconexión con red existente de SYNNEX (si aplica)

**Nota:** El cliente no menciona explícitamente otras redes o infraestructuras existentes que necesiten interconectarse. Los routers Cisco en ambos sitios se asumen como los puntos finales de la nueva solución. Si el cliente requiere en el futuro interconectar esta nueva fibra con otras redes (ej: cloud, data center remoto, filiales adicionales), se evaluarían alternativas como:

- **Extensión a futuro via MPLS o redes mesh:** Usar esta infraestructura de fibra como núcleo redundante y escalar hacia una red más grande.
- **Integración con redes existentes de terceros:** Si SYNNEX usa operadores o ISPs para otros servicios, evaluar peering points.

Por ahora, sin claridad del cliente sobre esto, no se detalla esta sección.

---

# Evaluación de la preparación para la cotización o estimación

**Estado:** **Parcialmente listo**

**Justificación:**

La solicitud puede avanzar a una **estimación presupuestaria preliminar** (ROM - Rough Order of Magnitude) dado que:

✅ **Se conoce:**
- Distancia aproximada (~58 km)
- Número de rutas (2 independientes)
- Tipo general de aplicación (replicación de datos)
- Endpoints (routers Cisco existentes)

⚠️ **Falta información crítica para cotización completa:**
- Velocidad de interfaz exacta → Determina plataforma y transpondedores
- Características de la fibra → Determina si se requiere amplificación y tipo de amplificadores
- SLA / RTO → Influye en arquitectura de protección y costo
- Ubicaciones exactas → Afecta validación de ruta y derechos de paso
- Modelo exacto de routers Cisco → Confirma compatibilidad de interfaces

**Recomendación para la propuesta:**

1. **Fase presente (ROM preliminar):** Elaborar estimación con supuestos claramente documentados (ej: "Asumiendo interfaces 10G, fibra SMF-28 estándar, sin amplificadores intermedios si la calidad de fibra lo permite").

2. **Fase siguiente (cotización formal):** Requiere confirmación de los puntos pendientes listados arriba antes de emitir precios vinculantes.

La urgencia de una semana **es alcanzable para una estimación preliminar**, pero **no para una cotización formal completa** sin clarificar primero la velocidad de interfaz y características de la fibra.

---

# Borrador de la nota de ingeniería

**NOTA DE INGENIERÍA - BORRADOR**

---

**Proyecto:** Interconexión de oficinas principales SYNNEX Corp vía fibra óptica  
**Fecha de reunión:** 11 de agosto de 2026  
**Solicitante:** SYNNEX Corp  
**Preparado por:** [Nombre del Sales Engineer]  
**Fecha del borrador:** [Fecha actual]  
**Estado:** Análisis de requisitos completado; diseño técnico pendiente de información adicional

---

### Resumen de la oportunidad

SYNNEX Corp solicita una solución de transporte de datos a través de fibra óptica para interconectar dos oficinas principales con el fin de replicar bases de datos en tiempo real o diferido. La distancia estimada es de ~58 km utilizando fibra oscura disponible. El cliente requiere redundancia con dos rutas independientes de fibra y operación continua en caso de falla de una ruta. El cliente desea recibir una estimación presupuestaria preliminar en una semana.

---

### Requisitos del cliente

| Aspecto | Detalle |
|--------|---------|
| **Capacidad requerida** | No especificada (1G, 10G, 100G incertidumbre) |
| **Distancia** | ~58 km |
| **Rutas** | 2 rutas independientes de fibra oscura |
| **Endpoints** | Routers Cisco existentes en ambos sitios |
| **Aplicación** | Replicación de bases de datos |
| **Resiliencia** | Operación continua con una sola ruta en caso de corte |
| **SLA** | No especificado |
| **Latencia máxima** | No especificada |
| **Plazo de propuesta** | 1 semana (~18 de agosto de 2026) |

---

### Supuestos de diseño

1. **Velocidad de interfaz:** Se analiza con supuestos de 10G y 100G como escenarios principales (no confirmados por el cliente).

2. **Fibra oscura:** SYNNEX dispone de acceso a dos rutas de fibra completamente independientes (geográficamente diversas).

3. **Características de fibra:** Se asume fibra SMF-28 estándar sin información de atenuación, dispersión o historia de fallas; requiere validación.

4. **Interfaces del router:** Se asume que los routers Cisco tienen capacidad para alojar transpondedores ópticos o módulos SFP+; requiere validación del modelo exacto.

5. **Replicación de datos:** Se asume tolerancia a latencia típica de redes LAN extendida (< 10 ms idealmente, pero no confirmado). No se especifica si es síncrona o asíncrona.

6. **Protección:** Se diseña con arquitectura 1+1 de ruta (ambas activas con conmutación automática en falla). El mecanismo exacto de conmutación (router, transpondedor, o controlador externo) es pendiente.

7. **SLA:** En ausencia de SLA específico, se asume disponibilidad corporativa estándar (99.9% aproximadamente), pero requiere confirmación.

---

### Soluciones propuestas

#### Solución A: DWDM con protección 1+1 (Supuesto: 10G)

**Descripción:**
- Dos transpondedores 10G (uno en cada sitio).
- Ruta A y Ruta B de fibra activas en paralelo.
- Si la atenuación lo permite, operación sin amplificadores intermedios.
- Si es necesaria amplificación, se instalan amplificadores EDFA.
- Conmutación automática a nivel de transpondedor o router en caso de falla.

**Componentes estimados:**
- 2x Transpondedor 10G DWDM (para ambos sitios)
- Opcional: 2x Amplificador EDFA + accesorios de línea (si es necesario)
- Cableado óptico y conectores (monomodo FC, LC o SC)
- Monitoreo y gestión de línea (OTN/OSC)

**Ventajas:**
- Redundancia geográfica clara.
- Escalabilidad futura (agregar canales DWDM).
- Conmutación rápida automática.

**Limitaciones:**
- Costo mayor que soluciones simplificadas.
- Requiere amplificación si la atenuación es alta.

---

#### Solución B: DWDM con protección 1+1 (Supuesto: 100G)

**Descripción:**
- Dos transpondedores 100G.
- Arquitectura similar a Solución A, pero con capacidad 10x mayor.
- Amplificación de línea casi con certeza necesaria.

**Componentes estimados:**
- 2x Transpondedor 100G DWDM
- 2x Amplificador EDFA + accesorios
- Cableado óptico de alta velocidad
- Gestión y monitoreo OTN/OSC

**Ventajas:**
- Capacidad futuro-proof.
- Potencial para agregar servicios adicionales.

**Limitaciones:**
- Presupuesto capital significativamente mayor.
- Mayor complejidad operativa.
- Requiere validación de compatibilidad con routers Cisco.

---

#### Solución C: Módulos SFP+ directos (Supuesto: 10G, fibra de calidad excepcional)

**Descripción:**
- Dos módulos SFP+ 10G ER/ZR instalados directamente en interfaces de los routers.
- Sin equipo DWDM intermedio.
- Conmutación de router entre interfaces en caso de falla.

**Componentes estimados:**
- 2x Módulo SFP+ 10G ER/ZR
- 2x Cableado monomodo (extremo a extremo)

**Ventajas:**
- Costo muy bajo.
- Implementación rápida.
- Menos complejidad operativa.

**Limitaciones:**
- **Viabilidad cuestionable:** Alcance típico de SFP+ ER/ZR es ~40 km; 58 km probablemente excede especificación.
- Requiere fibra de excepcional calidad (baja atenuación, bajo PMD).
- Sin escalabilidad futura en la misma fibra.

---

### Cuestiones pendientes (Critical)

1. **Velocidad de interfaz exacta:** ¿1G, 10G, 40G, 100G?
2. **Modelo exacto de routers Cisco y disponibilidad de interfaces ópticas.**
3. **Características de fibra oscura:** Tipo (SMF-28, NZDF), atenuación, PMD, historial de fallas.
4. **Distancia exacta de cada ruta de fibra** y confirmación de rutas geográficamente independientes.
5. **SLA de disponibilidad** y RTO esperado.
6. **Requisitos de latencia máxima** para la replicación de datos.
7. **Mecanismo de protección preferido:** ¿Conmutación automática, manual, redundancia de línea, otro?
8. **Ubicaciones exactas de los dos sitios** (para validación de derechos de paso y ruta de fibra).

---

### Riesgos

| Riesgo | Severidad | Mitigación |
|--------|-----------|-----------|
| Solución C (SFP+ directos) no viable por distancia | Alto | Validar inmediatamente características de fibra. Preparar alternativa DWDM como backup. |
| Amplificadores intermedios no disponibles en la ruta actual | Medio | Coordinar con proveedor de fibra oscura. Considerar regeneradores o transpondedores no-lineal. |
| Incompatibilidad de interfaces con routers Cisco | Medio | Solicitar modelo exacto y especificaciones. Validar compatibilidad de transpondedores. |
| Latencia inaceptable para replicación de datos | Medio | Definir requisitos de latencia con el cliente. Diseñar con mínima amplificación si es posible. |
| Falta de SLA claro genera expectativas incorrectas | Medio | Establecer SLA explícito en la propuesta. Documentar supuestos de disponibilidad. |
| Falla de fibra común a ambas rutas (ej: corte de zanja) | Bajo (si rutas son geográficamente diversas) | Confirmar diversidad geográfica real de ambas rutas. |

---

### Próximos pasos recomendados

1. **Inmediato (días 1–2):**
   - Enviar cuestionario de aclaración al cliente con las 8 cuestiones pendientes listadas arriba.
   - Solicitar modelos exactos de routers Cisco.
   - Solicitar documentación técnica de fibra oscura (atenuación, PMD, disponibilidad de amplificadores).

2. **Semana 1 (días 3–5):**
   - Recibir y procesar respuestas del cliente.
   - Elaborar ROM (estimación presupuestaria preliminar) con supuestos documentados.
   - Preparar documento de supuestos de diseño para revisión interna.

3. **Semana 1 (días 5–7):**
   - Entregar ROM preliminar al cliente.
   - Programar seguimiento para aclarar puntos restantes.

4. **Post-propuesta:**
   - Una vez confirmados detalles, elaborar cotización formal con BoM detallado.
   - Redactar nota de ingeniería completa.
   - Preparar presentación técnica para decisión de cliente.

---

**Nota:** Este borrador requiere revisión y aprobación del Sales Engineer antes de ser compartido con el cliente.

---

# Reunión de seguimiento con el cliente

**Objetivo de la reunión:**

Validar y clarificar los requisitos técnicos pendientes (especialmente velocidad de interfaz, características de fibra, SLA y latencia) para permitir el diseño de soluciones viables y la elaboración de una cotización formal. Presentar escenarios de solución preliminares con supuestos documentados.

---

**Orden del día recomendado:**

1. **Apertura y recap** (5 min)
   - Resumen de puntos acordados en la reunión del 11 de agosto.
   - Confirmación del plazo de propuesta (1 semana).

2. **Clarificación de requisitos técnicos** (20 min)
   - Velocidad de interfaz requerida (1G, 10G, 100G, otra).
   - Modelo exacto y especificaciones de routers Cisco.
   - Requisitos de latencia máxima para replicación de datos.
   - SLA de disponibilidad y Objetivo de Tiempo de Recuperación (RTO).

3. **Validación de infraestructura de fibra** (15 min)
   - Confirmación de disponibilidad de dos rutas de fibra independientes.
   - Ubicaciones exactas de ambos sitios (para validar ruta).
   - Características técnicas de la fibra (tipo, atenuación, PMD, historia de fallas).
   - Existencia de amplificadores o regeneradores intermedios en la ruta actual.

4. **Presentación de escenarios de solución** (15 min)
   - Opción A: DWDM 10G con protección 1+1.
   - Opción B: DWDM 100G con protección 1+1.
   - Opción C: SFP+ directo (con salvedad de viabilidad a 58 km).
   - Ventajas, limitaciones y riesgos de cada opción.

5. **Discusión de arquitectura de protección** (10 min)
   - Confirmación de conmutación automática vs. manual entre rutas.
   - Tolerancia a desconexión breve durante failover.
   - Simetría de capacidad en ambas rutas (¿ambas activas o una como standby?).

6. **Timeline y próximos pasos** (5 min)
   - Confirmación de fecha de entrega de ROM (semana 1).
   - Cronograma posterior para cotización formal.
   - Identificación de contactos técnicos clave en ambos lados.

---

**Temas clave de discusión:**

- **Velocidad de interfaz:** Impacto directo en tipo de plataforma, costo y complejidad. Prioridad máxima.
- **Características de fibra:** Define viabilidad de soluciones simples vs. complejas (amplificadores sí/no).
- **Latencia:** Crítica para aplicaciones de replicación sincrónica de bases de datos.
- **SLA y RTO:** Establece expectativas de disponibilidad y define arquitectura de redundancia.
- **Diversidad geográfica real de rutas:** Confirma que la protección 1+1 es válida (no falla común potencial).

---

**Decisiones requeridas del cliente:**

1. ¿Cuál es la velocidad de interfaz requerida? (Decisión: 1G / 10G / 40G / 100G / otra)
2. ¿Cuál es el SLA de disponibilidad esperado? (Decisión: 99.9%, 99.99%, otro)
3. ¿Se requiere conmutación automática o manual entre rutas en caso de falla? (Decisión: Automática / Manual)
4. ¿Ambas rutas operarán simultáneamente (1+1 activo-activo) o una como standby? (Decisión: Activo-Activo / Activo-Standby)
5. ¿Cuál es la latencia máxima tolerable? (Decisión: <5 ms / <10 ms / otro)
6. ¿Pueden proporcionar acceso a documentación técnica de la fibra oscura y modelos exactos de routers Cisco? (Decisión: Sí / Necesita seguimiento interno)

---

**Resultados esperados:**

- Confirmación de velocidad de interfaz.
- Documentación técnica de fibra (atenuación, PMD, disponibilidad).
- Modelos de routers Cisco y especificaciones de interfaces.
- SLA y requisitos de latencia documentados.
- Ubicaciones exactas de ambos sitios.
- Criterios de selección de solución (costo, escalabilidad, complejidad operativa, otro).
- Confirmación de cronograma (ROM en semana 1, decisión de propuesta en semana 2-3).

---

# Próximas acciones recomendadas

1. **Preparar cuestionario de aclaración detallado** (L2: SE revisa)
   - Enviar al cliente dentro de 24 horas de esta reunión.
   - Priorizar velocidad de interfaz y características de fibra.

2. **Coordinar con equipo técnico interno** (L2: SE revisa)
   - Validar capacidades de plataformas disponibles para 10G vs 100G.
   - Solicitar datos de costo preliminar (transpondedores, amplificadores, cableado).
   - Identificar potenciales limitaciones de interoperabilidad con routers Cisco.

3. **Preparar ROM con supuestos documentados** (L3: SE aprueba antes de entregar)
   - Elaborar dos escenarios de presupuesto (10G y 100G con supuestos claros).
   - Marcar ítems con precios "Pendiente de cotización" si no hay datos reales.
   - Incluir warnings claros sobre viabilidad de Solución C a 58 km.

4. **Programar seguimiento con cliente** (L2: SE revisa)
   - Agendar llamada o reunión para semana 1 (días 3–4) para revisar respuestas.
   - Presentar ROM preliminar en día 5–6 de la semana.

5. **Documentar supuestos y riesgos internamente** (L3: SE aprueba)
   - Mantener registro de todas las decisiones y supuestos de diseño.
   - Marcar puntos de riesgo alto para revisión de arquitecto si es necesario.

---

**Nota final:** Este análisis y propuesta están listos para revisión del Sales Engineer. No envíe nada al cliente sin aprobación L3 del borrador de nota de ingeniería y ROM.