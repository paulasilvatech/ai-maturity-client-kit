# AI Maturity Assessment, Pilar P3: Plataforma de Aplicações (Plataforma de Aplicaciones)

> Mide la sofisticación de la plataforma: arquitectura cloud-native, APIs, IA, datos, agentes, identidad, multi-cloud, performance y FinOps.

> [!IMPORTANT]
> Edición localizada runtime-safe: etiquetas estructurales en Español y todos los IDs preservados.
> El wording canónico de las preguntas (el texto de cada encabezado `P3-Cx-Qy`) se conserva en Portugués, byte-idéntico al banco de preguntas de Microsoft Forms, para mantener paridad estricta de scoring y auditoría con el workbook.

## Visión general

- **Pilar:** `P3`, Plataforma de Aplicações (Plataforma de Aplicaciones)
- **Capacidades (capabilities):** 9
- **Preguntas totales:** 46
- **Escala:** Likert L0–L4 (Inicial → Optimizando)
- **Idioma de la pregunta:** Portugués (Brasil), wording canónico preservado en todas las ediciones
- **Idioma de KPI/contexto/evidencia:** Inglés (términos técnicos universales)
- **Respuesta esperada por pregunta:** 1 nivel seleccionado + texto de evidencia (mínimo recomendado 80 caracteres) + anexo opcional

## Cómo interpretar la escala

| Nivel | Etiqueta | Significado |
|---|---|---|
| **L0** | Inicial | Sin práctica establecida; acciones ad-hoc, sin herramienta ni política. |
| **L1** | En Desarrollo | Pilotos aislados, cobertura <25%, sin gobernanza. |
| **L2** | Definido | Adopción en 25–50% de los equipos, con directrices y capacitación básica. |
| **L3** | Gestionado | Cobertura >75% con métricas de impacto y bibliotecas/plantillas compartidas. |
| **L4** | Optimizando | Cobertura casi universal (>95%), automatización, ajuste fino, mejora continua medida. |

## Tipos de información recolectada por pregunta

Cada pregunta captura simultáneamente **tres tipos de dato**:

1. **Cuantitativo (KPI):** una métrica numérica explícita (ej.: % de desarrolladores activos, MTTR, lead time, tasa de cobertura). Usa el KPI sugerido para estandarizar la comparación entre equipos.

2. **Cualitativo (descripción del nivel):** el encuestado selecciona el nivel L0–L4 cuya descripción mejor representa la realidad observada hoy (no la aspiracional).

3. **Evidencia (texto + anexos):** prueba documental: link de pipeline, screenshot de dashboard, política, runbook, contrato de licencias, métrica exportada. Cuanto más específica, mayor la calidad de la evidencia (escala: ninguna → mínima → adecuada → detallada → ejemplar).

## Criterios de calidad de la evidencia

- **Mínima (<80 caracteres):** texto genérico, sin nombre de herramienta, métrica ni link.
- **Adecuada (80–250):** menciona herramienta + cobertura/alcance aproximado.
- **Detallada (250–500):** incluye métrica numérica + link/anexo + período de medición.
- **Ejemplar (>500 o múltiples anexos):** múltiples fuentes corroborantes, serie temporal, comparativo antes/después.

## Capacidades del pilar P3

- **P3-C1**: Arquitetura Cloud-Native (Arquitectura Cloud-Native), 5 preguntas
- **P3-C2**: Gestão de APIs (Gestión de APIs), 5 preguntas
- **P3-C3**: Desenvolvimento de Aplicações IA (Desarrollo de Aplicaciones IA), 5 preguntas
- **P3-C4**: Plataforma de Dados e Lakehouse (Plataforma de Datos y Lakehouse), 5 preguntas
- **P3-C5**: Aplicações Agênticas (Aplicaciones Agénticas), 6 preguntas
- **P3-C6**: Gestão de Identidades e Acessos (Gestión de Identidades y Accesos), 5 preguntas
- **P3-C7**: Multi-Cloud e Portabilidade (Multi-Cloud y Portabilidad), 5 preguntas
- **P3-C8**: Desempenho e Escalabilidade (Desempeño y Escalabilidad), 5 preguntas
- **P3-C9**: FinOps e Otimização de Custos (FinOps y Optimización de Costos), 5 preguntas

