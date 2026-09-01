<!--
Caso: solicitud_003_bmining.md
Modelo: claude-haiku-4-5
Fecha: 2026-09-01T12:09:26
Tokens de entrada: 3564
Tokens de salida: 3757
Costo estimado de esta corrida (USD): 0.0223
-->

# Resumen de la oportunidad

**Tipo de entregable solicitado por el cliente:** Cotización formal con lista de materiales (BoM) presupuestaria y alternativas de solución

**Urgencia declarada por el cliente:** 10 días (plazo muy ajustado)

**Contexto:** BMINING es cliente existente. Esta es una nueva oportunidad para expandir su infraestructura con una red DWDM en anillo en San Juan, Argentina.

---

# Inconsistencias detectadas

1. **Nombre del canal:** La solicitud menciona "IT#1 y OT#1" como los dos canales iniciales, pero luego se refiere a "IT#1 y OT#2" en la especificación de velocidad (400 Gbps). Requiere clarificación sobre si el segundo canal es OT#1 u OT#2.

2. **Plataforma DWDM no estándar:** Se especifica "C-4615" como plataforma DWDM. Este modelo no forma parte del portafolio estándar de la mayoría de fabricantes de equipamiento de transporte óptico. Requiere confirmación sobre el proveedor/modelo correcto.

3. **Equipamiento en cada sitio:** La solicitud indica "2 plataformas C-4615 en cada sitio" para alta disponibilidad. En una arquitectura de anillo DWDM con 3 sitios, se requiere clarificación sobre la topología exacta de redundancia que BMINING espera (por ejemplo, ¿es una configuración activa-activa, activa-en-espera, o ambas plataformas transportan tráfico?).

---

# Fase 1 — Análisis de requisitos

## Objetivos del cliente

- Expandir la infraestructura de transporte óptico de BMINING con una nueva red local en San Juan, Argentina.
- Implementar alta disponibilidad mediante redundancia de equipamiento en cada sitio.
- Proporcionar capacidad de transporte de dos canales ópticos de 400 Gbps cada uno.

## Factores impulsores del negocio

- Presencia de BMINING como cliente existente (oportunidad de expansión).
- Necesidad de servicios de transporte de datos entre tres ubicaciones en San Juan.
- Requisito de confiabilidad operativa mediante redundancia.

## Requisitos técnicos

