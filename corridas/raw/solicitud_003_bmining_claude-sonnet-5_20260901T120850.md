<!--
Caso: solicitud_003_bmining.md
Modelo: claude-sonnet-5
Fecha: 2026-09-01T12:08:50
Tokens de entrada: 4746
Tokens de salida: 11559
Costo estimado de esta corrida (USD): 0.1251
-->

# Resumen de la oportunidad

**Cliente:** BMINING (cliente existente)
**Proyecto:** Nueva red en anillo DWDM de 3 sitios en San Juan, Argentina
**Fecha de solicitud:** 15 de agosto de 2026
**Tipo de entregable solicitado por el cliente:** Estimación presupuestaria preliminar (BoM presupuestario con precios) — el cliente usa el término "BoM presupuestaria", lo cual se interpreta como un ROM (Rough Order of Magnitude), no como cotización formal. **Esto debe confirmarse con el cliente** (ver Preguntas de aclaración).
**Urgencia declarada por el cliente:** Plazo de entrega de 10 días (tal como fue expresado; no se especifica si son 10 días hábiles o corridos, ni si el plazo aplica a la entrega del BoM o a la implementación del proyecto).

---

# Inconsistencias detectadas

1. **Nombres de canales ópticos inconsistentes:** en un punto de la solicitud se mencionan los canales "IT#1 y OT#1", y en otro punto "IT#1 y OT#2". No es posible determinar si se trata de un error de tipeo o de dos canales distintos. **Se trata como información pendiente de confirmar con el cliente** y no se asume cuál es la versión correcta.

---

# Requisitos del cliente

- Topología: anillo DWDM de 3 sitios.
- Sitios: aún no existen (a construir/habilitar), ubicados en San Juan, Argentina.
- Distancia entre sitios: menor a 50 km (declarada, sin confirmar ruta real de fibra).
- Canales ópticos iniciales: 2 (nombres a confirmar por inconsistencia señalada arriba).
- Velocidad de canal: 400 Gbps para ambos canales.
- Alta disponibilidad: 2 plataformas C-4615 por sitio (6 plataformas en total) — plataforma especificada por el cliente, se toma como dato, no como recomendación del asistente.
- Interfaces tributarias: no definidas por el cliente; se solicitan alternativas.
- Entregable: BoM presupuestario con precios.
- Plazo: 10 días.
- Se solicitan alternativas de interconexión de esta nueva red con otras redes actuales de BMINING.

---

# Clasificación de la información

**Hechos (declarados explícitamente por el cliente):**
- Anillo de 3 sitios DWDM en San Juan, Argentina.
- Sitios aún no existen.
- Separación entre sitios <50 km.
- 2 canales ópticos iniciales a 400 Gbps.
- 2x C-4615 por sitio (alta disponibilidad).
- Interfaces tributarias indefinidas.
- Plazo de 10 días.
- Cliente existente, con otras redes propias, solicita alternativas de interconexión.

**Supuestos (necesarios para poder avanzar en el análisis, deben validarse con el cliente):**
- Se asume que "menos de 50 km entre sitios" corresponde a distancia de ruta de fibra, no a distancia geodésica en línea recta.
- Se asume, solo a efectos de estructurar el BoM preliminar, que dado que cada tramo del anillo es <50 km no se requeriría amplificación óptica en línea; esto debe confirmarse con datos reales de atenuación de fibra una vez exista.
- Se asume que "alta disponibilidad" implica algún esquema de protección de equipo y/o de tráfico, pero **no se asume el mecanismo específico** (1+1, ODUk SNCP, protección de anillo óptico, etc.) — se trata como brecha de información en la Fase 2.

**Recomendaciones (del asistente, sujetas a revisión/aprobación del SE):**
- Alternativas de arquitectura de anillo (Fase 3).
- Alternativas de interfaces tributarias (Fase 3).
- Alternativas de interconexión con red(es) existente(s) de BMINING (Fase 3).
- Estructura de BoM preliminar (Fase 4/5), sin precios reales.

---

# Información faltante

