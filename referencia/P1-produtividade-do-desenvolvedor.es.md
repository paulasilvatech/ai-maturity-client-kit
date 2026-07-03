# AI Maturity Assessment, Pilar P1: Produtividade do Desenvolvedor (Productividad del Desarrollador)

> Mide cuánto adopta la ingeniería la IA para acelerar el ciclo de codificación, documentación, revisión, onboarding y colaboración interna.

> [!IMPORTANT]
> Edición localizada runtime-safe: etiquetas estructurales en Español y todos los IDs preservados.
> El wording canónico de las preguntas (el texto de cada encabezado `P1-Cx-Qy`) se conserva en Portugués, byte-idéntico al banco de preguntas de Microsoft Forms, para mantener paridad estricta de scoring y auditoría con el workbook.

## Visión general

- **Pilar:** `P1`, Produtividade do Desenvolvedor (Productividad del Desarrollador)
- **Capacidades (capabilities):** 9
- **Preguntas totales:** 53
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

## Capacidades del pilar P1

- **P1-C1**: Assistentes de Codificação IA (Asistentes de Codificación IA), 5 preguntas
- **P1-C2**: Plataforma de Experiência do Desenvolvedor (Plataforma de Experiencia del Desarrollador), 6 preguntas
- **P1-C3**: Gestão do Conhecimento (Gestión del Conocimiento), 6 preguntas
- **P1-C4**: Automação de Revisão de Código (Automatización de Revisión de Código), 7 preguntas
- **P1-C5**: Onboarding e Treinamento de Desenvolvedores (Onboarding y Capacitación de Desarrolladores), 7 preguntas
- **P1-C6**: Inner Source e Colaboração (Inner Source y Colaboración), 6 preguntas
- **P1-C7**: Automação de Documentação (Automatización de Documentación), 5 preguntas
- **P1-C8**: Medição de Produtividade do Desenvolvedor (Medición de Productividad del Desarrollador), 6 preguntas
- **P1-C9**: Automação de Ambientes e Espaços de Trabalho (Automatización de Entornos y Espacios de Trabajo), 5 preguntas

---

## P1-C1: Assistentes de Codificação IA (Asistentes de Codificación IA)

**5 preguntas en esta capability.**

### P1-C1-Q1: Em que medida sua organização utiliza ferramentas de completação de código com IA (ex. GitHub Copilot)?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% developers using AI completion`

**Contexto**

- **Qué mide (what):** Measures adoption of AI-powered code completion and suggestion tools across the development team.
- **Por qué importa (why):** AI coding assistants can increase developer velocity by 30-55% on routine coding tasks, reducing time-to-market.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin herramientas de codificación con IA implementadas. Todo el código se escribe manualmente sin asistencia de IA. | • No AI tool licenses<br>• No AI tool policies<br>• Manual-only coding workflows |
| **L1** | En Desarrollo | Implementación piloto de asistente de codificación IA para <10% de los desarrolladores. Uso ad-hoc sin directrices. | • Pilot program documentation<br>• < 10% license allocation<br>• No usage policy defined |
| **L2** | Definido | Asistente de codificación IA implementado para 25-50% de los desarrolladores con directrices de uso y capacitación básica. | • 25-50% license coverage<br>• Written usage guidelines<br>• Completion training materials |
| **L3** | Gestionado | Asistente de codificación IA implementado para >75% de los desarrolladores con ganancias de productividad medidas >15% y bibliotecas de prompts. | • >75% active users<br>• Productivity metrics showing >15% gain<br>• Shared prompt library repository |
| **L4** | Optimizando | Asistente de codificación IA universal (>95%) con ajuste fino de modelo personalizado y mejora de velocidad medida >30%. | • >95% daily active usage<br>• Custom model fine-tuning config<br>• Measured >30% velocity improvement<br>• Automated suggestion quality tracking |

---

### P1-C1-Q2: Quão efetivamente sua equipe aproveita IA para revisão de código e melhoria de qualidade?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% PRs with AI review`

**Contexto**

- **Qué mide (what):** Measures use of AI in code review processes to catch bugs, suggest improvements, and enforce standards.
- **Por qué importa (why):** AI-assisted code review reduces review time by 40% and catches 20% more defects than manual-only review.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin participación de IA en la revisión de código. Todas las revisiones son revisiones manuales entre pares. | • Manual-only review process<br>• No AI review tools<br>• No automated quality gates |
| **L1** | En Desarrollo | Linting básico y herramientas de análisis estático en CI. Sin sugerencias de revisión impulsadas por IA. | • CI linting configuration<br>• Static analysis tool setup<br>• No AI review bot configured |
| **L2** | Definido | Bot de revisión con IA configurado en 30-60% de los repositorios, entregando sugerencias automatizadas de código. | • AI review bot on 30-60% of repos<br>• PR suggestion examples<br>• Review bot configuration docs |
| **L3** | Gestionado | Revisión con IA integrada en >80% de los repositorios con reglas personalizadas alineadas a los estándares del equipo. | • >80% repo coverage<br>• Custom rule configuration<br>• Measured >25% review cycle reduction |
| **L4** | Optimizando | La IA realiza la primera revisión en todos los PRs, aprobando automáticamente los cambios de bajo riesgo y escalando los críticos. | • 100% PR AI first-pass<br>• Auto-approval policy documented<br>• Risk classification model<br>• >50% cycle time reduction |

