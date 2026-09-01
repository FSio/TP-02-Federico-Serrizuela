<!--
Caso: solicitud_001_acme.md
Modelo: claude-haiku-4-5
Fecha: 2026-09-01T11:57:45
Tokens de entrada: 3423
Tokens de salida: 5173
Costo estimado de esta corrida (USD): 0.0293
-->

# Resumen de la oportunidad
**Tipo de entregable solicitado por el cliente:** Propuesta (asumido que incluye cotización)  
**Urgencia declarada por el cliente:** 3 semanas (reunión del 10 de agosto, propuesta esperada aproximadamente el 31 de agosto de 2026)

---

# Inconsistencias detectadas
No se han detectado inconsistencias internas en los datos proporcionados. La información es limitada pero internamente coherente.

---

# Fase 1 — Análisis de requisitos

## Requisitos del cliente

| Aspecto | Detalle |
|--------|---------|
| **Objetivo de negocio** | Interconectar dos centros de datos geográficamente separados |
| **Drivers** | No especificados |
| **Ubicaciones** | Dos centros de datos; distancia aproximada: 120 km (se asume distancia de fibra similar) |
| **Capacidad actual** | 400G |
| **Capacidad futura** | 800G (horizonte: 2 años) |
| **Resiliencia** | Debe sobrevivir a un corte de fibra única (mecanismo de protección no especificado) |
| **Infraestructura existente** | Enrutadores Cisco en ambos extremos |
| **Interfaces ópticas existentes** | Desconocidas |
| **SLA requerido** | No especificado |
| **Plazo de entrega** | 3 semanas |

---

# Fase 2 — Análisis de brechas de descubrimiento

## Información crítica faltante

1. **Disponibilidad de fibra**
   - ¿Dispone el cliente de fibra propia entre los dos centros de datos?
   - ¿Es necesario arrendar fibra de un operador de telecomunicaciones?
   - Si es fibra arrendada, ¿hay acuerdos ya en marcha o es necesario procurar?

2. **Características de la fibra**
   - Tipo de fibra (SMF estándar, LEAF, NZDF, etc.)
   - Número de pares de fibra disponibles
   - Distancia exacta de la ruta (estimación de atenuación y dispersión)
   - Condiciones de la fibra (enlaces anteriormente utilizados, reciente instalación, etc.)

3. **Arquitectura de protección**
   - ¿Qué mecanismo exacto se requiere para la sobrevivencia a corte de fibra? (p. ej., 1+1 con conmutación automática, mesh-based protection, ODU SNCP, arquitectura redundante con doble enlace)
   - ¿Cuál es el RTO (Recovery Time Objective) y RPO (Recovery Point Objective) esperado?
   - ¿Se requiere protección a nivel de línea óptica, de cliente (ODU) o ambas?

4. **Interfaces ópticas existentes**
   - Modelos exactos de enrutadores Cisco
   - Interfaces ópticas disponibles (velocidad, tipo de transceptor: CFP, CFP2, CFP4, micro-optics, etc.)
   - ¿Hay limitaciones de espacio o potencia en los sitios?

5. **Protocolos y encapsulación**
   - Protocolo de enlace de cliente (Ethernet, OTU, OPU, etc.)
   - ¿Se requiere servicios gestionados (OAM, monitoreo)?
   - ¿Hay requisitos específicos de latencia?

6. **Requisitos de crecimiento**
   - ¿Es la transición a 800G una previsión firme o una posibilidad?
   - ¿Se contempla una migración directa de interfaces (reemplazo de transceptores) o se necesita infraestructura paralela durante la transición?

7. **Marcos regulatorios y derechos de paso**
   - Si se requiere fibra arrendada: ¿estado de los derechos de paso y licencias?
   - ¿Hay restricciones de ruta conocidas?

8. **Timeline operativo**
   - ¿La solicitud de 3 semanas incluye solo la propuesta comercial, o también el diseño final y orden de componentes?
   - ¿Cuándo se espera la implementación física?

---

## Preguntas de aclaración recomendadas

### Prioritarias (fundamentales para el diseño)

1. **Sobre la fibra:**
   - "¿Disponen ustedes de fibra propia entre estos dos centros de datos, o necesitamos ayudarles a procurar fibra arrendada a través de un operador regional?"
   - "Si es fibra propia, ¿conocen la distancia exacta de la ruta y el tipo de fibra (SMF estándar, LEAF, u otra)? ¿Cuántos pares están disponibles?"