- **Sitios:** ubicación exacta/predios de los 3 sitios (aún no existen); disponibilidad de energía, espacio y climatización en cada sitio; fecha estimada de disponibilidad física de los sitios (crítico dado que condiciona cualquier plazo de implementación).
- **Fibra:** disponibilidad de fibra oscura propia o arrendada entre los 3 sitios; distancia real de ruta (no solo distancia declarada <50 km); tipo de fibra, atenuación, número de hilos disponibles, edad/estado de la planta si ya existe en la zona.
- **Infraestructura existente:** si BMINING ya tiene infraestructura de ducto/poste en la zona o si se debe construir desde cero.
- **Esquema de protección:** mecanismo específico de protección de equipo y de tráfico (no asumido).
- **Latencia:** requisitos de latencia extremo a extremo, si existen.
- **Crecimiento:** expectativa de crecimiento en cantidad de canales/velocidad más allá de los 2 canales iniciales a 400G (dimensionamiento de slots, licencias, capacidad de la línea fotónica).
- **Interfaces y protocolos tributarios:** tipo de tráfico a transportar en IT#1 y OT#1/OT#2 (Ethernet, OTN, Fibre Channel, SAN, etc.), tasa, cantidad de puertos por canal.
- **Aplicación consumidora del servicio:** naturaleza del tráfico (por ejemplo, si es replicación de datos, SCADA de minería, backup, monitoreo), tolerancia a latencia, ventanas de mantenimiento/corte permitidas.
- **Redes existentes de BMINING para interconexión:** ubicación, plataforma, capacidad y protocolos de las redes existentes con las que se desea interconectar el nuevo anillo; punto(s) físico(s) de interconexión propuestos.
- **Aclaración de la inconsistencia** IT#1/OT#1 vs IT#1/OT#2.
- **Alcance real del plazo de 10 días:** si aplica a la entrega del BoM/estimación o a la implementación completa del proyecto.

---

# Preguntas de aclaración

1. ¿Los nombres correctos de los canales ópticos son "IT#1 y OT#1" o "IT#1 y OT#2"? Por favor confirmar.
2. ¿El plazo de 10 días se refiere a la entrega del BoM/estimación presupuestaria, o a la implementación completa del proyecto?
3. ¿Existen predios ya identificados para los 3 sitios, o aún deben seleccionarse/adquirirse? ¿Cuál es la fecha estimada de disponibilidad física de cada sitio?
4. ¿BMINING dispone de fibra oscura propia o arrendada entre los futuros sitios, o debe contratarse/tenderse nueva fibra?
5. ¿Cuál es el tipo de tráfico y protocolo que se transportará sobre IT#1 y OT#1/OT#2 (Ethernet, OTN, Fibre Channel, otro)? ¿Cuántos puertos tributarios se requieren por canal?
6. ¿Qué esquema de protección se espera (protección de equipo, de tráfico óptico en anillo, ambas)?
7. ¿Existen requisitos de latencia máxima end-to-end para alguno de los dos canales?
8. ¿Cuál es la expectativa de crecimiento de canales/capacidad en el mediano plazo (para dimensionar slots y licencias)?
9. Respecto a la interconexión con otras redes de BMINING: ¿cuáles son esas redes (ubicación, plataforma, capacidad), y en qué sitio(s) se desea materializar la interconexión?
10. ¿Existe alguna restricción de espacio/energía conocida en los sitios a construir que deba considerarse en el diseño de rack?

---

# Alternativas de solución

*(Nota de gobernanza: esta fase requiere revisión y aprobación explícita del SE antes de utilizarse en cualquier paso posterior, incluyendo la preparación de cotización/BoM y la nota de ingeniería.)*

## Opción 1 — Anillo DWDM con ROADM en cada sitio

**Descripción:** Los 3 sitios se equipan con capacidad de ROADM (Reconfigurable Optical Add/Drop Multiplexer), permitiendo agregar/extraer longitudes de onda de forma flexible en cualquier sitio del anillo, sobre la plataforma C-4615 indicada por el cliente.