---

## P3-C1: Arquitetura Cloud-Native (Arquitectura Cloud-Native)

**5 preguntas en esta capability.**

### P3-C1-Q1: Qual é a maturidade da adoção de arquitetura cloud-native?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `% workloads containerized`

**Contexto**

- **Qué mide (what):** Measures adoption of cloud-native patterns including containerization, orchestration, and service decomposition.
- **Por qué importa (why):** Cloud-native architectures enable 10x faster scaling, 99.99% availability, and 50% infrastructure cost reduction.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Aplicaciones monolíticas desplegadas en VMs o bare metal. Sin containerización. | • No container adoption<br>• VM-based deployment topology<br>• Monolithic architecture in use |
| **L1** | En Desarrollo | Algunas aplicaciones containerizadas (<30%). Docker usado para desarrollo pero no para producción. | • <30% containerized rate measured<br>• Docker in dev only<br>• No orchestration platform |
| **L2** | Definido | 50-70% de los workloads containerizados. Kubernetes u orquestación de contenedores en producción. Descomposición básica en microservicios. | • 50-70% containerized rate measured<br>• K8s in production<br>• Some microservices deployed |
| **L3** | Gestionado | >85% de los workloads cloud-native. Service mesh, despliegue GitOps, escalado automatizado. Límites de servicio bien definidos. | • >85% cloud-native rate measured<br>• Service mesh deployed<br>• GitOps workflow adopted<br>• Automated scaling rules configured |
| **L4** | Otimizando | Cloud-native completo con asignación de recursos optimizada por IA, auto-escalado predictivo, infraestructura self-healing y serverless donde sea apropiado. | • AI resource optimization<br>• Predictive automated scaling enabled<br>• Self-healing infrastructure enabled<br>• Serverless platform adoption |

---

### P3-C1-Q2: Em que medida Arquitetura Nativa da Nuvem (container adoption) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% workloads containerized`

**Contexto**

- **Qué mide (what):** Workloads run as containers on Kubernetes or managed platforms.
- **Por qué importa (why):** Containers enable density, portability, and declarative deploys.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin container adoption implementado. Los equipos operan sin esta capacidad. | • No container adoption deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de container adoption con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | container adoption adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | container adoption estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | container adoption está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C1-Q3: Em que medida Arquitetura Nativa da Nuvem (service mesh / zero trust networking) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services on mesh`

**Contexto**

- **Qué mide (what):** Service mesh handles mTLS, retries, and traffic shaping.
- **Por qué importa (why):** Mesh moves reliability and security out of app code.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin service mesh / zero trust networking implementado. Los equipos operan sin esta capacidad. | • No service mesh / zero trust networking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de service mesh / zero trust networking con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | service mesh / zero trust networking adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | service mesh / zero trust networking estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | service mesh / zero trust networking está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C1-Q4: Em que medida Arquitetura Nativa da Nuvem (event-driven architecture) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% flows async`

**Contexto**