- **Topología:** Anillo con 3 sitios DWDM.
- **Canales ópticos:** 2 canales (IT#1 y OT#1/OT#2, requiere aclaración).
- **Velocidad de canal:** 400 Gbps por canal (inicial).
- **Equipamiento:** 2 plataformas C-4615 por sitio (modelo requiere confirmación).
- **Redundancia:** Alta disponibilidad en cada sitio.

## Requisitos de capacidad

- **Inicial:** 2 × 400 Gbps = 800 Gbps de capacidad total en la red.
- **Crecimiento futuro:** No especificado.

## Requisitos geográficos

- **Ubicación:** San Juan, Argentina.
- **Cobertura:** 3 sitios dentro de un área geográfica donde la distancia entre sitios es menor a 50 km.
- **Rutas de fibra:** No especificadas.

## Requisitos de servicio

- **Alta disponibilidad:** Redundancia de equipamiento en cada sitio.
- **Mecanismo de protección:** No especificado (por ejemplo, 1+1, mesh, ODU SNCP).

## Requisitos de plazos

- **Plazo de entrega:** 10 días (muy ajustado).

---

# Clasificación de la información

**Hechos:**
- BMINING es cliente existente.
- Proyecto ubicado en San Juan, Argentina.
- Topología planeada: anillo DWDM con 3 sitios.
- Distancia máxima entre sitios: < 50 km.
- Capacidad requerida: 2 canales de 400 Gbps cada uno.
- Alta disponibilidad mediante 2 plataformas por sitio (modelo requiere confirmación).
- Plazo solicitado: 10 días.
- Se requiere una BoM presupuestaria y alternativas de interconexión con redes actuales de BMINING.

**Supuestos:**
- Los sitios utilizarán infraestructura de fibra óptica terrestre (no submarina ni subacuática).
- La fibra ya está disponible o puede ser provista (no se especificó disponibilidad de ruta).
- Los canales IT#1 y OT#1 transportarán aplicaciones diferentes (IT y OT sugieren distintos contextos de negocio).
- Se espera que el anillo sea operativo con mecanismo de protección automático.
- Las plataformas C-4615 son compatibles con interfaces tributarias de 400 Gbps (requiere validación).
- BMINING tiene capacidad de ingeniería interna para integración y operación.

**Recomendaciones:**
- Requerir confirmación del modelo exacto de plataforma DWDM (fabricante, serie, modelo).
- Solicitar especificación del mecanismo de protección deseado.
- Aclarar las interfaces tributarias que consumirán los canales ópticos.
- Confirmar la disponibilidad de rutas de fibra entre los tres sitios.
- Validar la arquitectura de redundancia esperada (configuración activa-activa vs. activa-en-espera).

---

# Fase 2 — Análisis de brechas de descubrimiento

## Información faltante crítica

1. **Identificación de sitios:** Nombres, ubicaciones exactas, coordenadas geográficas de los 3 sitios.

2. **Infraestructura de fibra:**
   - ¿Existe fibra óptica disponible entre los 3 sitios, o debe ser instalada?
   - ¿Qué disponibilidad/número de hilos de fibra hay en cada ruta?
   - ¿Distancias exactas de ruta de fibra entre cada par de sitios?
   - ¿Características de la fibra (tipo, antigüedad, calidad óptica)?

3. **Plataforma DWDM:**
   - ¿Quién es el proveedor y cuál es el modelo exacto de la plataforma DWDM? ("C-4615" requiere validación/confirmación.
   - ¿Cuáles son las capacidades máximas de la plataforma?
   - ¿Qué interfaces tributarias soporta (por ejemplo, 2×400GE, 4×200GE, 8×100GE, otros)?

4. **Canales ópticos:**
   - Confirmación: ¿Son IT#1 y OT#1, u OT#2?
   - ¿Ambos deben ser 400 Gbps, o existe posibilidad de escalado futuro?
   - ¿Qué aplicaciones consumirán estos canales (replicación de datos, almacenamiento, datos en tiempo real)?
   - ¿Requisitos de latencia, jitter o disponibilidad específicos?

5. **Interfaces tributarias:**
   - ¿Qué interfaces tributarias utilizarán los sitios para conectarse a las plataformas DWDM? (por ejemplo, QSFP-DD 400GE, CFP2-DCO, otros.)
   - ¿Qué protocolo de capa de cliente (por ejemplo, Ethernet, OTU4, otro)?
   - ¿Existen restricciones de equipamiento tributario en los sitios?

6. **Arquitectura de redundancia:**
   - ¿Cuál es exactamente la configuración esperada de las 2 plataformas C-4615 por sitio? (¿Activa-activa? ¿Activa-en-espera?)
   - ¿Cómo se sincronizarán ambas plataformas?
   - ¿Qué mecanismo de protección se espera? (por ejemplo, 1+1 con conmutación automática, mesh de protección ODU, otro).

7. **Infraestructura existente de BMINING:**
   - ¿Qué otras redes ópticas o infraestructuras tiene BMINING en Argentina o en otras regiones?
   - ¿Cuáles son los puntos de interconexión deseados para esta nueva red en anillo?
   - ¿Qué topología actual tienen sus redes ópticas?
   - ¿Existen requisitos de interoperabilidad con equipamiento existente?

8. **Restricciones de sitio:**
   - ¿Cuál es la disponibilidad de espacio en rack en cada sitio?
   - ¿Cuál es la disponibilidad de energía (voltaje, amperaje máximo)?
   - ¿Existen restricciones ambientales (temperatura, humedad)?
   - ¿Hay acceso a aire acondicionado/sistemas de enfriamiento?

9. **Servicio y soporte:**
   - ¿Qué nivel de servicio técnico se espera post-implementación?
   - ¿Requiere monitoreo remoto, mantenimiento preventivo u otro servicio?

10. **Plazo de 10 días:**
    - ¿Este plazo incluye solo el suministro de equipamiento, o también la ingeniería, la instalación física y la puesta en servicio?
    - ¿Cuál es el estado de disponibilidad del equipamiento C-4615 en inventario?

---

## Preguntas de aclaración para el cliente

### Cuestiones críticas (bloquean la cotización)

1. **Confirmación del modelo de plataforma:** ¿Pueden proporcionar el modelo exacto, proveedor y datasheet de la plataforma DWDM que planean utilizar? ("C-4615" no coincide con los modelos estándar conocidos.)

2. **Confirmación de canales:** ¿Son exactamente 2 canales denominados IT#1 y OT#1, o es OT#2? ¿Qué significa cada sigla en su contexto operativo?

3. **Arquitectura de redundancia:** ¿Cómo desean configurar las 2 plataformas por sitio? ¿Ambas activas transportando tráfico, o una en espera?

4. **Disponibilidad de fibra:** ¿Existe ruta de fibra óptica disponible entre los 3 sitios? ¿Cuántos hilos de fibra hay disponibles en cada tramo?

5. **Distancias exactas:** ¿Cuáles son las distancias de ruta de fibra entre cada par de sitios (por ejemplo, Sitio A → Sitio B, Sitio B → Sitio C, Sitio C → Sitio A)?

6. **Interfaces tributarias:** ¿Qué equipamiento tributario (routers, switches, servidores) se conectará a cada sitio DWDM? ¿Qué interfaces proporcionan (400GE, 200GE, 100GE, otra)?

### Cuestiones de confirmación (mejoran el diseño)

7. **Mecanismo de protección:** ¿Qué mecanismo de protección esperan? ¿1+1 bidireccional, mesh ODU SNCP, u otro?

8. **Redes existentes de BMINING:** ¿Cuáles son las ubicaciones, topologías y tecnologías de sus redes ópticas actuales?

9. **Punto(s) de interconexión:** ¿Con qué puntos o redes actuales de BMINING debe conectarse esta nueva red en anillo?

10. **Requisitos de aplicación:** ¿Qué aplicaciones clave consumirán IT#1 y OT#1? ¿Requieren síncrono, asíncrono, tolerancia a latencia específica?

11. **Plazo desglosado:** Del plazo de 10 días, ¿cuánto es para ingeniería, cuánto para procura, cuánto para instalación y puesta en servicio?

12. **Disponibilidad de equipamiento:** ¿Está el modelo DWDM especificado en stock, o requiere leadtime de fabricante?

---

# Información disponible para avanzar

Existe suficiente información **de alto nivel** para iniciar un análisis ROM (Rough Order of Magnitude) y para elaborar preguntas de refinamiento. **Sin embargo, no hay suficiente información para preparar una cotización formal precisa o una BoM definitiva.**

Razones:
- El modelo de plataforma DWDM no está claramente especificado.
- Las interfaces tributarias no están definidas.
- La arquitectura de redundancia no está detallada.
- La disponibilidad de fibra no se confirmó.
- Las distancias exactas de ruta no se proporcionaron.
- El estado de las redes existentes de BMINING (para interconexión) no se describió.

---

# Fases completadas

✅ **Fase 1:** Análisis de requisitos (completado)  
✅ **Fase 2:** Análisis de brechas de descubrimiento (completado)

---

# Fases pendientes

⏸️ **Fase 3:** Evaluación de solución (en espera de información de las fases 1–2)  
⏸️ **Fase 4:** Preparación para cotización (en espera de datos técnicos confirmados)  
⏸️ **Fase 5:** Nota de ingeniería (en espera de confirmación de solución)  
⏸️ **Fase 6:** Reunión de seguimiento (en espera de solución validada)

---

# Recomendación inmediata para el Sales Engineer

**Acción prioritaria:** Contáctese con BMINING dentro de las próximas 24 horas para obtener respuestas a las **cuestiones críticas** (preguntas 1–6 de la sección anterior). Sin estas confirmaciones, no es posible avanzar hacia una cotización y el plazo de 10 días estará en riesgo.

**Sugerencia:** Proponga una breve llamada técnica con BMINING para validar el modelo DWDM, la arquitectura de redundancia, la disponibilidad de fibra y las interfaces tributarias. Esto desatascará el proceso.

Una vez que se obtengan estas confirmaciones, el agente está listo para ejecutar las **Fases 3–6 completas** (evaluación de solución, BoM, nota de ingeniería y preparación de la reunión de seguimiento).