**Ventajas:**
- Flexibilidad para redirigir canales ópticos entre sitios sin intervención manual en la capa fotónica.
- Facilita el crecimiento futuro de canales sin rediseño de la capa óptica.
- Compatible con esquemas de protección de anillo óptico (mecanismo específico a definir).

**Limitaciones:**
- Mayor costo de plataforma fotónica comparado con un esquema fijo.
- Requiere confirmar que la plataforma C-4615 soporte configuración ROADM en la variante/tarjetas necesarias para este proyecto (dato a validar, no asumido).

**Riesgos:**
- Técnico: sin confirmación de las capacidades ROADM exactas del C-4615 para este caso de uso, existe riesgo de sobredimensionamiento o subdimensionamiento del BoM.
- Operativo: mayor complejidad de gestión y configuración inicial en sitios que aún no existen físicamente, lo que puede impactar el cronograma de instalación.

## Opción 2 — Anillo con OADM fijo / configuración punto a punto en cascada

**Descripción:** Los 3 sitios se interconectan mediante multiplexores ópticos de add/drop fijos (no reconfigurables), con las longitudes de onda de IT#1 y OT#1/OT#2 asignadas de forma estática entre los sitios de origen y destino.

**Ventajas:**
- Menor costo relativo de la capa fotónica frente a un esquema ROADM.
- Menor complejidad de gestión inicial, adecuado si no se prevé necesidad de reconfiguración frecuente de canales.

**Limitaciones:**
- Menor flexibilidad ante crecimiento futuro o cambios en el patrón de tráfico entre sitios.
- Cualquier cambio en el enrutamiento de longitudes de onda requeriría intervención física.

**Riesgos:**
- Técnico: si la expectativa de crecimiento (no informada aún, ver brechas) resulta significativa, esta opción podría requerir un rediseño de la capa óptica antes de lo previsto.
- Operativo: menor tolerancia a cambios de última hora en la asignación de canales durante la implementación.

## Alternativas de interfaces tributarias

Dado que el cliente indicó explícitamente que las interfaces tributarias no están claras, se presentan alternativas típicas para servicios de 400 Gbps, sujetas a confirmación de protocolo/tráfico real (ver Preguntas de aclaración):

- **100GbE x4 (agregado en un canal de 400G):** adecuado si el tráfico es predominantemente Ethernet de datacenter/IT.
- **400GbE nativo:** adecuado si existe un único flujo de 400G Ethernet a transportar.
- **OTU4 / structura OTN:** adecuado si se requiere transporte multiservicio u otros protocolos (SAN, Fibre Channel, etc.) sobre la misma infraestructura.
- **Combinación mixta de interfaces de menor velocidad agregadas:** aplicable si existen múltiples flujos de menor tasa a consolidar en el canal de 400G.

La selección final depende de la naturaleza del tráfico de IT#1 y OT#1/OT#2, que aún no ha sido confirmada por el cliente.

## Interconexión con red(es) existente(s) del cliente

*(Se evalúa porque el cliente solicitó explícitamente alternativas de interconexión. Información de las redes existentes de BMINING no fue proporcionada; las alternativas siguientes son genéricas y deben refinarse una vez se conozca la plataforma, capacidad y ubicación de la red existente.)*

### Alternativa A — Interconexión óptica directa (extensión de capa DWDM)
**Descripción:** Uno de los 3 sitios del nuevo anillo actúa como punto de interconexión óptica con la red existente de BMINING, extendiendo o interconectando longitudes de onda entre ambas redes.
**Ventajas:** Evita conversión de capa, potencialmente menor latencia adicional.
**Limitaciones:** Requiere que la plataforma existente sea compatible o interoperable con el C-4615 en la capa fotónica.
**Riesgos:** Riesgo técnico de interoperabilidad entre plataformas si la red existente no es de la misma familia; riesgo operativo si el sitio de interconexión no tiene capacidad de puertos ópticos disponibles.