---

### P1-C1-Q3: Como sua organização mede e rastreia o impacto das ferramentas de codificação IA na produtividade?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 0.8
- **Professional Edition:** No
- **KPI principal:** `Productivity measurement maturity`

**Contexto**

- **Qué mide (what):** Measures the organization's ability to quantify the value of AI coding tools.
- **Por qué importa (why):** Without measurement, organizations cannot justify AI tool investment or optimize adoption strategies.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin medición del impacto de las herramientas de IA. Sin métricas de productividad de línea base capturadas. | • No DORA metrics<br>• No productivity dashboards<br>• No AI tool usage tracking |
| **L1** | En Desarrollo | Feedback anecdótico de los desarrolladores sobre la utilidad de las herramientas de IA. Sin medición cuantitativa. | • Developer survey results<br>• Informal feedback collection<br>• No quantitative data |
| **L2** | Definido | Métricas DORA básicas rastreadas (frecuencia de despliegue, lead time). Analítica de uso de herramientas de IA disponible. | • DORA metrics dashboard<br>• Monthly usage analytics report<br>• Baseline measurements established |
| **L3** | Gestionado | Métricas integrales de productividad del desarrollador que incluyen medidas específicas de IA: tasa de aceptación, tiempo ahorrado. | • >40% suggestion acceptance rate<br>• >20% time-to-merge improvement<br>• Defect density trend analysis |
| **L4** | Optimizando | Plataforma de inteligencia de productividad en tiempo real que correlaciona el uso de herramientas de IA con resultados de negocio. | • Real-time productivity dashboard<br>• Automated ROI reports<br>• Business outcome correlation analysis<br>• Per-team optimization recommendations |

---

### P1-C1-Q4: Qual nível de capacidades de testes assistidos por IA sua organização emprega?

**Metadatos**

