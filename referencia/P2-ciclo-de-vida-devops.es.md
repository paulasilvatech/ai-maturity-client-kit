# AI Maturity Assessment, Pilar P2: Ciclo de Vida DevOps

> Mide la madurez de pipelines, infraestructura como código, observabilidad, DevSecOps, releases, pruebas, incidentes y seguridad de la cadena de suministro.

> [!IMPORTANT]
> Edición localizada runtime-safe: etiquetas estructurales en Español y todos los IDs preservados.
> El wording canónico de las preguntas (el texto de cada encabezado `P2-Cx-Qy`) se conserva en Portugués, byte-idéntico al banco de preguntas de Microsoft Forms, para mantener paridad estricta de scoring y auditoría con el workbook.

## Visión general

- **Pilar:** `P2`, Ciclo de Vida DevOps
- **Capacidades (capabilities):** 10
- **Preguntas totales:** 59
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

## Capacidades del pilar P2

- **P2-C1**: Inteligência de Pipeline CI/CD (Inteligencia de Pipeline CI/CD), 6 preguntas
- **P2-C2**: Infraestrutura como Código (Infraestructura como Código), 6 preguntas
- **P2-C3**: Observabilidade e Monitoramento (Observabilidad y Monitoreo), 6 preguntas
- **P2-C4**: Integração de Segurança (DevSecOps) (Integración de Seguridad), 6 preguntas
- **P2-C5**: Estratégias de Release e Implantação (Estrategias de Release y Despliegue), 6 preguntas
- **P2-C6**: Automação de Testes (Automatización de Pruebas), 7 preguntas
- **P2-C7**: Gestão de Incidentes e SRE (Gestión de Incidentes y SRE), 7 preguntas
- **P2-C8**: Gestão de Artefatos e Pacotes (Gestión de Artefactos y Paquetes), 5 preguntas
- **P2-C9**: Gestão de Mudanças e GitOps (Gestión de Cambios y GitOps), 5 preguntas
- **P2-C10**: Segurança de Dependências e Cadeia de Suprimentos (Seguridad de Dependencias y Cadena de Suministro), 5 preguntas

---

## P2-C1: Inteligência de Pipeline CI/CD (Inteligencia de Pipeline CI/CD)

**6 preguntas en esta capability.**

### P2-C1-Q1: Quão maduro é seu pipeline CI/CD em termos de automação e integração de IA?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `Deployment frequency per week`

**Contexto**

- **Qué mide (what):** Measures the automation level and intelligence of CI/CD pipelines.
- **Por qué importa (why):** Mature CI/CD pipelines enable teams to deploy 200x more frequently with 3x lower change failure rate (DORA research).

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Builds y despliegues manuales. Sin pipeline CI/CD. Los despliegues ocurren semanalmente o con menor frecuencia. | • No CI/CD pipeline<br>• Manual build process<br>• Weekly or less deployments |
| **L1** | En Desarrollo | Pipeline CI básico con builds automatizados y pruebas unitarias. Proceso de despliegue manual. Frecuencia de despliegue: semanal. | • CI pipeline configured<br>• Automated unit tests<br>• Manual deployments weekly |
| **L2** | Definido | Pipeline CI/CD completo con pruebas automatizadas, despliegue a staging y promoción manual a producción. Frecuencia de despliegue: diaria. | • Automated staging deployment<br>• Manual prod promotion<br>• Daily production deployments cadence |
| **L3** | Gestionado | CI/CD inteligente: suites de pruebas con auto-escalado, selección inteligente de pruebas (ejecuta solo las pruebas afectadas), despliegues canary. Múltiples despliegues por día. | • Smart test selection<br>• Canary deployment config<br>• Multiple daily deployments<br>• Test impact analysis |
| **L4** | Optimizando | Pipeline optimizado con IA: predicción de fallas de build, auto-remediación de pruebas flaky, análisis canary impulsado por ML, despliegues self-healing. | • Predictive failure model<br>• Automated remediation scripts deployed<br>• ML canary analysis<br>• Self-healing deployment docs |

---

### P2-C1-Q2: Em que medida Inteligência de Pipeline CI/CD (pipeline-as-code everywhere) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Seguridad, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% pipelines as code`

**Contexto**