2. **Sobre la protección:**
   - "Cuando mencionan 'debe sobrevivir a un corte en una sola fibra', ¿se refieren a un esquema de protección 1+1 con dos enlaces físicos separados, o a un mecanismo de protección a nivel de equipo (p. ej., SNCP en la capa ODU)?"
   - "¿Cuál es el tiempo máximo tolerable de recuperación ante una falla (RTO) y la pérdida máxima de datos tolerable (RPO)?"

3. **Sobre interfaces ópticas:**
   - "¿Podrían confirmar los modelos exactos de los enrutadores Cisco y las interfaces ópticas disponibles (número de puertos, velocidades, tipos de transceptores)?"
   - "¿Hay restricciones de espacio en rack o disponibilidad de potencia en los sitios?"

4. **Sobre crecimiento y timeline:**
   - "La expansión a 800G en 2 años, ¿es una necesidad confirmada o una posibilidad que desean tener cubierta en el diseño?"
   - "¿Esperan que la propuesta en 3 semanas incluya solo la cotización, o también el diseño final listo para procuración?"

### Secundarias (útiles para refinamiento)

5. "¿Hay aplicaciones críticas cuya latencia máxima tolerable sea inferior a los ~0,6 ms típicos a 120 km?"
6. "¿Requieren servicios OAM (monitoreo de alarmas, monitoreo de PM) en tiempo real?"
7. "¿Tienen preferencia por enfoques de arquitectura (p. ej., DWDM punto a punto, packet-optical, ROADM) o es neutral?"

---

# Fase 3 — Evaluación de la solución

**Estado: Evaluación preliminar; recomendación de completitud**

Dados los datos incompletos, especialmente sobre mecanismo de protección, características de fibra e interfaces ópticas, no es posible desarrollar soluciones detalladas en esta fase. Sin embargo, se esbozarán dos direcciones arquitectónicas genéricas que cubren los escenarios más probables:

## Opción A: DWDM punto a punto con protección 1+1 (dos enlaces independientes)

**Descripción:**
- Dos enlaces de fibra física independientes, cada uno equipado con un sistema DWDM bidireccional.
- Cada enlace transporta 400G inicialmente (p. ej., 4× 100G wavelengths o 1× 400G wavelength con amplificación).
- En caso de corte en un enlace, el tráfico conmuta automáticamente al segundo enlace.
- Crecimiento a 800G: se agregan wavelengths adicionales a ambos enlaces (escalamiento de espectro) o se reemplaza la plataforma DWDM (escalamiento de plataforma).

**Ventajas:**
- Alta disponibilidad: sobrevivencia garantizada a corte de fibra única.
- Escalabilidad clara: se pueden agregar wavelengths dentro de los límites de la plataforma.
- Operación probada en redes de transporte terrestres.

**Limitaciones:**
- Requiere dos rutas de fibra separadas (más costoso, más complicado de procurar).
- Si ambas rutas comparten conductos o postes, el riesgo de corte simultáneo es alto (requiere validación de ruta de fibra física).
- Mayor CAPEX inicial por duplicación de infraestructura.

**Riesgos técnicos:**
- Si las dos rutas de fibra no están físicamente separadas, la protección 1+1 no proporciona la resiliencia esperada ante cortes.
- La conmutación automática requiere un protocolo de señalización (p. ej., OAM a nivel de línea, o protección a nivel de cliente) que debe estar alineado con la arquitectura del enrutador Cisco.
- Dispersión cromática y PMD acumulativos en 120 km: requieren validación para 400G y especialmente para 800G (posible necesidad de compensación).

**Riesgos operativos:**
- Mayor complejidad de gestión operativa (dos sistemas, dos rutas).
- Necesidad de tests periódicos de conmutación para validar la protección.

---

## Opción B: DWDM punto a punto con protección a nivel de cliente (ODU SNCP o equivalente)

**Descripción:**
- Un único enlace de fibra física (o un único par de fibras) equipado con un sistema DWDM.
- La protección se implementa a nivel de la capa de cliente (p. ej., mediante SNCP en la rama ODU, o replicación de paquetes a nivel de enrutador).
- En caso de corte de la fibra óptica, el tráfico se redirige a través de rutas alternativas de datos (si existen) o se tolera una pérdida temporal mientras se restaura la fibra.