- **Público objetivo:** Desarrollador, qa-test, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% test coverage from AI generation`

**Contexto**

- **Qué mide (what):** Measures use of AI to generate, maintain, and optimize test suites.
- **Por qué importa (why):** AI-generated tests can increase coverage from 40% to 80% in weeks, catching regressions that manual tests miss.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Todas las pruebas escritas manualmente. Cobertura de pruebas inferior al 40% en la mayoría de los proyectos. | • Manual test writing only<br>• <40% average coverage<br>• No AI test generation tools |
| **L1** | En Desarrollo | Uso ocasional de IA para generar esqueletos de pruebas unitarias. La cobertura permanece por debajo del 50%. | • Ad-hoc AI test generation<br>• <50% coverage rate measured<br>• No systematic approach |
| **L2** | Definido | Generación de pruebas con IA integrada en el flujo de desarrollo para 30-50% del código nuevo. Cobertura >60%. | • AI test generation in 30-50% of new code<br>• 60% coverage gates in CI<br>• Test generation guidelines |
| **L3** | Gestionado | La IA genera >70% de las pruebas unitarias con revisión humana. Cobertura >75%. La IA identifica casos extremos. | • >70% AI-generated tests<br>• >75% coverage across projects<br>• Edge case suggestion examples |
| **L4** | Optimizando | Optimización de pruebas impulsada por IA: genera suites de regresión automáticamente, identifica pruebas inestables, optimiza la cobertura. | • >85% coverage rate measured<br>• <5% flaky test rate<br>• Automated regression suite generation<br>• Mutation testing integration |

---

### P1-C1-Q5: Como sua organização governa o código gerado por IA em termos de segurança e conformidade?

**Metadatos**

- **Público objetivo:** Desarrollador, Seguridad, product-owner, qa-test
- **Peso:** 1.1
- **Professional Edition:** No
- **KPI principal:** `AI code governance maturity`

**Contexto**

- **Qué mide (what):** Measures policies and controls around AI-generated code quality, security, and IP compliance.
- **Por qué importa (why):** Without governance, AI-generated code can introduce vulnerabilities, license violations, and compliance risks.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin gobernanza sobre el código generado por IA. No existe ninguna política. Los desarrolladores usan herramientas de IA sin restricciones. | • No AI code policy<br>• No security scanning of AI code<br>• No license compliance checks |
| **L1** | En Desarrollo | Existe una política básica que prohíbe el uso de IA en módulos sensibles a la seguridad. Sin automatización. | • Written AI usage policy<br>• Security-sensitive module list<br>• No automated enforcement |
| **L2** | Definido | El código generado por IA pasa por análisis de seguridad estándar (SAST/DAST). Verificación de cumplimiento de licencias en CI. | • SAST/DAST pipeline includes AI code<br>• License compliance scanning<br>• Policy enforcement in CI |
| **L3** | Gestionado | Puertas de calidad de código dedicadas para IA: escaneo de vulnerabilidades, auditoría de licencias, revisión de calidad de código. | • AI-specific quality gates<br>• Code provenance tracking<br>• <2% security flag rate<br>• Quarterly audit reports |
| **L4** | Optimizando | Gobernanza de código IA en tiempo real: cada sugerencia escaneada antes de mostrarse, licencias bloqueadas y métricas de calidad rastreadas. | • Pre-display content scanning enabled<br>• Auto-rejection of blocked licenses<br>• Zero unreviewed AI code policy<br>• Compliance certification achieved |

---

## P1-C2: Plataforma de Experiência do Desenvolvedor (Plataforma de Experiencia del Desarrollador)

**6 preguntas en esta capability.**

### P1-C2-Q1: Quão maduro é seu portal ou plataforma interna para desenvolvedores?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `Developer portal adoption %`

**Contexto**

- **Qué mide (what):** Measures the maturity of centralized developer portal for service catalog, docs, and self-service.
- **Por qué importa (why):** A mature developer portal reduces onboarding time by 60% and eliminates context-switching between tools.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin portal del desarrollador. Documentación dispersa en wikis, Slack y correo electrónico. | • No centralized portal<br>• Documentation in multiple tools<br>• No service catalog |
| **L1** | En Desarrollo | Wiki básica o espacio en Confluence con algo de documentación. Sin catálogo de servicios ni capacidades de autoservicio. | • Central wiki exists<br>• Some API docs<br>• No service catalog |
| **L2** | Definido | Portal del desarrollador desplegado (Backstage o similar) con catálogo de servicios que cubre >50% de los servicios. Plantillas básicas de documentación. | • >50% services cataloged<br>• Portal deployment docs<br>• Documentation templates published |
| **L3** | Gestionado | El portal del desarrollador cubre >80% de los servicios con scaffolding de autoservicio, documentación de API automatizada y estado de CI/CD integrado. Tiempo de onboarding reducido >40%. | • >80% service coverage<br>• Self-service scaffolding tooling<br>• >40% onboarding time reduction |
| **L4** | Optimizando | Portal del desarrollador potenciado por IA: búsqueda en lenguaje natural en toda la documentación, diagramas de arquitectura autogenerados, detección predictiva de problemas. >95% de satisfacción de los desarrolladores. | • AI-powered search enabled<br>• Auto-generated architecture diagrams<br>• >95% satisfaction score<br>• Predictive issue detection |

---

### P1-C2-Q2: Quão efetivamente suas equipes usam ambientes de desenvolvimento padronizados?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma
- **Peso:** 0.9
- **Professional Edition:** Sí
- **KPI principal:** `Environment setup time (minutes)`

**Contexto**

- **Qué mide (what):** Measures standardization of development environments across teams.
- **Por qué importa (why):** Standardized environments eliminate 'works on my machine' issues and reduce setup time from days to minutes.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Cada desarrollador mantiene su propia configuración de entorno. Sin estandarización. La configuración toma >4 horas para nuevos miembros del equipo. | • No environment standardization<br>• Setup time >4 hours<br>• Manual dependency installation |
| **L1** | En Desarrollo | README con instrucciones de configuración. Algunos equipos usan Docker para desarrollo local. Tiempo de configuración de 1-4 horas. | • README setup guide<br>• Some Docker usage<br>• 1-4 hour setup time |
| **L2** | Definido | Docker Compose o devcontainer para >50% de los proyectos. Tiempo de configuración <30 minutos. Configuraciones compartidas. | • >50% projects with containers<br>• <30 min setup time<br>• Shared dev configs |
| **L3** | Gestionado | Devcontainers estandarizados para >80% de los proyectos. Entornos de desarrollo en la nube disponibles (Codespaces). Tiempo de configuración <10 minutos. | • >80% devcontainer coverage<br>• Cloud dev environment available<br>• <10 min setup time |
| **L4** | Optimizando | Entornos de desarrollo efímeros de un clic con dependencias configuradas por IA. Cero configuración manual. Paridad del entorno con producción garantizada. | • One-click environment creation<br>• Zero manual setup steps<br>• Production parity verification documented<br>• AI dependency configuration |

---

### P1-C2-Q3: Em que medida Plataforma de Experiência do Desenvolvedor (self-service IDP) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma, Arquitecto, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `Self-service catalog coverage`

**Contexto**

- **Qué mide (what):** Internal developer platform (IDP) provides paved paths with self-service provisioning.
- **Por qué importa (why):** IDPs reduce cognitive load and accelerate onboarding by 50-70%.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin self-service idp implementado. Los equipos operan sin esta capacidad. | • No self-service IDP deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de self-service idp con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | self-service IDP adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | self-service IDP estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | self-service IDP está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q4: Em que medida Plataforma de Experiência do Desenvolvedor (golden paths and templates) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services from templates`

**Contexto**

- **Qué mide (what):** Golden-path templates encode opinionated defaults for new services.
- **Por qué importa (why):** Standard templates reduce time-to-first-commit and enforce security baselines.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin golden paths and templates implementado. Los equipos operan sin esta capacidad. | • No golden paths and templates deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de golden paths and templates con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | golden paths and templates adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | golden paths and templates estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | golden paths and templates está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q5: Em que medida Plataforma de Experiência do Desenvolvedor (developer portal) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `Portal MAU (monthly active users)`