- **Qué mide (what):** All pipelines live next to code as versioned YAML/HCL.
- **Por qué importa (why):** Pipeline-as-code is auditable, reviewable, and reproducible.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin pipeline-as-code everywhere implementado. Los equipos operan sin esta capacidad. | • No pipeline-as-code everywhere deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de pipeline-as-code everywhere con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | pipeline-as-code everywhere adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | pipeline-as-code everywhere estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | pipeline-as-code everywhere está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q3: Em que medida Inteligência de Pipeline CI/CD (build caching and artifact reuse) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% cache hit ratio`

**Contexto**

- **Qué mide (what):** Remote build caches and content-addressed artifacts reduce build time.
- **Por qué importa (why):** Caching cuts CI time by 40-70% and reduces cloud spend.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin build caching and artifact reuse implementado. Los equipos operan sin esta capacidad. | • No build caching and artifact reuse deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de build caching and artifact reuse con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | build caching and artifact reuse adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | build caching and artifact reuse estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | build caching and artifact reuse está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q4: Em que medida Inteligência de Pipeline CI/CD (trunk-based development) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `branches >7 days old`

**Contexto**

- **Qué mide (what):** Short-lived branches merged to trunk multiple times a day.
- **Por qué importa (why):** Trunk-based dev reduces merge hell and enables continuous delivery.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin trunk-based development implementado. Los equipos operan sin esta capacidad. | • No trunk-based development deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de trunk-based development con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | trunk-based development adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | trunk-based development estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | trunk-based development está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q5: Em que medida Inteligência de Pipeline CI/CD (deployment frequency) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `deploys per day`

**Contexto**

- **Qué mide (what):** Elite DORA teams deploy many times per day to production.
- **Por qué importa (why):** High deploy frequency correlates with low change fail rate.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin deployment frequency implementado. Los equipos operan sin esta capacidad. | • No deployment frequency deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de deployment frequency con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | deployment frequency adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | deployment frequency estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | deployment frequency está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q6: Em que medida Inteligência de Pipeline CI/CD (feature flags for progressive delivery) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `flags used per release`

**Contexto**

- **Qué mide (what):** Feature flags decouple deployment from release.
- **Por qué importa (why):** Flags enable dark launches, canary rollouts, and fast rollback.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin feature flags for progressive delivery implementado. Los equipos operan sin esta capacidad. | • No feature flags for progressive delivery deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de feature flags for progressive delivery con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | feature flags for progressive delivery adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | feature flags for progressive delivery estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | feature flags for progressive delivery está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C2: Infraestrutura como Código (Infraestructura como Código)

**6 preguntas en esta capability.**

### P2-C2-Q1: Qual porcentagem de sua infraestrutura é gerenciada por código?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Seguridad, qa-test
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `% infrastructure as code`

**Contexto**

- **Qué mide (what):** Measures the extent to which infrastructure provisioning and management is codified and version-controlled.
- **Por qué importa (why):** IaC reduces provisioning errors by 90% and enables infrastructure changes to be reviewed, tested, and audited like application code.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Toda la infraestructura se aprovisiona manualmente vía consola cloud o comandos CLI. Sin control de versiones para la infraestructura. | • Manual provisioning only<br>• No IaC files in repos<br>• Console-based management workflow |
| **L1** | En Desarrollo | Parte de la infraestructura definida en código (<30%). Mezcla de aprovisionamiento manual y automatizado. Scripts sin control de versiones consistente. | • <30% IaC coverage<br>• Mixed manual and automated processes<br>• Inconsistent version control |
| **L2** | Definido | 50-75% de la infraestructura definida en código. Módulos IaC para patrones comunes. Revisión basada en PR para cambios de infraestructura. | • 50-75% IaC coverage<br>• Reusable IaC modules<br>• PR-based infra review |
| **L3** | Gestionado | >90% de la infraestructura como código. Detección de drift habilitada. Aplicación de policy-as-code. Aprovisionamiento self-service vía plantillas. | • >90% IaC coverage<br>• Drift detection reports<br>• Policy-as-code rules enforced<br>• Self-service templates published |
| **L4** | Optimizando | 100% IaC con recomendaciones de infraestructura generadas por IA. Auto-remediación de drift. Sugerencias de optimización de costos. Escalado predictivo. | • 100% IaC coverage<br>• AI infra recommendations<br>• Automated drift remediation enabled<br>• Predictive scaling config |

---

### P2-C2-Q2: Em que medida Infraestrutura como Código (Terraform/Bicep-based IaC) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% infra as code`

**Contexto**

- **Qué mide (what):** All long-lived infra is declared as code.
- **Por qué importa (why):** IaC eliminates snowflake servers and enables reproducible environments.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin terraform/bicep-based iac implementado. Los equipos operan sin esta capacidad. | • No Terraform/Bicep-based IaC deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de terraform/bicep-based iac con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | Terraform/Bicep-based IaC adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | Terraform/Bicep-based IaC estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | Terraform/Bicep-based IaC está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q3: Em que medida Infraestrutura como Código (module and pattern library) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% resources via modules`

**Contexto**

- **Qué mide (what):** A shared module library encodes opinionated security and networking.
- **Por qué importa (why):** Modules enforce standards and reduce per-team cognitive load.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin module and pattern library implementado. Los equipos operan sin esta capacidad. | • No module and pattern library deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de module and pattern library con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | module and pattern library adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | module and pattern library estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | module and pattern library está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q4: Em que medida Infraestrutura como Código (GitOps for config drift) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% envs drift-detected`

**Contexto**