**Ventajas:**
- CAPEX más bajo: una única ruta de fibra.
- Escalabilidad similar a la Opción A (agregar wavelengths o escalar plataforma).
- Puede ser viable si el cliente tiene acceso a rutas alternativas de datos (p. ej., otra fibra, IP-MPLS con reroute rápido).

**Limitaciones:**
- No garantiza RTO cero en caso de corte de fibra: depende de la velocidad de restauración de las rutas alternativas.
- Requiere redundancia lógica en la capa de cliente (enrutador Cisco), que debe estar diseñada específicamente.
- Si no hay rutas alternativas disponibles, la protección no es verdadera.

**Riesgos técnicos:**
- Dependencia crítica de la arquitectura IP/MPLS del cliente; requiere coordinación de diseño entre equipos óptico e IP.
- Si la conmutación no es suficientemente rápida, puede haber pérdida de paquetes que el cliente no tolere.

**Riesgos operativos:**
- Mayor complejidad operativa: requiere coordinación entre equipo óptico y equipo de enrutamiento.
- Necesidad de validación exhaustiva de tiempos de conmutación.

---

## Escalamiento a 800G

En ambas opciones:
- **Escalamiento de espectro:** Se añaden wavelengths adicionales (p. ej., si inicialmente se usan 4 wavelengths de 100G, se escalan a 8 wavelengths). Viabilidad depende del rango de longitudes de onda disponibles en la plataforma y las características de la fibra.
- **Escalamiento de plataforma:** Se reemplaza el sistema DWDM actual por uno de generación más nueva (más denso espectralmente). Esto implica una migración de equipo; requiere una ventana de corte operativo.

Sin datos sobre la plataforma específica propuesta, no es posible determinar cuál enfoque es más viable.

---

## Conclusión provisoria sobre soluciones

**No se recomienda una selección definitiva de arquitectura en esta fase** debido a:
- Desconocimiento del mecanismo exacto de protección esperado.
- Falta de datos sobre disponibilidad de rutas de fibra.
- Incertidumbre sobre interfaces ópticas de los enrutadores Cisco.
- Requerimientos de escalamiento (¿cuántos pares de fibra se pueden provisionar?).

**Siguientes pasos antes de Fase 4 (cotización):**
Responder las preguntas de aclaración prioritarias (especialmente: fibra, mecanismo de protección, interfaces Cisco).

---

# Fase 4 — Preparación para la cotización o estimación

**Estado:** **No listo para cotización formal**

**Justificación:**

Para una cotización de calidad, se requiere:

1. **Confirmación de disponibilidad de fibra** (actualmente desconocida)
   - Sin esto, no se puede estimar costos de procuración de fibra ni tiempos.

2. **Definición del mecanismo de protección** (actualmente ambiguo)
   - La arquitectura de protección define directamente la cantidad de equipo, sistemas DWDM, y rutas requeridas.
   - Las dos opciones precedentes tienen costos muy diferentes.

3. **Confirmación de interfaces ópticas disponibles** (actualmente desconocida)
   - Determina si se requieren transceptores nuevos, sus velocidades, y compatibilidad con plataformas DWDM estándar.

4. **Validación de distancia de fibra** (estimación de 120 km; requiere confirmación)
   - Afecta el diseño de amplificación, compensación de dispersión, y selección de transceptores.

5. **Requerimientos de escalamiento confirmados** (actualmente "posibilidad en 2 años")
   - Define el headroom espectral y la elección de plataforma inicial.

**Estado alternativo:** Se podría elaborar una **estimación presupuestaria preliminar de alto nivel** con supuestos claramente declarados (p. ej., "asumiendo 1+1 con dos rutas de fibra, fibra estándar SMF, 400G inicial escalable a 800G con adicionales wavelengths"). Esto permitiría al cliente validar el orden de magnitud de inversión mientras se responden las preguntas de detalle.

---

# Fase 5 — Preparación de la nota de ingeniería

**No elaborada en esta etapa** por:
- Información insuficiente para una arquitectura de solución confirmada.
- Falta de detalles de diseño (ruta de fibra, plataformas específicas, BoM provisional).

**Será elaborada tras la Fase 4 completa**, una vez que el cliente responda las preguntas de aclaración prioritarias y se haya acordado una dirección de arquitectura.

---

# Fase 6 — Preparación de la reunión de seguimiento con el cliente

**Objetivo de la reunión:**
Validar supuestos de descubrimiento, aclarar requisitos técnicos críticos para el diseño de la solución, y alinearse sobre el alcance y timeline de la propuesta.