**Contexto**

- **Qué mide (what):** A developer portal centralizes docs, APIs, and service catalog.
- **Por qué importa (why):** A single pane of glass reduces context switching and improves discovery.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin developer portal implementado. Los equipos operan sin esta capacidad. | • No developer portal deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de developer portal con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | developer portal adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | developer portal estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | developer portal está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q6: Em que medida Plataforma de Experiência do Desenvolvedor (paved road policy enforcement) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma, Seguridad, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `services on paved road`

**Contexto**

- **Qué mide (what):** Platform policies are codified so teams must opt-out explicitly.
- **Por qué importa (why):** Policy-as-code turns governance into an enabler, not a blocker.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin paved road policy enforcement implementado. Los equipos operan sin esta capacidad. | • No paved road policy enforcement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de paved road policy enforcement con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | paved road policy enforcement adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | paved road policy enforcement estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | paved road policy enforcement está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C3: Gestão do Conhecimento (Gestión del Conocimiento)

**6 preguntas en esta capability.**

### P1-C3-Q1: Quão efetivamente sua organização captura e compartilha conhecimento de desenvolvimento?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `Knowledge retrieval success rate %`

**Contexto**

- **Qué mide (what):** Measures how well development knowledge is captured, organized, and accessible.
- **Por qué importa (why):** Poor knowledge management causes 20% of developer time wasted searching for information or reinventing solutions.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | El conocimiento vive en la cabeza de desarrolladores individuales. Sin cultura de documentación. Alto riesgo de bus-factor. | • No documentation policy<br>• Knowledge in individuals<br>• High bus-factor risk |
| **L1** | En Desarrollo | Existe documentación básica para sistemas críticos. Intercambio de conocimiento mediante reuniones ad-hoc e hilos de Slack. | • Some critical system docs<br>• Ad-hoc knowledge sharing<br>• Slack-based Q&A channel |
| **L2** | Definido | Documentación estructurada en una wiki central. Tech talks o sesiones de intercambio de conocimiento regulares. Registros de decisiones para cambios mayores. | • Central wiki with structure<br>• Regular tech talks<br>• ADR practice established |
| **L3** | Gestionado | Base de conocimiento con búsqueda que cubre >70% de los sistemas. Generación de documentación asistida por IA. Runbooks automatizados para problemas comunes. | • >70% system documentation<br>• AI-assisted doc generation<br>• Automated runbooks published |
| **L4** | Optimizando | Grafo de conocimiento potenciado por IA que vincula código, documentación, incidentes y decisiones. Las consultas en lenguaje natural devuelven respuestas contextuales. Frescura del conocimiento monitoreada automáticamente. | • Knowledge graph implementation<br>• NL query interface<br>• Automated freshness monitoring enabled<br>• Contextual answer system |

---

### P1-C3-Q2: Em que medida Gestão do Conhecimento (semantic code search) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos indexed`

**Contexto**

- **Qué mide (what):** Organization-wide semantic search across repos, docs, and chats.
- **Por qué importa (why):** Semantic search cuts duplicate work by making prior solutions discoverable.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin semantic code search implementado. Los equipos operan sin esta capacidad. | • No semantic code search deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de semantic code search con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | semantic code search adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | semantic code search estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | semantic code search está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q3: Em que medida Gestão do Conhecimento (RAG-based docs assistant) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `queries per developer/month`

**Contexto**

- **Qué mide (what):** LLM-backed assistant answers dev questions from internal knowledge base.
- **Por qué importa (why):** RAG assistants reduce interrupt load on senior engineers.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin rag-based docs assistant implementado. Los equipos operan sin esta capacidad. | • No RAG-based docs assistant deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de rag-based docs assistant con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | RAG-based docs assistant adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | RAG-based docs assistant estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | RAG-based docs assistant está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q4: Em que medida Gestão do Conhecimento (runbook and playbook coverage) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% critical services with runbook`

**Contexto**

- **Qué mide (what):** Automated runbooks capture operational knowledge.
- **Por qué importa (why):** Documented runbooks shorten MTTR and enable on-call rotation.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin runbook and playbook coverage implementado. Los equipos operan sin esta capacidad. | • No runbook and playbook coverage deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de runbook and playbook coverage con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | runbook and playbook coverage adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | runbook and playbook coverage estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | runbook and playbook coverage está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q5: Em que medida Gestão do Conhecimento (ADR (architecture decision records)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with ADRs`

**Contexto**

- **Qué mide (what):** Architecture decisions are captured as ADRs in the repo.
- **Por qué importa (why):** ADRs preserve institutional memory beyond individuals.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin adr (architecture decision records) implementado. Los equipos operan sin esta capacidad. | • No ADR (architecture decision records) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de adr (architecture decision records) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | ADR (architecture decision records) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | ADR (architecture decision records) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | ADR (architecture decision records) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q6: Em que medida Gestão do Conhecimento (learning content & curated paths) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `completions per quarter`

**Contexto**