- **Qué mide (what):** GitOps controllers reconcile cluster and cloud state to Git.
- **Por qué importa (why):** GitOps eliminates drift and makes Git the single source of truth.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin gitops for config drift implementado. Los equipos operan sin esta capacidad. | • No GitOps for config drift deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de gitops for config drift con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | GitOps for config drift adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | GitOps for config drift estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | GitOps for config drift está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q5: Em que medida Infraestrutura como Código (policy-as-code (OPA/Conftest)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Seguridad, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `policies enforced in PR`

**Contexto**

- **Qué mide (what):** Policies are evaluated on IaC changes before merge.
- **Por qué importa (why):** Policy-as-code shifts governance left and scales security review.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin policy-as-code (opa/conftest) implementado. Los equipos operan sin esta capacidad. | • No policy-as-code (OPA/Conftest) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de policy-as-code (opa/conftest) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | policy-as-code (OPA/Conftest) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | policy-as-code (OPA/Conftest) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | policy-as-code (OPA/Conftest) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q6: Em que medida Infraestrutura como Código (ephemeral environment per PR) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `PR envs spun up`

**Contexto**

- **Qué mide (what):** Every PR gets an ephemeral environment for integration testing.
- **Por qué importa (why):** Ephemeral envs find bugs earlier and speed up review.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin ephemeral environment per pr implementado. Los equipos operan sin esta capacidad. | • No ephemeral environment per PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de ephemeral environment per pr con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | ephemeral environment per PR adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | ephemeral environment per PR estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | ephemeral environment per PR está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C3: Observabilidade e Monitoramento (Observabilidad y Monitoreo)

**6 preguntas en esta capability.**

### P2-C3-Q1: Quão abrangente é sua stack de observabilidade (logs, métricas, traces)?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** Sí
- **KPI principal:** `MTTR in minutes`

**Contexto**

- **Qué mide (what):** Measures the maturity of the observability stack including logging, metrics, and distributed tracing.
- **Por qué importa (why):** Comprehensive observability reduces MTTR from hours to minutes and enables proactive issue detection.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Logging mínimo. Sin monitoreo centralizado. Los problemas se descubren cuando los usuarios los reportan. | • No centralized logging<br>• No monitoring dashboards<br>• User-reported issues only |
| **L1** | En Desarrollo | Logging centralizado (ELK/CloudWatch). Monitoreo básico de uptime. MTTR >60 minutos. | • Centralized log platform<br>• Basic uptime checks<br>• MTTR >60 minutes |
| **L2** | Definido | Logging estructurado, métricas de aplicación (Prometheus/Datadog), alertas básicas. MTTR 30-60 minutos. | • Structured JSON logging<br>• Application metrics dashboard<br>• MTTR 30-60 minutes |
| **L3** | Gestionado | Observabilidad completa: distributed tracing, logs-métricas-traces correlacionados, alertas basadas en SLO. MTTR <15 minutos. | • Distributed tracing enabled<br>• Correlated observability stack deployed<br>• SLO-based alerts configured<br>• MTTR <15 minutes |
| **L4** | Optimizando | Observabilidad impulsada por IA: detección de anomalías, alertas predictivas, auto-correlación de incidentes, remediación sugerida. MTTR <5 minutos. | • AI anomaly detection<br>• Predictive alerting enabled<br>• Automated incident correlation enabled<br>• MTTR <5 minutes |

---

### P2-C3-Q2: Em que medida Observabilidade e Monitoramento (structured logging w/ correlation IDs) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services emitting structured logs`

**Contexto**

- **Qué mide (what):** All logs follow a schema and carry trace/correlation IDs.
- **Por qué importa (why):** Structured logs are searchable, aggregatable, and machine-readable.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin structured logging w/ correlation ids implementado. Los equipos operan sin esta capacidad. | • No structured logging w/ correlation IDs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de structured logging w/ correlation ids con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | structured logging w/ correlation IDs adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | structured logging w/ correlation IDs estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | structured logging w/ correlation IDs está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q3: Em que medida Observabilidade e Monitoramento (distributed tracing (OpenTelemetry)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services instrumented`

**Contexto**

- **Qué mide (what):** OTEL SDKs emit traces across service boundaries.
- **Por qué importa (why):** Distributed tracing reveals latency contributors across microservices.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin distributed tracing (opentelemetry) implementado. Los equipos operan sin esta capacidad. | • No distributed tracing (OpenTelemetry) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de distributed tracing (opentelemetry) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | distributed tracing (OpenTelemetry) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | distributed tracing (OpenTelemetry) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | distributed tracing (OpenTelemetry) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q4: Em que medida Observabilidade e Monitoramento (SLOs and error budgets) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with SLOs`

**Contexto**

- **Qué mide (what):** Service-level objectives with error budgets drive reliability decisions.
- **Por qué importa (why):** SLOs align engineering priorities with user experience.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin slos and error budgets implementado. Los equipos operan sin esta capacidad. | • No SLOs and error budgets deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de slos and error budgets con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SLOs and error budgets adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | SLOs and error budgets estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | SLOs and error budgets está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q5: Em que medida Observabilidade e Monitoramento (synthetic monitoring) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `journeys monitored`

**Contexto**

- **Qué mide (what):** Synthetic probes exercise critical user journeys continuously.
- **Por qué importa (why):** Synthetics catch regressions before users do.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin synthetic monitoring implementado. Los equipos operan sin esta capacidad. | • No synthetic monitoring deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de synthetic monitoring con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | synthetic monitoring adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | synthetic monitoring estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | synthetic monitoring está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q6: Em que medida Observabilidade e Monitoramento (anomaly detection with ML) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `alerts auto-triaged`

**Contexto**

- **Qué mide (what):** ML models detect anomalies and suppress noise.
- **Por qué importa (why):** ML-based detection reduces alert fatigue and speeds response.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin anomaly detection with ml implementado. Los equipos operan sin esta capacidad. | • No anomaly detection with ML deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de anomaly detection with ml con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | anomaly detection with ML adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | anomaly detection with ML estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | anomaly detection with ML está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C4: Integração de Segurança (DevSecOps) (Integración de Seguridad)

**6 preguntas en esta capability.**

### P2-C4-Q1: Quão integrada está a segurança no seu pipeline de desenvolvimento e implantação?

**Metadatos**

- **Público objetivo:** Seguridad, devops, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% vulnerabilities caught pre-prod`

**Contexto**

- **Qué mide (what):** Measures the integration of security practices into the development lifecycle (shift-left security).
- **Por qué importa (why):** Fixing vulnerabilities in production costs 30x more than catching them in development. DevSecOps reduces security incidents by 50%.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | La seguridad se revisa solo antes del release. Sin escaneo automatizado. Vulnerabilidades encontradas en producción. | • No automated security scanning<br>• Pre-release only reviews<br>• Production vulnerability incidents |
| **L1** | En Desarrollo | Escaneo básico de dependencias en CI (Dependabot/Snyk). Revisión de seguridad manual para funcionalidades críticas. | • Dependency scanning configured<br>• Manual security reviews<br>• No SAST or DAST scanning |
| **L2** | Definido | SAST y escaneo de dependencias en el pipeline CI. Requisitos de seguridad en la definition of done. >50% de vulnerabilidades detectadas antes de producción. | • SAST in CI pipeline<br>• Security in DoD<br>• >50% pre-prod catch rate |
| **L3** | Gestionado | DevSecOps completo: SAST, DAST, SCA, escaneo de contenedores, detección de secretos. Gates de seguridad que bloquean el despliegue. >80% de tasa de detección pre-producción. | • SAST, DAST, SCA, and container scanning<br>• Secret detection enabled<br>• >80% pre-prod catch rate |
| **L4** | Optimizando | Seguridad impulsada por IA: modelado de amenazas automatizado, detección predictiva de vulnerabilidades, auto-parcheo de CVEs conocidos, protección en runtime. >95% de tasa de detección pre-producción. | • Automated threat modeling<br>• Predictive vulnerability detection<br>• Automated patching pipeline enabled<br>• >95% pre-prod catch rate |

---

### P2-C4-Q2: Em que medida Integração de Segurança (DevSecOps) (SAST in every pipeline) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos with SAST`

**Contexto**

- **Qué mide (what):** Static analysis scans every PR for vulnerabilities.
- **Por qué importa (why):** SAST finds bugs cheaply at authoring time.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin sast in every pipeline implementado. Los equipos operan sin esta capacidad. | • No SAST in every pipeline deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de sast in every pipeline con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SAST in every pipeline adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | SAST in every pipeline estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | SAST in every pipeline está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q3: Em que medida Integração de Segurança (DevSecOps) (SCA and dependency review) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos with SCA`

**Contexto**

- **Qué mide (what):** Software composition analysis flags vulnerable dependencies.
- **Por qué importa (why):** Known-vuln dependencies are a top attack vector.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin sca and dependency review implementado. Los equipos operan sin esta capacidad. | • No SCA and dependency review deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de sca and dependency review con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SCA and dependency review adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | SCA and dependency review estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | SCA and dependency review está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q4: Em que medida Integração de Segurança (DevSecOps) (secret scanning and push protection) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `secrets blocked per month`

**Contexto**

- **Qué mide (what):** Secrets are detected pre-commit and blocked from push.
- **Por qué importa (why):** Leaked secrets are the #1 source of breach in cloud environments.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin secret scanning and push protection implementado. Los equipos operan sin esta capacidad. | • No secret scanning and push protection deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de secret scanning and push protection con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | secret scanning and push protection adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | secret scanning and push protection estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | secret scanning and push protection está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q5: Em que medida Integração de Segurança (DevSecOps) (DAST and API security testing) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops, qa-test
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% APIs DAST-tested`

**Contexto**

- **Qué mide (what):** Dynamic testing exercises the running app for runtime vulns.
- **Por qué importa (why):** DAST catches issues SAST cannot (auth, logic, configuration).

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin dast and api security testing implementado. Los equipos operan sin esta capacidad. | • No DAST and API security testing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de dast and api security testing con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | DAST and API security testing adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | DAST and API security testing estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | DAST and API security testing está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q6: Em que medida Integração de Segurança (DevSecOps) (security champions program) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `champions per 20 devs`

**Contexto**

- **Qué mide (what):** Every team has a security champion trained and resourced.
- **Por qué importa (why):** Champions scale security expertise into every team.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin security champions program implementado. Los equipos operan sin esta capacidad. | • No security champions program deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de security champions program con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | security champions program adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | security champions program estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | security champions program está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C5: Estratégias de Release e Implantação (Estrategias de Release y Despliegue)

**6 preguntas en esta capability.**

### P2-C5-Q1: Em que medida Estratégias de Release e Implantação (blue/green or canary deploys) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with canary`

**Contexto**

- **Qué mide (what):** Canary or blue/green deploys reduce blast radius.
- **Por qué importa (why):** Progressive rollout catches issues before full exposure.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin blue/green or canary deploys implementado. Los equipos operan sin esta capacidad. | • No blue/green or canary deploys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de blue/green or canary deploys con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | blue/green or canary deploys adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | blue/green or canary deploys estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | blue/green or canary deploys está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q2: Em que medida Estratégias de Release e Implantação (automated rollback) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median rollback time`

**Contexto**

- **Qué mide (what):** SLO breach or error spike triggers automatic rollback.
- **Por qué importa (why):** Automated rollback limits user impact when deploys go wrong.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin automated rollback implementado. Los equipos operan sin esta capacidad. | • No automated rollback deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de automated rollback con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | automated rollback adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | automated rollback estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | automated rollback está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q3: Em que medida Estratégias de Release e Implantação (feature flag platform) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Arquitecto
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `flags in active use`

**Contexto**

- **Qué mide (what):** A flag platform supports progressive exposure and experiments.
- **Por qué importa (why):** Flags decouple deploy from release.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin feature flag platform implementado. Los equipos operan sin esta capacidad. | • No feature flag platform deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de feature flag platform con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | feature flag platform adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | feature flag platform estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | feature flag platform está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q4: Em que medida Estratégias de Release e Implantação (release coordination via ChatOps) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% releases using ChatOps`

**Contexto**

- **Qué mide (what):** Releases are coordinated through a chat bot with approvals.
- **Por qué importa (why):** ChatOps creates an audit trail and reduces handoff errors.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin release coordination via chatops implementado. Los equipos operan sin esta capacidad. | • No release coordination via ChatOps deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de release coordination via chatops con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | release coordination via ChatOps adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | release coordination via ChatOps estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | release coordination via ChatOps está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q5: Em que medida Estratégias de Release e Implantação (progressive delivery across regions) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `regions rolled out per release`

**Contexto**

- **Qué mide (what):** Releases ripple across regions with automated health checks.
- **Por qué importa (why):** Multi-region rollout contains regional failures.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin progressive delivery across regions implementado. Los equipos operan sin esta capacidad. | • No progressive delivery across regions deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de progressive delivery across regions con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | progressive delivery across regions adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | progressive delivery across regions estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | progressive delivery across regions está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q6: Em que medida Estratégias de Release e Implantação (release metrics dashboard) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% releases meeting SLO`

**Contexto**

- **Qué mide (what):** Deployment success and SLO impact are tracked per release.
- **Por qué importa (why):** Data-driven release retros drive continuous improvement.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin release metrics dashboard implementado. Los equipos operan sin esta capacidad. | • No release metrics dashboard deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de release metrics dashboard con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | release metrics dashboard adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | release metrics dashboard estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | release metrics dashboard está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C6: Automação de Testes (Automatización de Pruebas)

**7 preguntas en esta capability.**

### P2-C6-Q1: Em que medida Automação de Testes (unit test coverage targets) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos >80% coverage`

**Contexto**

- **Qué mide (what):** Every repo has a measurable coverage target.
- **Por qué importa (why):** Coverage is a useful proxy when combined with mutation testing.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin unit test coverage targets implementado. Los equipos operan sin esta capacidad. | • No unit test coverage targets deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de unit test coverage targets con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | unit test coverage targets adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | unit test coverage targets estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | unit test coverage targets está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q2: Em que medida Automação de Testes (integration test suites) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `integration tests in CI`

**Contexto**

- **Qué mide (what):** Integration tests exercise real service boundaries.
- **Por qué importa (why):** Integration tests catch wiring bugs that units cannot.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin integration test suites implementado. Los equipos operan sin esta capacidad. | • No integration test suites deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de integration test suites con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | integration test suites adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | integration test suites estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | integration test suites está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q3: Em que medida Automação de Testes (end-to-end / journey tests) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `critical journeys automated`

**Contexto**

- **Qué mide (what):** Critical user journeys run automatically on every deploy.
- **Por qué importa (why):** E2E tests protect revenue-critical flows.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin end-to-end / journey tests implementado. Los equipos operan sin esta capacidad. | • No end-to-end / journey tests deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de end-to-end / journey tests con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | end-to-end / journey tests adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | end-to-end / journey tests estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | end-to-end / journey tests está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q4: Em que medida Automação de Testes (contract testing) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% service pairs with contract tests`

**Contexto**

- **Qué mide (what):** Consumer-driven contract tests catch API breakage.
- **Por qué importa (why):** Contract tests protect microservice compatibility.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin contract testing implementado. Los equipos operan sin esta capacidad. | • No contract testing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de contract testing con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | contract testing adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | contract testing estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | contract testing está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q5: Em que medida Automação de Testes (AI-assisted test generation) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% tests AI-generated`

**Contexto**

- **Qué mide (what):** AI proposes tests for new and changed code.
- **Por qué importa (why):** AI-generated tests raise the floor on coverage.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin ai-assisted test generation implementado. Los equipos operan sin esta capacidad. | • No AI-assisted test generation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de ai-assisted test generation con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | AI-assisted test generation adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | AI-assisted test generation estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | AI-assisted test generation está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q6: Em que medida Automação de Testes (flaky-test detection & quarantine) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `flaky test rate`

**Contexto**

- **Qué mide (what):** Flaky tests are auto-quarantined and triaged.
- **Por qué importa (why):** Flaky tests erode trust; detection restores it.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin flaky-test detection & quarantine implementado. Los equipos operan sin esta capacidad. | • No flaky-test detection & quarantine deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de flaky-test detection & quarantine con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | flaky-test detection & quarantine adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | flaky-test detection & quarantine estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | flaky-test detection & quarantine está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q7: Em que medida Automação de Testes (mutation testing) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** qa-test, Desarrollador, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `mutation score of critical modules`

**Contexto**

- **Qué mide (what):** Mutation testing validates the quality of the test suite.
- **Por qué importa (why):** Mutation scores reveal whether tests actually catch bugs.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin mutation testing implementado. Los equipos operan sin esta capacidad. | • No mutation testing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de mutation testing con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | mutation testing adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | mutation testing estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | mutation testing está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C7: Gestão de Incidentes e SRE (Gestión de Incidentes y SRE)

**7 preguntas en esta capability.**

### P2-C7-Q1: Em que medida Gestão de Incidentes e SRE (on-call rotation with tooling) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services with on-call`

**Contexto**

- **Qué mide (what):** Every prod service has a named on-call rotation.
- **Por qué importa (why):** Clear ownership is the foundation of reliability.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin on-call rotation with tooling implementado. Los equipos operan sin esta capacidad. | • No on-call rotation with tooling deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de on-call rotation with tooling con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | on-call rotation with tooling adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | on-call rotation with tooling estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | on-call rotation with tooling está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q2: Em que medida Gestão de Incidentes e SRE (blameless postmortems) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% incidents with postmortem`

**Contexto**

- **Qué mide (what):** Postmortems focus on systems, not people.
- **Por qué importa (why):** Blameless culture unlocks honest learning.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin blameless postmortems implementado. Los equipos operan sin esta capacidad. | • No blameless postmortems deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de blameless postmortems con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | blameless postmortems adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | blameless postmortems estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | blameless postmortems está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q3: Em que medida Gestão de Incidentes e SRE (error budget policy) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Seguridad, product-owner
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% services using error budgets`

**Contexto**

- **Qué mide (what):** Error budgets gate feature work vs reliability work.
- **Por qué importa (why):** Error budgets make reliability a shared business decision.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin error budget policy implementado. Los equipos operan sin esta capacidad. | • No error budget policy deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de error budget policy con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | error budget policy adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | error budget policy estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | error budget policy está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q4: Em que medida Gestão de Incidentes e SRE (chaos engineering) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `gamedays per quarter`

**Contexto**

- **Qué mide (what):** Controlled fault injection exercises resilience.
- **Por qué importa (why):** Chaos engineering builds confidence in recovery.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin chaos engineering implementado. Los equipos operan sin esta capacidad. | • No chaos engineering deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de chaos engineering con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | chaos engineering adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | chaos engineering estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | chaos engineering está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q5: Em que medida Gestão de Incidentes e SRE (incident commander role) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% major incidents with IC`

**Contexto**

- **Qué mide (what):** An incident commander coordinates response.
- **Por qué importa (why):** A single coordinator reduces confusion during incidents.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin incident commander role implementado. Los equipos operan sin esta capacidad. | • No incident commander role deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de incident commander role con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | incident commander role adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | incident commander role estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | incident commander role está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q6: Em que medida Gestão de Incidentes e SRE (SRE-dev partnership model) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% teams with SRE partner`

**Contexto**

- **Qué mide (what):** SRE and dev teams collaborate on reliability roadmaps.
- **Por qué importa (why):** Embedded partnership beats gatekeeping.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin sre-dev partnership model implementado. Los equipos operan sin esta capacidad. | • No SRE-dev partnership model deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de sre-dev partnership model con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SRE-dev partnership model adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | SRE-dev partnership model estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | SRE-dev partnership model está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q7: Em que medida Gestão de Incidentes e SRE (runbook automation) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% incidents with runbook run`

**Contexto**

- **Qué mide (what):** Runbook steps are codified and executed automatically.
- **Por qué importa (why):** Runbook automation shrinks MTTR and reduces human error.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin runbook automation implementado. Los equipos operan sin esta capacidad. | • No runbook automation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de runbook automation con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | runbook automation adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | runbook automation estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | runbook automation está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C8: Gestão de Artefatos e Pacotes (Gestión de Artefactos y Paquetes)

**5 preguntas en esta capability.**

### P2-C8-Q1: Em que medida Gestão de Artefatos e Pacotes (internal package registry) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% packages via registry`

**Contexto**

- **Qué mide (what):** Internal registry hosts all packages; no public-only deps.
- **Por qué importa (why):** A registry enables auditing and availability controls.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin internal package registry implementado. Los equipos operan sin esta capacidad. | • No internal package registry deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de internal package registry con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | internal package registry adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | internal package registry estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | internal package registry está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q2: Em que medida Gestão de Artefatos e Pacotes (SBOM for every build) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% builds with SBOM`

**Contexto**

- **Qué mide (what):** Each build generates a software bill of materials.
- **Por qué importa (why):** SBOMs are now a regulatory and security requirement.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin sbom for every build implementado. Los equipos operan sin esta capacidad. | • No SBOM for every build deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de sbom for every build con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SBOM for every build adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | SBOM for every build estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | SBOM for every build está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q3: Em que medida Gestão de Artefatos e Pacotes (artifact signing (SLSA)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% artifacts signed`

**Contexto**

- **Qué mide (what):** Artifacts are signed and verified on deploy.
- **Por qué importa (why):** Signing prevents supply-chain tampering.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin artifact signing (slsa) implementado. Los equipos operan sin esta capacidad. | • No artifact signing (SLSA) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de artifact signing (slsa) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | artifact signing (SLSA) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | artifact signing (SLSA) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | artifact signing (SLSA) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q4: Em que medida Gestão de Artefatos e Pacotes (vulnerability scanning of artifacts) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% artifacts scanned`

**Contexto**

- **Qué mide (what):** Every artifact is scanned before deployment.
- **Por qué importa (why):** Pre-deploy scanning blocks known-bad artifacts.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin vulnerability scanning of artifacts implementado. Los equipos operan sin esta capacidad. | • No vulnerability scanning of artifacts deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de vulnerability scanning of artifacts con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | vulnerability scanning of artifacts adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | vulnerability scanning of artifacts estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | vulnerability scanning of artifacts está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q5: Em que medida Gestão de Artefatos e Pacotes (retention & promotion policies) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `artifacts promoted via policy`

**Contexto**

- **Qué mide (what):** Artifacts move through dev→stage→prod with policy gates.
- **Por qué importa (why):** Promotion policies tie deploys to provenance.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin retention & promotion policies implementado. Los equipos operan sin esta capacidad. | • No retention & promotion policies deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de retention & promotion policies con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | retention & promotion policies adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | retention & promotion policies estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | retention & promotion policies está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C9: Gestão de Mudanças e GitOps (Gestión de Cambios y GitOps)

**5 preguntas en esta capability.**

### P2-C9-Q1: Em que medida Gestão de Mudanças e GitOps (GitOps controllers in prod) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% clusters on GitOps`

**Contexto**

- **Qué mide (what):** Cluster state is reconciled from Git by a controller.
- **Por qué importa (why):** GitOps makes change traceable, auditable, and reversible.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin gitops controllers in prod implementado. Los equipos operan sin esta capacidad. | • No GitOps controllers in prod deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de gitops controllers in prod con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | GitOps controllers in prod adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | GitOps controllers in prod estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | GitOps controllers in prod está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q2: Em que medida Gestão de Mudanças e GitOps (automated change tickets) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% changes ticketed automatically`

**Contexto**

- **Qué mide (what):** Change records are created from PRs automatically.
- **Por qué importa (why):** Automation keeps records accurate without slowing delivery.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin automated change tickets implementado. Los equipos operan sin esta capacidad. | • No automated change tickets deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de automated change tickets con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | automated change tickets adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | automated change tickets estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | automated change tickets está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q3: Em que medida Gestão de Mudanças e GitOps (approvals in PR (not tickets)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% approvals in PR`

**Contexto**

- **Qué mide (what):** Change approvals happen in code review, not separate tickets.
- **Por qué importa (why):** Approval-as-code cuts cycle time while keeping audit trail.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin approvals in pr (not tickets) implementado. Los equipos operan sin esta capacidad. | • No approvals in PR (not tickets) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de approvals in pr (not tickets) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | approvals in PR (not tickets) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | approvals in PR (not tickets) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | approvals in PR (not tickets) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q4: Em que medida Gestão de Mudanças e GitOps (environment promotion via PR) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% envs promoted via PR`

**Contexto**

- **Qué mide (what):** Moving from stage to prod is a PR, not a click.
- **Por qué importa (why):** PR-based promotion inherits review and rollback.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin environment promotion via pr implementado. Los equipos operan sin esta capacidad. | • No environment promotion via PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de environment promotion via pr con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | environment promotion via PR adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | environment promotion via PR estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | environment promotion via PR está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q5: Em que medida Gestão de Mudanças e GitOps (compliance evidence auto-collected) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** devops, Ingeniero de Plataforma, Seguridad
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `controls automated`

**Contexto**

- **Qué mide (what):** Evidence for SOC2/ISO is gathered automatically from CI.
- **Por qué importa (why):** Auto-evidence turns audits into a side effect of normal work.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin compliance evidence auto-collected implementado. Los equipos operan sin esta capacidad. | • No compliance evidence auto-collected deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de compliance evidence auto-collected con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | compliance evidence auto-collected adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | compliance evidence auto-collected estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | compliance evidence auto-collected está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C10: Segurança de Dependências e Cadeia de Suprimentos (Seguridad de Dependencias y Cadena de Suministro)

**5 preguntas en esta capability.**

### P2-C10-Q1: Em que medida Segurança de Dependências e Cadeia de Suprimentos (dependabot or renovate on every repo) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% repos auto-updated`

**Contexto**

- **Qué mide (what):** Dependabot or Renovate opens PRs for outdated deps.
- **Por qué importa (why):** Automated updates keep CVE window short.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin dependabot or renovate on every repo implementado. Los equipos operan sin esta capacidad. | • No dependabot or renovate on every repo deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de dependabot or renovate on every repo con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | dependabot or renovate on every repo adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | dependabot or renovate on every repo estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | dependabot or renovate on every repo está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q2: Em que medida Segurança de Dependências e Cadeia de Suprimentos (allow-list registries only) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `% deps from allow-listed source`

**Contexto**

- **Qué mide (what):** Proxy registries filter packages from trusted sources.
- **Por qué importa (why):** Proxying blocks typosquatting and malicious packages.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin allow-list registries only implementado. Los equipos operan sin esta capacidad. | • No allow-list registries only deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de allow-list registries only con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | allow-list registries only adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | allow-list registries only estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | allow-list registries only está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q3: Em que medida Segurança de Dependências e Cadeia de Suprimentos (build provenance (SLSA level)) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `SLSA level reached`

**Contexto**

- **Qué mide (what):** Builds carry verifiable provenance metadata.
- **Por qué importa (why):** Provenance is the foundation of supply-chain trust.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin build provenance (slsa level) implementado. Los equipos operan sin esta capacidad. | • No build provenance (SLSA level) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de build provenance (slsa level) con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | build provenance (SLSA level) adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | build provenance (SLSA level) estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | build provenance (SLSA level) está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q4: Em que medida Segurança de Dependências e Cadeia de Suprimentos (critical dep response playbook) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `median time to patch critical`

**Contexto**

- **Qué mide (what):** A playbook handles Log4Shell-class events.
- **Por qué importa (why):** Preparation beats improvisation in a zero-day.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin critical dep response playbook implementado. Los equipos operan sin esta capacidad. | • No critical dep response playbook deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de critical dep response playbook con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | critical dep response playbook adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | critical dep response playbook estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | critical dep response playbook está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q5: Em que medida Segurança de Dependências e Cadeia de Suprimentos (vendor/OSS risk reviews) foi adotado entre as equipes?

**Metadatos**

- **Público objetivo:** Seguridad, devops
- **Peso:** 1.0
- **Professional Edition:** No
- **KPI principal:** `critical vendors reviewed/year`

**Contexto**

- **Qué mide (what):** High-risk vendors and OSS dependencies are reviewed annually.
- **Por qué importa (why):** Review surfaces risk before it becomes an incident.

**Formato de respuesta**

Escala Likert de 5 niveles (L0–L4). Selecciona **un** nivel que mejor describa tu organización hoy. Agrega evidencia textual y/o anexos (PDF, DOCX, XLSX, PNG, JPEG, hasta 10 MB).

**Niveles y evidencias esperadas**

| Nivel | Etiqueta | Descripción | Evidencias sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sin vendor/oss risk reviews implementado. Los equipos operan sin esta capacidad. | • No vendor/OSS risk reviews deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | En Desarrollo | Implementación piloto de vendor/oss risk reviews con <10% de cobertura de equipos y uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | vendor/OSS risk reviews adoptado por 25-50% de los equipos con directrices básicas y capacitación. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gestionado | vendor/OSS risk reviews estandarizado en >75% de los equipos con resultados medidos y gobernanza. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizando | vendor/OSS risk reviews está optimizado, automatizado y mejorado continuamente con insights basados en datos. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## Cómo se puntúa esta sección

- Cada pregunta recibe un valor numérico del nivel seleccionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- La puntuación de la capacidad es el promedio ponderado de las preguntas (peso default = 1.0; las preguntas con peso 1.5 o 2.0 cuentan más).
- La puntuación del pilar **P2** es el promedio de las 10 capacidades.
- El resultado se muestra en escala 0–4 y se convierte a % de madurez (nivel / 4 × 100).

## Glosario rápido

- **Pillar:** dimensión estratégica de madurez.
- **Capability:** subdominio funcional dentro de un pilar.
- **Question:** ítem de evaluación concreto, ID estándar `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0–L4):** punto en la escala Likert de madurez.
- **KPI:** indicador clave que valida objetivamente el nivel declarado.
- **Evidence:** prueba cualitativa (texto) o cuantitativa (anexo) que sustenta la respuesta.