- **Qué mide (what):** Events and queues decouple services for resilience and scale.
- **Por qué importa (why):** EDA enables loose coupling and graceful degradation.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin event-driven architecture implementado. Los equipos operan sin esta capacidad. | • No event-driven architecture deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de event-driven architecture con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | event-driven architecture adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | event-driven architecture estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | event-driven architecture está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C1-Q5: Em que medida Arquitetura Nativa da Nuvem (managed services preference) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% managed vs self-hosted`

**Contexto**

- **Qué mide (what):** Prefer managed databases, queues, and caches over self-operated.
- **Por qué importa (why):** Managed services shift ops burden to the cloud provider.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin managed services preference implementado. Los equipos operan sin esta capacidad. | • No managed services preference deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de managed services preference con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | managed services preference adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | managed services preference estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | managed services preference está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C2: Gestão de APIs (Gestión de APIs)

**5 preguntas en esta capability.**

### P3-C2-Q1: Quão madura é sua estratégia de gestão de APIs?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma, Desarrollador, engineering-leader, Seguridad
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `% APIs with OpenAPI spec`

**Contexto**

- **Qué mide (what):** Measures the maturity of API design, documentation, versioning, and governance practices.
- **Por qué importa (why):** Well-managed APIs reduce integration time by 70% and enable partner ecosystem growth.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin estándares de API. APIs diseñadas ad-hoc. Sin documentación más allá del código fuente. | • No API standards<br>• Ad-hoc API design<br>• No API documentation |
| **L1** | En Desarrollo | Algunas APIs tienen documentación básica. Sin estrategia de versionado. Manejo de errores inconsistente. | • Basic API docs exist<br>• No versioning policy<br>• Inconsistent error formats |
| **L2** | Definido | Specs OpenAPI para >50% de las APIs. Directrices de diseño de API documentadas. Estrategia de versionado definida. | • >50% APIs with OpenAPI<br>• Design guidelines doc<br>• API versioning strategy documented |
| **L3** | Gestionado | API gateway con gestión centralizada. >80% de las APIs documentadas. Rate limiting, auth y monitoreo estandarizados. Gestión del ciclo de vida de las APIs. | • API gateway deployed<br>• >80% documented rate measured<br>• Standardized auth/rate limiting |
| **L4** | Otimizando | Gestión de APIs potenciada por IA: docs auto-generadas desde el código, detección de anomalías en el tráfico de API, planificación predictiva de capacidad, verificaciones automatizadas de compatibilidad retroactiva. | • Auto-generated API docs<br>• Traffic anomaly detection<br>• Predictive capacity planning<br>• Auto compatibility checks |

---

### P3-C2-Q2: Em que medida Gestão de APIs (API gateway for all external APIs) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma, Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% APIs behind gateway`

**Contexto**

- **Qué mide (what):** Gateway handles auth, rate limiting, and observability.
- **Por qué importa (why):** A gateway centralizes cross-cutting API concerns.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin api gateway for all external apis implementado. Los equipos operan sin esta capacidad. | • No API gateway for all external APIs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de api gateway for all external apis con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | API gateway for all external APIs adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | API gateway for all external APIs estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | API gateway for all external APIs está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C2-Q3: Em que medida Gestão de APIs (OpenAPI contracts) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma, Desarrollador, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% APIs with spec`

**Contexto**

- **Qué mide (what):** Every API has a machine-readable contract.
- **Por qué importa (why):** Contracts enable codegen, mock servers, and compatibility testing.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin openapi contracts implementado. Los equipos operan sin esta capacidad. | • No OpenAPI contracts deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de openapi contracts con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | OpenAPI contracts adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | OpenAPI contracts estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | OpenAPI contracts está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C2-Q4: Em que medida Gestão de APIs (versioning & deprecation policy) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma, Desarrollador, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `deprecated APIs retired on time`

**Contexto**

- **Qué mide (what):** Explicit versioning and deprecation schedules.
- **Por qué importa (why):** Clear policy preserves customer trust and avoids breakage.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin versioning & deprecation policy implementado. Los equipos operan sin esta capacidad. | • No versioning & deprecation policy deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de versioning & deprecation policy con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | versioning & deprecation policy adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | versioning & deprecation policy estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | versioning & deprecation policy está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C2-Q5: Em que medida Gestão de APIs (developer portal with self-serve keys) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma, Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `time-to-first-call`

**Contexto**

- **Qué mide (what):** Self-service key issuance and interactive docs.
- **Por qué importa (why):** Dev portals accelerate partner integration.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin developer portal with self-serve keys implementado. Los equipos operan sin esta capacidad. | • No developer portal with self-serve keys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de developer portal with self-serve keys con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | developer portal with self-serve keys adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | developer portal with self-serve keys estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | developer portal with self-serve keys está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C3: Desenvolvimento de Aplicações IA (Desarrollo de Aplicaciones IA)

**5 preguntas en esta capability.**

### P3-C3-Q1: Quão madura é a capacidade da sua organização de construir e implantar aplicações com IA?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `# AI features in production`

**Contexto**