- **Qué mide (what):** Curated learning paths tied to role and career ladder.
- **Por qué importa (why):** Structured learning reduces ramp time and improves retention.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin learning content & curated paths implementado. Los equipos operan sin esta capacidad. | • No learning content & curated paths deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de learning content & curated paths con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | learning content & curated paths adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | learning content & curated paths estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | learning content & curated paths está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C4: Automação de Revisão de Código (Automatización de Revisión de Código)

**7 preguntas en esta capability.**

### P1-C4-Q1: Em que medida Automação de Revisão de Código (AI reviewer bot on every PR) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% PRs AI-reviewed`

**Contexto**

- **Qué mide (what):** A bot posts AI-generated review comments on every PR.
- **Por qué importa (why):** AI reviewers catch issues before humans look at the code.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin ai reviewer bot on every pr implementado. Los equipos operan sin esta capacidad. | • No AI reviewer bot on every PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de ai reviewer bot on every pr con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | AI reviewer bot on every PR adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | AI reviewer bot on every PR estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | AI reviewer bot on every PR está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q2: Em que medida Automação de Revisão de Código (static linting and style auto-fix) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `lint violations per kLOC`

**Contexto**

- **Qué mide (what):** Linters and formatters run automatically on every commit.
- **Por qué importa (why):** Automated style removes bikeshedding from reviews.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin static linting and style auto-fix implementado. Los equipos operan sin esta capacidad. | • No static linting and style auto-fix deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de static linting and style auto-fix con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | static linting and style auto-fix adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | static linting and style auto-fix estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | static linting and style auto-fix está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q3: Em que medida Automação de Revisão de Código (automated security review) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `critical findings per PR`

**Contexto**

- **Qué mide (what):** SAST comments inline on the PR diff.
- **Por qué importa (why):** Inline findings are fixed 10x faster than backlog items.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin automated security review implementado. Los equipos operan sin esta capacidad. | • No automated security review deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de automated security review con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | automated security review adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | automated security review estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | automated security review está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q4: Em que medida Automação de Revisão de Código (required-reviewer rules) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% PRs meeting review rule`

**Contexto**

- **Qué mide (what):** CODEOWNERS enforces domain-expert review per path.
- **Por qué importa (why):** Right reviewer + right code = better catches.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin required-reviewer rules implementado. Los equipos operan sin esta capacidad. | • No required-reviewer rules deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de required-reviewer rules con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | required-reviewer rules adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | required-reviewer rules estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | required-reviewer rules está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q5: Em que medida Automação de Revisão de Código (review SLA tracking) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median PR cycle time`

**Contexto**

- **Qué mide (what):** PR cycle time is measured and targeted.
- **Por qué importa (why):** Fast review cycles keep developers in flow.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin review sla tracking implementado. Los equipos operan sin esta capacidad. | • No review SLA tracking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de review sla tracking con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | review SLA tracking adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | review SLA tracking estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | review SLA tracking está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q6: Em que medida Automação de Revisão de Código (change size enforcement) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median PR size (LoC)`

**Contexto**

- **Qué mide (what):** Pre-commit hooks encourage small PRs.
- **Por qué importa (why):** Small PRs get better reviews and merge faster.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin change size enforcement implementado. Los equipos operan sin esta capacidad. | • No change size enforcement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de change size enforcement con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | change size enforcement adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | change size enforcement estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | change size enforcement está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q7: Em que medida Automação de Revisão de Código (reviewer load balancing) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `review load balance index`

**Contexto**

- **Qué mide (what):** Reviewer assignment balances load across the team.
- **Por qué importa (why):** Balanced review load prevents burnout of top reviewers.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin reviewer load balancing implementado. Los equipos operan sin esta capacidad. | • No reviewer load balancing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de reviewer load balancing con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | reviewer load balancing adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | reviewer load balancing estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | reviewer load balancing está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C5: Onboarding e Treinamento de Desenvolvedores (Onboarding y Capacitación de Desarrolladores)

**7 preguntas en esta capability.**

### P1-C5-Q1: Em que medida Onboarding e Treinamento de Desenvolvedores (codespaces/dev containers for instant env) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `time-to-first-commit (hours)`

**Contexto**

- **Qué mide (what):** Cloud dev envs are ready in minutes.
- **Por qué importa (why):** Fast env setup unblocks new hires on day one.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin codespaces/dev containers for instant env implementado. Los equipos operan sin esta capacidad. | • No codespaces/dev containers for instant env deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de codespaces/dev containers for instant env con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | codespaces/dev containers for instant env adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | codespaces/dev containers for instant env estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | codespaces/dev containers for instant env está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q2: Em que medida Onboarding e Treinamento de Desenvolvedores (structured onboarding playbook) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% new hires completing onboarding`

**Contexto**

- **Qué mide (what):** A documented 30/60/90-day onboarding plan per role.
- **Por qué importa (why):** Structured onboarding reduces ramp time by 30-50%.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin structured onboarding playbook implementado. Los equipos operan sin esta capacidad. | • No structured onboarding playbook deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de structured onboarding playbook con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | structured onboarding playbook adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | structured onboarding playbook estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | structured onboarding playbook está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q3: Em que medida Onboarding e Treinamento de Desenvolvedores (mentor pairing program) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `mentor:mentee ratio`