### Alternativa B — Interconexión a nivel de capa de paquete/cliente (Ethernet/OTN grooming)
**Descripción:** La interconexión se realiza a nivel de servicio (Ethernet u OTN), donde el tráfico se extrae de la capa óptica en un sitio común y se entrega a la red existente mediante interfaces de cliente.
**Ventajas:** Mayor independencia entre plataformas fotónicas de ambas redes; más simple de implementar si las plataformas no son interoperables a nivel óptico.
**Limitaciones:** Requiere equipo adicional de grooming/switching en el sitio de interconexión; puede introducir latencia adicional.
**Riesgos:** Operativo: necesidad de coordinar ventanas de corte en la red existente; técnico: dependiendo del protocolo, puede requerir conversión de medios.

### Alternativa C — Servicio arrendado/gestionado como punto de interconexión temporal
**Descripción:** Mientras el nuevo anillo se implementa, se utiliza un enlace arrendado o gestionado como puente temporal hacia la red existente.
**Ventajas:** Permite continuidad de servicio durante la etapa de construcción de los nuevos sitios.
**Limitaciones:** Costo operativo adicional, capacidad limitada según el proveedor del servicio arrendado.
**Riesgos:** Operativo: dependencia de terceros y SLAs externos.

**Nota importante:** sin conocer la ubicación, plataforma y capacidad de la(s) red(es) existente(s) de BMINING, estas alternativas son preliminares y de carácter genérico.

---

# Evaluación de la preparación para la cotización o estimación

*(Nota de gobernanza: esta fase requiere revisión y aprobación explícita del SE antes de ser utilizada en cualquier paso posterior.)*

**Estado: No listo** (para cotización formal) / **Parcialmente listo** (para una estimación presupuestaria preliminar/ROM de alto nivel, con supuestos explícitos y advertencias claras de incertidumbre).

**Justificación:**
- Los sitios aún no existen, por lo que no hay confirmación de distancia real de ruta de fibra, disponibilidad de fibra, ni condiciones de energía/espacio — información crítica para dimensionar la capa fotónica (necesidad o no de amplificación, tipo de tarjetas de línea).
- El esquema de protección no está definido, lo que afecta directamente la cantidad de tarjetas y puertos a incluir en el BoM.
- Las interfaces tributarias no están definidas, lo que impide precisar tarjetas cliente, cantidad de puertos y tipo de óptica.
- No se cuenta con información sobre la red existente de BMINING para dimensionar la interconexión solicitada.
- Dado lo anterior, es posible avanzar únicamente con un **BoM estructural preliminar basado en supuestos declarados**, sin precios reales (los precios deben marcarse como "Pendiente de cotización con Producto/Pricing" conforme a las restricciones del proceso), y con todas las brechas de información señaladas explícitamente.
- El plazo de 10 días es de alto riesgo dado el volumen de información pendiente; se recomienda comunicar al cliente que el entregable en ese plazo será un ROM preliminar sujeto a revisión una vez se resuelvan las brechas críticas (particularmente sitios, fibra y esquema de protección).

---

# Borrador de la nota de ingeniería

*(Nota de gobernanza: este borrador requiere revisión y aprobación explícita del SE antes de ser presentado internamente o al cliente.)*

**Resumen de la oportunidad**
BMINING (cliente existente) solicita una estimación presupuestaria preliminar para una nueva red DWDM en anillo de 3 sitios en San Juan, Argentina, con 2 canales ópticos iniciales a 400 Gbps cada uno, equipo redundante (2x C-4615 por sitio) y alternativas de interconexión con su red existente. Los sitios físicos aún no existen. Plazo solicitado: 10 días.

**Requisitos del cliente**
Ver sección "Requisitos del cliente" arriba.

**Supuestos de diseño**
- Distancia declarada <50 km corresponde a ruta de fibra (a confirmar).
- No se requeriría amplificación óptica en línea dado que las distancias declaradas son cortas (a confirmar con datos reales una vez existan los sitios).
- Esquema de protección: no asumido, pendiente de definición con el cliente.

**Solución(es) propuesta(s)**
Dos alternativas de arquitectura óptica (ROADM vs. OADM fijo) y alternativas de interfaz tributaria, presentadas para discusión y decisión conjunta con el cliente (ver sección "Alternativas de solución"). Tres alternativas de interconexión con red(es) existente(s) de BMINING, de carácter preliminar por falta de información sobre dicha(s) red(es).