- **Qué mide (what):** Measures the organization's capability to develop, deploy, and maintain AI-powered application features.
- **Por qué importa (why):** Organizations with mature AI application development ship AI features 5x faster and with 3x fewer production incidents.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin funcionalidades de IA en aplicaciones de producción. Sin capacidad del equipo para desarrollo de IA. | • No AI features deployed<br>• No ML/AI engineering skills<br>• No AI development tools |
| **L1** | En Desarrollo | Experimentando con APIs de IA (OpenAI, Azure AI) en 1-2 aplicaciones. Sin prácticas de MLOps. | • 1-2 AI experiments<br>• Direct API integration<br>• No MLOps tooling in place |
| **L2** | Definido | 3-5 funcionalidades con IA en producción. Prácticas básicas de prompt engineering. Patrón RAG para recuperación de conocimiento. | • 3-5 AI features live<br>• Prompt engineering guidelines<br>• RAG implementation deployed |
| **L3** | Gestionado | Framework estandarizado de desarrollo de IA. Pipeline de evaluación de modelos. Versionado de prompts y pruebas A/B. >10 funcionalidades de IA en producción. | • AI dev framework docs<br>• Model evaluation pipeline<br>• Prompt versioning workflow<br>• >10 AI features |
| **L4** | Otimizando | Aplicaciones AI-native con agentes autónomos, orquestación multi-modelo, evaluación continua de modelos y optimización automatizada de prompts. Las funcionalidades de IA son núcleo del producto. | • Autonomous agent deployments<br>• Multi-model orchestration enabled<br>• Continuous model eval<br>• Automated prompt optimization |

---

### P3-C3-Q2: Em que medida Desenvolvimento de Aplicações de IA (LLM application frameworks) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% AI apps on framework`

**Contexto**

- **Qué mide (what):** Teams use frameworks (LangChain, Semantic Kernel) for LLM apps.
- **Por qué importa (why):** Frameworks accelerate RAG, agents, and evaluation patterns.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin llm application frameworks implementado. Los equipos operan sin esta capacidad. | • No LLM application frameworks deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de llm application frameworks con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | LLM application frameworks adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | LLM application frameworks estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | LLM application frameworks está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C3-Q3: Em que medida Desenvolvimento de Aplicações de IA (evaluation harness for AI) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `evals per release`

**Contexto**

- **Qué mide (what):** Automated evals run on every model or prompt change.
- **Por qué importa (why):** AI evals catch regressions that unit tests cannot.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin evaluation harness for ai implementado. Los equipos operan sin esta capacidad. | • No evaluation harness for AI deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de evaluation harness for ai con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | evaluation harness for AI adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | evaluation harness for AI estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | evaluation harness for AI está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C3-Q4: Em que medida Desenvolvimento de Aplicações de IA (vector database / RAG platform) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `RAG apps in prod`

**Contexto**

- **Qué mide (what):** A shared vector store/RAG platform serves multiple apps.
- **Por qué importa (why):** Centralized RAG reduces duplicated work across teams.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin vector database / rag platform implementado. Los equipos operan sin esta capacidad. | • No vector database / RAG platform deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de vector database / rag platform con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | vector database / RAG platform adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | vector database / RAG platform estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | vector database / RAG platform está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C3-Q5: Em que medida Desenvolvimento de Aplicações de IA (responsible AI / safety filters) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Desarrollador, Arquitecto, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% AI apps with guardrails`

**Contexto**

- **Qué mide (what):** All AI apps integrate content safety and audit logging.
- **Por qué importa (why):** Responsible AI is table stakes; retrofitting is expensive.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin responsible ai / safety filters implementado. Los equipos operan sin esta capacidad. | • No responsible AI / safety filters deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de responsible ai / safety filters con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | responsible AI / safety filters adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | responsible AI / safety filters estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | responsible AI / safety filters está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C4: Plataforma de Dados e Lakehouse (Plataforma de Datos y Lakehouse)

**5 preguntas en esta capability.**

### P3-C4-Q1: Em que medida Plataforma de Dados e Lakehouse (lakehouse or data platform in use) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% data in platform`

**Contexto**

- **Qué mide (what):** A lakehouse unifies structured and unstructured data.
- **Por qué importa (why):** Lakehouses combine warehouse performance with lake flexibility.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin lakehouse or data platform in use implementado. Los equipos operan sin esta capacidad. | • No lakehouse or data platform in use deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de lakehouse or data platform in use con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | lakehouse or data platform in use adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | lakehouse or data platform in use estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | lakehouse or data platform in use está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q2: Em que medida Plataforma de Dados e Lakehouse (data contracts between producers & consumers) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% pipelines with contracts`

**Contexto**

- **Qué mide (what):** Data contracts declare schema and quality guarantees.
- **Por qué importa (why):** Contracts prevent silent breakage between teams.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin data contracts between producers & consumers implementado. Los equipos operan sin esta capacidad. | • No data contracts between producers & consumers deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de data contracts between producers & consumers con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | data contracts between producers & consumers adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | data contracts between producers & consumers estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | data contracts between producers & consumers está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q3: Em que medida Plataforma de Dados e Lakehouse (catalog and lineage tracking) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% datasets cataloged`