**Contexto**

- **Qué mide (what):** Every new hire gets a senior mentor for 90 days.
- **Por qué importa (why):** Mentoring shortens ramp and boosts retention.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin mentor pairing program implementado. Los equipos operan sin esta capacidad. | • No mentor pairing program deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de mentor pairing program con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | mentor pairing program adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | mentor pairing program estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | mentor pairing program está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q4: Em que medida Onboarding e Treinamento de Desenvolvedores (hands-on curriculum & kata) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `katas completed per hire`

**Contexto**

- **Qué mide (what):** Role-specific coding kata produce demonstrable skill.
- **Por qué importa (why):** Deliberate practice builds skill faster than reading.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin hands-on curriculum & kata implementado. Los equipos operan sin esta capacidad. | • No hands-on curriculum & kata deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de hands-on curriculum & kata con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | hands-on curriculum & kata adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | hands-on curriculum & kata estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | hands-on curriculum & kata está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q5: Em que medida Onboarding e Treinamento de Desenvolvedores (shadow on-call rotation) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `new hires who shadowed on-call`

**Contexto**

- **Qué mide (what):** New hires shadow on-call to learn operational context.
- **Por qué importa (why):** Operational context is the fastest way to understand the system.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin shadow on-call rotation implementado. Los equipos operan sin esta capacidad. | • No shadow on-call rotation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de shadow on-call rotation con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | shadow on-call rotation adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | shadow on-call rotation estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | shadow on-call rotation está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q6: Em que medida Onboarding e Treinamento de Desenvolvedores (onboarding feedback loop) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `NPS from new hires`

**Contexto**

- **Qué mide (what):** New hires rate onboarding; results drive improvements.
- **Por qué importa (why):** Feedback loops turn onboarding into a continuously improving product.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin onboarding feedback loop implementado. Los equipos operan sin esta capacidad. | • No onboarding feedback loop deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de onboarding feedback loop con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | onboarding feedback loop adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | onboarding feedback loop estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | onboarding feedback loop está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q7: Em que medida Onboarding e Treinamento de Desenvolvedores (ramp-time measurement) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median ramp-time to first deploy`

**Contexto**

- **Qué mide (what):** Time-to-first-deploy is measured and improved for new hires.
- **Por qué importa (why):** Measuring ramp turns onboarding improvements into ROI.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin ramp-time measurement implementado. Los equipos operan sin esta capacidad. | • No ramp-time measurement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de ramp-time measurement con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | ramp-time measurement adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | ramp-time measurement estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | ramp-time measurement está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C6: Inner Source e Colaboração (Inner Source y Colaboración)

**6 preguntas en esta capability.**

### P1-C6-Q1: Em que medida Inner Source e Colaboração (internal repos with open contribution) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos open to all devs`

**Contexto**

- **Qué mide (what):** Repos inside the org welcome PRs from other teams.
- **Por qué importa (why):** Inner source breaks silos and increases reuse.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin internal repos with open contribution implementado. Los equipos operan sin esta capacidad. | • No internal repos with open contribution deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de internal repos with open contribution con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | internal repos with open contribution adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | internal repos with open contribution estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | internal repos with open contribution está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q2: Em que medida Inner Source e Colaboração (CONTRIBUTING.md standards) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos with CONTRIBUTING`

**Contexto**

- **Qué mide (what):** Every repo documents how to contribute and review.
- **Por qué importa (why):** Clear contribution norms lower friction for cross-team work.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin contributing.md standards implementado. Los equipos operan sin esta capacidad. | • No CONTRIBUTING.md standards deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de contributing.md standards con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | CONTRIBUTING.md standards adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | CONTRIBUTING.md standards estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | CONTRIBUTING.md standards está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q3: Em que medida Inner Source e Colaboração (inner-source discovery portal) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `cross-team PRs per month`

**Contexto**

- **Qué mide (what):** A portal indexes inner-source projects seeking contributions.
- **Por qué importa (why):** Discovery drives participation.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin inner-source discovery portal implementado. Los equipos operan sin esta capacidad. | • No inner-source discovery portal deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de inner-source discovery portal con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | inner-source discovery portal adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | inner-source discovery portal estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | inner-source discovery portal está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q4: Em que medida Inner Source e Colaboração (good-first-issue labeling) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `GFI issues closed per month`

**Contexto**

- **Qué mide (what):** Starter issues help newcomers contribute confidently.
- **Por qué importa (why):** Labeling lowers the bar for first-time contributors.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin good-first-issue labeling implementado. Los equipos operan sin esta capacidad. | • No good-first-issue labeling deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de good-first-issue labeling con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | good-first-issue labeling adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | good-first-issue labeling estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | good-first-issue labeling está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q5: Em que medida Inner Source e Colaboração (cross-team design reviews) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `reviews per quarter`

**Contexto**

- **Qué mide (what):** Design docs are reviewed by multiple teams.
- **Por qué importa (why):** Cross-team review catches assumptions and shares patterns.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin cross-team design reviews implementado. Los equipos operan sin esta capacidad. | • No cross-team design reviews deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de cross-team design reviews con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | cross-team design reviews adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | cross-team design reviews estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | cross-team design reviews está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q6: Em que medida Inner Source e Colaboração (community of practice) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `CoP active members`

**Contexto**

- **Qué mide (what):** Guilds and CoPs build horizontal expertise.
- **Por qué importa (why):** CoPs accelerate learning and de-risk hiring gaps.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin community of practice implementado. Los equipos operan sin esta capacidad. | • No community of practice deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de community of practice con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | community of practice adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | community of practice estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | community of practice está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C7: Automação de Documentação (Automatización de Documentación)

**5 preguntas en esta capability.**

### P1-C7-Q1: Em que medida Automação de Documentação (docs-as-code in Git) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with docs in repo`