**Orden del día recomendado:**

1. **Resumen de entendimiento del Sales Engineer** (5 min)
   - Recap: interconexión de 2 DC a 120 km, 400G expandible a 800G, sobrevivencia a corte de fibra.
   - Confirmación de objetivos de negocio subyacentes.

2. **Discusión técnica: Infraestructura de fibra** (10 min)
   - "¿Tienen fibra propia entre los dos centros de datos?"
   - Si es propia: características (distancia exacta, tipo, pares disponibles).
   - Si es arrendada: ¿qué operador? ¿estado de acuerdos? ¿derechos de paso confirmados?
   - Validación de separación física de rutas (para protección 1+1).

3. **Discusión técnica: Mecanismo de protección** (10 min)
   - Clarificación: "Sobrevivencia a corte de fibra" = ¿dos enlaces físicos independientes? ¿protección en el enrutador?
   - RTO esperado (si no hay ruta alternativa, ¿cuánto tiempo tolera sin conectividad?).
   - RPO: ¿pérdida de datos tolerable durante conmutación?

4. **Discusión técnica: Enrutadores y interfaces ópticas** (10 min)
   - Confirmación de modelos Cisco y puertos ópticos disponibles.
   - Restricciones de espacio/potencia en sitios.
   - Preferencia sobre transceptores (si la tienen).

5. **Discusión: Escalamiento a 800G** (5 min)
   - ¿Timeline confirmado (2 años) o estimado?
   - ¿Debe el diseño inicial permitir expansión sin upgrade de infraestructura de fibra?

6. **Alcance y timeline de la propuesta** (5 min)
   - Confirmación: ¿3 semanas = propuesta comercial únicamente, o incluye diseño final?
   - ¿Quiénes son los stakeholders de aprobación del lado del cliente?

7. **Próximos pasos y cronograma** (5 min)
   - Comunicación de cuándo se completará la propuesta.
   - Identificación de punto de contacto único para preguntas pendientes.

**Temas clave de discusión:**

- Fibra: propia vs. arrendada; separación física de rutas.
- Protección: mecanismo exacto, RTO, RPO.
- Enrutadores: modelos y disponibilidad de interfaces.
- Crecimiento: confirmación de necesidad y timeline.

**Decisiones requeridas del cliente:**

1. Disponibilidad y características de fibra.
2. Mecanismo de protección preferido.
3. Confirmación de modelos de enrutador y puertos ópticos.
4. Timeline firme para escalamiento a 800G.

**Información aún requerida tras esta reunión:**

- Respuestas a todas las preguntas prioritarias de aclaración (véase Fase 2).
- Documentación técnica de enrutadores (si aplica).
- Plano de red del cliente (ubicaciones exactas, ancho de banda actual, tráfico esperado).

**Resultados esperados de la reunión:**

- Consenso sobre arquitectura de solución (Opción A vs. B, o variante).
- Suficiencia de información para avanzar a Fase 4 (cotización) y Fase 5 (nota de ingeniería).
- Acuerdo sobre cronograma de entrega de propuesta y próxima reunión de revisión.

---

# Próximas acciones recomendadas

1. **Preparar y enviar cuestionario de descubrimiento** al cliente consolidando las preguntas de aclaración (priorizar las cuatro prioritarias).

2. **Agendar reunión de aclaración técnica** (idealmente, dentro de 7–10 días) con el cliente incluyendo:
   - Sales Engineer
   - Ingeniero técnico (especialista óptico, si aplica)
   - Posiblemente: representante del cliente de infraestructura de fibra o equipamiento.

3. **Solicitar documentación técnica:**
   - Diagrama de red del cliente.
   - Hojas de datos de enrutadores.
   - Plano de ruta de fibra (si existe).

4. **En paralelo:** Validar con el equipo interno qué plataformas DWDM estándar cubrirían este caso (100G a 400G en 120 km), para tener opciones listas tras el descubrimiento.

5. **Post-reunión:** Consolidar hallazgos en un resumen ejecutivo interno y proceder a Fases 3–5 una vez confirmados los requisitos críticos.

---

**Nota final:** Esta oportunidad tiene plazo apretado (3 semanas) pero información incompleta. Se recomienda **agendar la reunión de aclaración lo antes posible** (preferentemente la próxima semana) para recuperar tiempo e iterar rápidamente sobre el diseño.