**Contexto**

- **Qué mide (what):** Every dataset has ownership, lineage, and quality metadata.
- **Por qué importa (why):** Catalogs accelerate discovery and investigations.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin catalog and lineage tracking implementado. Los equipos operan sin esta capacidad. | • No catalog and lineage tracking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de catalog and lineage tracking con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | catalog and lineage tracking adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | catalog and lineage tracking estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | catalog and lineage tracking está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q4: Em que medida Plataforma de Dados e Lakehouse (self-service analytics) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% decisions using data`

**Contexto**

- **Qué mide (what):** Business users query data themselves via governed tools.
- **Por qué importa (why):** Self-service shifts the bottleneck off the data team.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin self-service analytics implementado. Los equipos operan sin esta capacidad. | • No self-service analytics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de self-service analytics con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | self-service analytics adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | self-service analytics estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | self-service analytics está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q5: Em que medida Plataforma de Dados e Lakehouse (real-time streaming ingestion) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% use-cases real-time`

**Contexto**

- **Qué mide (what):** Streaming is available for time-sensitive use cases.
- **Por qué importa (why):** Real-time data enables fresher AI and operational decisions.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin real-time streaming ingestion implementado. Los equipos operan sin esta capacidad. | • No real-time streaming ingestion deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de real-time streaming ingestion con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | real-time streaming ingestion adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | real-time streaming ingestion estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | real-time streaming ingestion está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C5: Aplicações Agênticas (Aplicaciones Agénticas)

**6 preguntas en esta capability.**

### P3-C5-Q1: Em que medida Aplicações Agênticas (agents with tool-use in prod) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `agents in production`

**Contexto**