**Contexto**

- **Qué mide (what):** Docs live with code and are reviewed in PRs.
- **Por qué importa (why):** Docs-as-code prevents docs from rotting away from source.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin docs-as-code in git implementado. Los equipos operan sin esta capacidad. | • No docs-as-code in Git deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de docs-as-code in git con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | docs-as-code in Git adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | docs-as-code in Git estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | docs-as-code in Git está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q2: Em que medida Automação de Documentação (auto-generated API reference) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% APIs with generated docs`

**Contexto**

- **Qué mide (what):** API reference is generated from OpenAPI or source.
- **Por qué importa (why):** Generated docs are always up to date.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin auto-generated api reference implementado. Los equipos operan sin esta capacidad. | • No auto-generated API reference deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de auto-generated api reference con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | auto-generated API reference adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | auto-generated API reference estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | auto-generated API reference está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q3: Em que medida Automação de Documentação (AI-assisted doc drafting) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% PRs with AI doc suggestions`

**Contexto**

- **Qué mide (what):** AI suggests README and doc updates from code diffs.
- **Por qué importa (why):** AI drafts raise the floor on documentation quality.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin ai-assisted doc drafting implementado. Los equipos operan sin esta capacidad. | • No AI-assisted doc drafting deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de ai-assisted doc drafting con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | AI-assisted doc drafting adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | AI-assisted doc drafting estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | AI-assisted doc drafting está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q4: Em que medida Automação de Documentação (doc quality linting) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `broken-link count`

**Contexto**

- **Qué mide (what):** Link checks and style linters run in CI.
- **Por qué importa (why):** Automated checks keep docs trustworthy.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin doc quality linting implementado. Los equipos operan sin esta capacidad. | • No doc quality linting deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de doc quality linting con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | doc quality linting adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | doc quality linting estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | doc quality linting está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q5: Em que medida Automação de Documentação (docs analytics) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `top unanswered queries`

**Contexto**

- **Qué mide (what):** Search analytics reveal what users cannot find.
- **Por qué importa (why):** Analytics turn docs into a data-driven product.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin docs analytics implementado. Los equipos operan sin esta capacidad. | • No docs analytics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de docs analytics con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | docs analytics adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | docs analytics estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | docs analytics está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C8: Medição de Produtividade do Desenvolvedor (Medición de Productividad del Desarrollador)

**6 preguntas en esta capability.**

### P1-C8-Q1: Em que medida Medição de Produtividade do Desenvolvedor (DORA four key metrics) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `deploys/day, lead time, CFR, MTTR`

**Contexto**

- **Qué mide (what):** Deployment frequency, lead time, change fail rate, MTTR are tracked.
- **Por qué importa (why):** DORA metrics correlate with business outcomes.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin dora four key metrics implementado. Los equipos operan sin esta capacidad. | • No DORA four key metrics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de dora four key metrics con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | DORA four key metrics adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | DORA four key metrics estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | DORA four key metrics está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q2: Em que medida Medição de Produtividade do Desenvolvedor (developer experience surveys) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `DX survey NPS`

**Contexto**

- **Qué mide (what):** Quarterly surveys measure developer satisfaction.
- **Por qué importa (why):** DX surveys surface friction that metrics miss.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin developer experience surveys implementado. Los equipos operan sin esta capacidad. | • No developer experience surveys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de developer experience surveys con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | developer experience surveys adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | developer experience surveys estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | developer experience surveys está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q3: Em que medida Medição de Produtividade do Desenvolvedor (build/test feedback loop time) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `p95 CI duration`

**Contexto**

- **Qué mide (what):** CI provides signal within 10 minutes for typical PRs.
- **Por qué importa (why):** Fast feedback keeps developers in flow.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin build/test feedback loop time implementado. Los equipos operan sin esta capacidad. | • No build/test feedback loop time deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de build/test feedback loop time con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | build/test feedback loop time adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | build/test feedback loop time estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | build/test feedback loop time está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q4: Em que medida Medição de Produtividade do Desenvolvedor (SPACE framework adoption) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `SPACE dimensions tracked`

**Contexto**