**Cuestiones pendientes**
Ver secciones "Inconsistencias detectadas" e "Información faltante" arriba — en particular: aclaración de nombres de canales, disponibilidad de sitios y fibra, esquema de protección, interfaces tributarias, y datos de la red existente a interconectar.

**Riesgos**
- Técnico: dimensionamiento del BoM basado en supuestos no confirmados (protección, amplificación, interfaces).
- Técnico: interoperabilidad desconocida con la red existente de BMINING.
- Operativo: plazo de 10 días es ajustado dado el volumen de información pendiente y que los sitios físicos aún no existen.
- Operativo: cronograma de implementación real dependerá de la disponibilidad física de los sitios, no informada.

**Próximos pasos**
1. Confirmar con el cliente la inconsistencia de nombres de canales.
2. Obtener respuestas a las preguntas de aclaración (Fase 2).
3. Validar con el SE las alternativas de arquitectura antes de avanzar al BoM detallado.
4. Preparar reunión de seguimiento (ver Fase 6) para resolver brechas críticas dentro del plazo de 10 días.

---

# Reunión de seguimiento con el cliente

*(Nota de gobernanza: este borrador de reunión requiere revisión del SE antes de coordinarse con el cliente.)*

**Objetivo**
Resolver las brechas de información críticas identificadas y validar con BMINING las alternativas de arquitectura, interfaces tributarias e interconexión, a fin de encuadrar correctamente el alcance del BoM presupuestario dentro del plazo solicitado.

**Orden del día**
1. Confirmación de la inconsistencia en nombres de canales (IT#1/OT#1 vs. OT#2).
2. Estado de los sitios: ubicación, disponibilidad física estimada, energía y espacio.
3. Disponibilidad de fibra entre sitios.
4. Definición de esquema de protección esperado.
5. Definición de tipo de tráfico e interfaces tributarias para IT#1 y OT#1/OT#2.
6. Expectativas de crecimiento futuro de capacidad/canales.
7. Datos de la red existente de BMINING para evaluar interconexión.
8. Alineación sobre alcance y limitaciones del entregable dado el plazo de 10 días.

**Temas clave de discusión**
- El plazo de 10 días permite entregar un ROM preliminar basado en supuestos, no una cotización formal, dado que los sitios aún no existen.
- Las alternativas de arquitectura (ROADM vs. fijo) tienen implicancias de costo y flexibilidad futura que requieren decisión del cliente.
- La interconexión con la red existente depende de información que el cliente debe proporcionar.

**Decisiones requeridas del cliente**
- Confirmación del nombre correcto de los canales.
- Elección preliminar de arquitectura (ROADM vs. fijo), o solicitud de mantener ambas opciones abiertas en el BoM.
- Confirmación de tipo de tráfico/interfaz tributaria esperada.
- Confirmación de esquema de protección deseado.
- Datos de la red existente para interconexión.

**Información que aún se requiere**
Ver sección "Información faltante" arriba.

**Resultados esperados**
- Reducción de las brechas críticas de información.
- Acuerdo sobre el alcance y las limitaciones del ROM preliminar a entregar en el plazo de 10 días.
- Definición de próximos pasos para una eventual cotización formal una vez confirmada la disponibilidad de sitios y fibra.

---

# Próximas acciones recomendadas

1. **SE debe revisar y aprobar explícitamente** las Fases 3, 4 y 5 antes de que esta información se use en cualquier comunicación con el cliente o en la preparación del BoM.
2. Enviar al cliente las preguntas de aclaración antes o durante la reunión de seguimiento, dado el plazo ajustado de 10 días.
3. Confirmar con el cliente si el plazo de 10 días es para el ROM preliminar o para la implementación completa.
4. Una vez resueltas las brechas críticas (sitios, fibra, protección, interfaces, datos de red existente), reevaluar el estado de preparación para cotización formal.
5. Si se requiere el BoM estructural preliminar (ítems y cantidades sin precios reales) antes de la reunión de seguimiento, indicarlo explícitamente para generarlo como entregable separado, marcando todos los precios como "Pendiente de cotización con Producto/Pricing".