- **Qué mide (what):** Agents call tools and APIs to perform multi-step work.
- **Por qué importa (why):** Agentic workflows automate complex tasks humans used to route.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin agents with tool-use in prod implementado. Los equipos operan sin esta capacidad. | • No agents with tool-use in prod deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de agents with tool-use in prod con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | agents with tool-use in prod adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | agents with tool-use in prod estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | agents with tool-use in prod está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q2: Em que medida Aplicações Agênticas (orchestration framework (Semantic Kernel, etc)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% agents on framework`

**Contexto**

- **Qué mide (what):** Agents are built on a standard orchestration runtime.
- **Por qué importa (why):** Standard runtimes reduce per-agent engineering cost.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin orchestration framework (semantic kernel, etc) implementado. Los equipos operan sin esta capacidad. | • No orchestration framework (Semantic Kernel, etc) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de orchestration framework (semantic kernel, etc) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | orchestration framework (Semantic Kernel, etc) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | orchestration framework (Semantic Kernel, etc) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | orchestration framework (Semantic Kernel, etc) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q3: Em que medida Aplicações Agênticas (evaluation and safety for agents) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `eval scenarios per agent`

**Contexto**

- **Qué mide (what):** Agents are evaluated for safety, cost, and task completion.
- **Por qué importa (why):** Agent evaluation is different from LLM evaluation.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin evaluation and safety for agents implementado. Los equipos operan sin esta capacidad. | • No evaluation and safety for agents deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de evaluation and safety for agents con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | evaluation and safety for agents adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | evaluation and safety for agents estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | evaluation and safety for agents está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q4: Em que medida Aplicações Agênticas (tool/action registry) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de Plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `tools available to agents`

**Contexto**

- **Qué mide (what):** A governed registry lists tools agents may call.
- **Por qué importa (why):** A registry controls blast radius and enables auditing.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin tool/action registry implementado. Los equipos operan sin esta capacidad. | • No tool/action registry deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de tool/action registry con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | tool/action registry adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | tool/action registry estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | tool/action registry está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q5: Em que medida Aplicações Agênticas (human-in-the-loop controls) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% agents with HITL`

**Contexto**

- **Qué mide (what):** High-stakes actions require human confirmation.
- **Por qué importa (why):** HITL lets teams ship agents safely while learning.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin human-in-the-loop controls implementado. Los equipos operan sin esta capacidad. | • No human-in-the-loop controls deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de human-in-the-loop controls con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | human-in-the-loop controls adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | human-in-the-loop controls estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | human-in-the-loop controls está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q6: Em que medida Aplicações Agênticas (agent cost and latency telemetry) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** data-ai, Arquitecto, Ingeniero de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `p95 agent step latency`

**Contexto**

- **Qué mide (what):** Agent performance and cost are tracked per step.
- **Por qué importa (why):** Telemetry is required to run agents profitably at scale.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin agent cost and latency telemetry implementado. Los equipos operan sin esta capacidad. | • No agent cost and latency telemetry deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de agent cost and latency telemetry con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | agent cost and latency telemetry adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | agent cost and latency telemetry estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | agent cost and latency telemetry está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C6: Gestão de Identidades e Acessos (Gestión de Identidades y Accesos)

**5 preguntas en esta capability.**

### P3-C6-Q1: Em que medida Gestão de Identidades e Acessos (SSO for all apps) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% apps behind SSO`

**Contexto**

- **Qué mide (what):** All apps authenticate via central SSO.
- **Por qué importa (why):** SSO is the foundation of user lifecycle and revocation.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin sso for all apps implementado. Los equipos operan sin esta capacidad. | • No SSO for all apps deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de sso for all apps con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SSO for all apps adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | SSO for all apps estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | SSO for all apps está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q2: Em que medida Gestão de Identidades e Acessos (workload identity (no long-lived secrets)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% workloads using WI`

**Contexto**

- **Qué mide (what):** Workloads use managed identity, not static keys.
- **Por qué importa (why):** Managed identities eliminate an entire class of leak.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin workload identity (no long-lived secrets) implementado. Los equipos operan sin esta capacidad. | • No workload identity (no long-lived secrets) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de workload identity (no long-lived secrets) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | workload identity (no long-lived secrets) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | workload identity (no long-lived secrets) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | workload identity (no long-lived secrets) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q3: Em que medida Gestão de Identidades e Acessos (least-privilege with JIT elevation) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% access through JIT`

**Contexto**

- **Qué mide (what):** Standing admin is replaced by just-in-time elevation.
- **Por qué importa (why):** JIT dramatically reduces blast radius of compromised accounts.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin least-privilege with jit elevation implementado. Los equipos operan sin esta capacidad. | • No least-privilege with JIT elevation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de least-privilege with jit elevation con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | least-privilege with JIT elevation adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | least-privilege with JIT elevation estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | least-privilege with JIT elevation está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q4: Em que medida Gestão de Identidades e Acessos (conditional access policies) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% sessions policy-evaluated`

**Contexto**

- **Qué mide (what):** Access is granted based on device, location, and risk.
- **Por qué importa (why):** Conditional access adapts security to context.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin conditional access policies implementado. Los equipos operan sin esta capacidad. | • No conditional access policies deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de conditional access policies con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | conditional access policies adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | conditional access policies estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | conditional access policies está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q5: Em que medida Gestão de Identidades e Acessos (access reviews and audit) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `access reviews per year`

**Contexto**

- **Qué mide (what):** Access is reviewed at least quarterly and logged.
- **Por qué importa (why):** Reviews prevent access drift from acquisitions and reorgs.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin access reviews and audit implementado. Los equipos operan sin esta capacidad. | • No access reviews and audit deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de access reviews and audit con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | access reviews and audit adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | access reviews and audit estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | access reviews and audit está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C7: Multi-Cloud e Portabilidade (Multi-Cloud y Portabilidad)

**5 preguntas en esta capability.**

### P3-C7-Q1: Em que medida Multi-Cloud e Portabilidade (container-based workloads for portability) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% workloads portable`

**Contexto**

- **Qué mide (what):** Workloads run in containers on any cloud.
- **Por qué importa (why):** Portability is a hedge against lock-in and outages.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin container-based workloads for portability implementado. Los equipos operan sin esta capacidad. | • No container-based workloads for portability deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de container-based workloads for portability con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | container-based workloads for portability adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | container-based workloads for portability estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | container-based workloads for portability está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q2: Em que medida Multi-Cloud e Portabilidade (abstracted data tier (Postgres, etc)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% data on portable engines`

**Contexto**

- **Qué mide (what):** Data services use open standards (Postgres, MySQL).
- **Por qué importa (why):** Open engines keep migration costs bounded.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin abstracted data tier (postgres, etc) implementado. Los equipos operan sin esta capacidad. | • No abstracted data tier (Postgres, etc) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de abstracted data tier (postgres, etc) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | abstracted data tier (Postgres, etc) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | abstracted data tier (Postgres, etc) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | abstracted data tier (Postgres, etc) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q3: Em que medida Multi-Cloud e Portabilidade (multi-region deployment capability) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services multi-region`

**Contexto**

- **Qué mide (what):** Services can run active-active across regions.
- **Por qué importa (why):** Multi-region capability is required for DR and compliance.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin multi-region deployment capability implementado. Los equipos operan sin esta capacidad. | • No multi-region deployment capability deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de multi-region deployment capability con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | multi-region deployment capability adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | multi-region deployment capability estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | multi-region deployment capability está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q4: Em que medida Multi-Cloud e Portabilidade (cloud-agnostic IaC modules) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% modules cloud-agnostic`

**Contexto**

- **Qué mide (what):** IaC modules abstract provider specifics where sensible.
- **Por qué importa (why):** Thoughtful abstraction limits porting pain.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin cloud-agnostic iac modules implementado. Los equipos operan sin esta capacidad. | • No cloud-agnostic IaC modules deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de cloud-agnostic iac modules con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | cloud-agnostic IaC modules adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | cloud-agnostic IaC modules estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | cloud-agnostic IaC modules está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q5: Em que medida Multi-Cloud e Portabilidade (disaster recovery drills) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Arquitecto, Ingeniero de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `DR drills per year`

**Contexto**

- **Qué mide (what):** Annual DR drills validate recovery time and process.
- **Por qué importa (why):** Untested DR is not DR.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin disaster recovery drills implementado. Los equipos operan sin esta capacidad. | • No disaster recovery drills deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de disaster recovery drills con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | disaster recovery drills adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | disaster recovery drills estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | disaster recovery drills está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C8: Desempenho e Escalabilidade (Desempeño y Escalabilidad)

**5 preguntas en esta capability.**

### P3-C8-Q1: Em que medida Desempenho e Escalabilidade (performance budgets per service) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Arquitecto, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with perf budget`

**Contexto**

- **Qué mide (what):** Services declare latency and throughput budgets.
- **Por qué importa (why):** Budgets turn performance into a first-class requirement.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin performance budgets per service implementado. Los equipos operan sin esta capacidad. | • No performance budgets per service deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de performance budgets per service con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | performance budgets per service adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | performance budgets per service estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | performance budgets per service está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q2: Em que medida Desempenho e Escalabilidade (load/stress testing in CI) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services load-tested`

**Contexto**

- **Qué mide (what):** Load tests run on every release candidate.
- **Por qué importa (why):** Catching regressions in CI beats catching them in prod.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin load/stress testing in ci implementado. Los equipos operan sin esta capacidad. | • No load/stress testing in CI deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de load/stress testing in ci con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | load/stress testing in CI adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | load/stress testing in CI estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | load/stress testing in CI está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q3: Em que medida Desempenho e Escalabilidade (autoscaling based on real demand) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Arquitecto, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services autoscaled`

**Contexto**

- **Qué mide (what):** Services autoscale on CPU, latency, or queue depth.
- **Por qué importa (why):** Autoscaling matches cost to demand.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin autoscaling based on real demand implementado. Los equipos operan sin esta capacidad. | • No autoscaling based on real demand deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de autoscaling based on real demand con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | autoscaling based on real demand adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | autoscaling based on real demand estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | autoscaling based on real demand está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q4: Em que medida Desempenho e Escalabilidade (profiling in production) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services continuously profiled`

**Contexto**

- **Qué mide (what):** Always-on profiling (e.g., pyroscope, parca) runs in prod.
- **Por qué importa (why):** Prod profiling surfaces bottlenecks real users hit.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin profiling in production implementado. Los equipos operan sin esta capacidad. | • No profiling in production deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de profiling in production con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | profiling in production adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | profiling in production estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | profiling in production está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q5: Em que medida Desempenho e Escalabilidade (capacity planning cadence) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `capacity reviews per year`

**Contexto**

- **Qué mide (what):** Capacity is reviewed with growth projections.
- **Por qué importa (why):** Planning prevents painful migrations at peak load.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin capacity planning cadence implementado. Los equipos operan sin esta capacidad. | • No capacity planning cadence deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de capacity planning cadence con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | capacity planning cadence adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | capacity planning cadence estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | capacity planning cadence está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C9: FinOps e Otimização de Custos (FinOps y Optimización de Costos)

**5 preguntas en esta capability.**

### P3-C9-Q1: Em que medida FinOps e Otimização de Custos (cost allocation & showback) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% cost tagged to team`

**Contexto**

- **Qué mide (what):** Every resource is tagged and attributed to a team.
- **Por qué importa (why):** Showback creates ownership for cost.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin cost allocation & showback implementado. Los equipos operan sin esta capacidad. | • No cost allocation & showback deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de cost allocation & showback con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | cost allocation & showback adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | cost allocation & showback estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | cost allocation & showback está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q2: Em que medida FinOps e Otimização de Custos (committed use / savings plans) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% eligible spend committed`

**Contexto**

- **Qué mide (what):** Commit spend is used where usage is predictable.
- **Por qué importa (why):** Commitments cut spend 20-50% at minimal risk.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin committed use / savings plans implementado. Los equipos operan sin esta capacidad. | • No committed use / savings plans deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de committed use / savings plans con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | committed use / savings plans adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | committed use / savings plans estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | committed use / savings plans está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q3: Em que medida FinOps e Otimização de Custos (idle and unused resource cleanup) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de Plataforma, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `$/month saved by cleanup`

**Contexto**

- **Qué mide (what):** Automation flags and removes idle resources.
- **Por qué importa (why):** Cleanup is the highest-leverage FinOps activity.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin idle and unused resource cleanup implementado. Los equipos operan sin esta capacidad. | • No idle and unused resource cleanup deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de idle and unused resource cleanup con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | idle and unused resource cleanup adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | idle and unused resource cleanup estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | idle and unused resource cleanup está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q4: Em que medida FinOps e Otimização de Custos (rightsizing recommendations) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% rightsizing applied`

**Contexto**

- **Qué mide (what):** Automated recommendations drive continuous rightsizing.
- **Por qué importa (why):** Rightsizing closes the gap between provisioned and needed.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin rightsizing recommendations implementado. Los equipos operan sin esta capacidad. | • No rightsizing recommendations deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de rightsizing recommendations con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | rightsizing recommendations adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | rightsizing recommendations estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | rightsizing recommendations está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q5: Em que medida FinOps e Otimização de Custos (unit economics per product) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** product-owner, engineering-leader, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% products with $/user`

**Contexto**

- **Qué mide (what):** Products track cost per user, request, or transaction.
- **Por qué importa (why):** Unit economics align engineering and business decisions.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin unit economics per product implementado. Los equipos operan sin esta capacidad. | • No unit economics per product deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de unit economics per product con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | unit economics per product adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | unit economics per product estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | unit economics per product está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## Cómo se puntúa esta sección

- Cada pregunta recibe un valor numérico del nivel seleccionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- La puntuación de la capacidad es el promedio ponderado de las preguntas (peso default = 1.0; las preguntas con peso 1.5 o 2.0 cuentan más).
- La puntuación del pilar **P3** es el promedio de las 9 capacidades.
- El resultado se muestra en escala 0–4 y se convierte a % de madurez (nivel / 4 × 100).

## Glosario rápido

- **Pillar:** dimensión estratégica de madurez.
- **Capability:** subdominio funcional dentro de un pilar.
- **Question:** ítem de evaluación concreto, ID estándar `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0–L4):** punto en la escala Likert de madurez.
- **KPI:** indicador clave que valida objetivamente el nivel declarado.
- **Evidence:** prueba cualitativa (texto) o cuantitativa (anexo) que sustenta la respuesta.