- **Qué mide (what):** Teams track Satisfaction, Performance, Activity, Communication, Efficiency.
- **Por qué importa (why):** SPACE balances quantitative and qualitative signals.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin space framework adoption implementado. Los equipos operan sin esta capacidad. | • No SPACE framework adoption deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de space framework adoption con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SPACE framework adoption adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | SPACE framework adoption estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | SPACE framework adoption está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q5: Em que medida Medição de Produtividade do Desenvolvedor (flow vs friction dashboards) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% teams viewing dashboard monthly`

**Contexto**

- **Qué mide (what):** Leaders and teams see productivity data side by side.
- **Por qué importa (why):** Shared data aligns improvements across teams.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin flow vs friction dashboards implementado. Los equipos operan sin esta capacidad. | • No flow vs friction dashboards deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de flow vs friction dashboards con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | flow vs friction dashboards adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | flow vs friction dashboards estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | flow vs friction dashboards está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q6: Em que medida Medição de Produtividade do Desenvolvedor (quarterly productivity OKRs) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** engineering-leader, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% teams hitting DX OKRs`

**Contexto**

- **Qué mide (what):** DX improvements are tracked as OKRs.
- **Por qué importa (why):** OKRs make productivity a first-class investment.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin quarterly productivity okrs implementado. Los equipos operan sin esta capacidad. | • No quarterly productivity OKRs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de quarterly productivity okrs con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | quarterly productivity OKRs adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | quarterly productivity OKRs estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | quarterly productivity OKRs está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C9: Automação de Ambientes e Espaços de Trabalho (Automatización de Entornos y Espacios de Trabajo)

**5 preguntas en esta capability.**

### P1-C9-Q1: Em que medida Automação de Ambientes e Espaços de Trabalho (reproducible local envs (devcontainers)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos with devcontainer`

**Contexto**

- **Qué mide (what):** Every repo ships a devcontainer or Nix shell.
- **Por qué importa (why):** Reproducible envs eliminate 'works on my machine' failures.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin reproducible local envs (devcontainers) implementado. Los equipos operan sin esta capacidad. | • No reproducible local envs (devcontainers) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de reproducible local envs (devcontainers) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | reproducible local envs (devcontainers) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | reproducible local envs (devcontainers) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | reproducible local envs (devcontainers) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q2: Em que medida Automação de Ambientes e Espaços de Trabalho (cloud workspaces (Codespaces/Gitpod)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% devs using cloud workspace`

**Contexto**

- **Qué mide (what):** Cloud workspaces are the default dev env.
- **Por qué importa (why):** Cloud workspaces make env setup instant and consistent.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin cloud workspaces (codespaces/gitpod) implementado. Los equipos operan sin esta capacidad. | • No cloud workspaces (Codespaces/Gitpod) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de cloud workspaces (codespaces/gitpod) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | cloud workspaces (Codespaces/Gitpod) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | cloud workspaces (Codespaces/Gitpod) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | cloud workspaces (Codespaces/Gitpod) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q3: Em que medida Automação de Ambientes e Espaços de Trabalho (tool and SDK version pinning) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `tools pinned per repo`

**Contexto**

- **Qué mide (what):** Language and tool versions are pinned and lockfiles committed.
- **Por qué importa (why):** Pinned versions keep builds reproducible across machines.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin tool and sdk version pinning implementado. Los equipos operan sin esta capacidad. | • No tool and SDK version pinning deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de tool and sdk version pinning con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | tool and SDK version pinning adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | tool and SDK version pinning estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | tool and SDK version pinning está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q4: Em que medida Automação de Ambientes e Espaços de Trabalho (on-demand test data) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `time to get fresh test data`

**Contexto**

- **Qué mide (what):** Developers can reset or provision realistic test data on demand.
- **Por qué importa (why):** Fresh data unblocks testing and debugging.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin on-demand test data implementado. Los equipos operan sin esta capacidad. | • No on-demand test data deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de on-demand test data con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | on-demand test data adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | on-demand test data estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | on-demand test data está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q5: Em que medida Automação de Ambientes e Espaços de Trabalho (workspace telemetry & health) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Desarrollador, Ingeniero de Plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% workspaces healthy`

**Contexto**

- **Qué mide (what):** Workspace telemetry reveals setup failures and tool crashes.
- **Por qué importa (why):** Telemetry lets platform teams fix friction proactively.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin workspace telemetry & health implementado. Los equipos operan sin esta capacidad. | • No workspace telemetry & health deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de workspace telemetry & health con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | workspace telemetry & health adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | workspace telemetry & health estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | workspace telemetry & health está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## Cómo se puntúa esta sección

- Cada pregunta recibe un valor numérico del nivel seleccionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- La puntuación de la capacidad es el promedio ponderado de las preguntas (peso default = 1.0; las preguntas con peso 1.5 o 2.0 cuentan más).
- La puntuación del pilar **P1** es el promedio de las 9 capacidades.
- El resultado se muestra en escala 0–4 y se convierte a % de madurez (nivel / 4 × 100).

## Glosario rápido

- **Pillar:** dimensión estratégica de madurez.
- **Capability:** subdominio funcional dentro de un pilar.
- **Question:** ítem de evaluación concreto, ID estándar `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0–L4):** punto en la escala Likert de madurez.
- **KPI:** indicador clave que valida objetivamente el nivel declarado.
- **Evidence:** prueba cualitativa (texto) o cuantitativa (anexo) que sustenta la respuesta.
