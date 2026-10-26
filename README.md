# Radiografía Socioeconómica y Brecha Digital de Colombia
**Análisis de Microdatos — Encuesta de Calidad de Vida (ECV) 2024, DANE**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.12](https://img.shields.io/badge/Python-3.12-brightgreen.svg)](requirements.txt)
[![Data: DANE ECV 2024](https://img.shields.io/badge/Data-DANE%20ECV%202024-orange.svg)](https://microdatos.dane.gov.co)

---

## Pregunta de investigación

¿Cómo se relacionan las condiciones socioeconómicas y el capital humano de los hogares colombianos con su acceso a servicios de Internet, su equipamiento de cómputo y el uso efectivo de la red?

---

## Indicadores clave y consistencia con cifras oficiales

| Indicador | Definición Operacional (Microdatos ECV 2024) | Valor Ponderado (`FEX_C`) | Cifra Oficial DANE / Referencia |
|---|---|---|---|
| **Servicio de conexión a Internet en el hogar** | Pregunta de servicio residencial `P1075` (conexión fija o móvil contratada en la vivienda) | **65.6%** | **65.6%** (Boletín Técnico ECV 2024) |
| **Presencia de usuarios de Internet en el hogar** | Hogares con $\ge 1$ integrante de 5+ años que usó Internet (`P1082`) | **96.9%** | Métrica sintética de adopción en el hogar |
| **Tenencia de computador (escritorio o portátil)** | Hogares con equipo de escritorio o portátil (`P1077S15` / `P1077S16` / `P5230`) | **40.3%** | 40.4% (`P5230`); Benchmark ENTIC: 35.7%* |
| **Tenencia ampliada de cómputo (con tabletas)** | Hogares con computador de escritorio, portátil o tableta (`P1077 (S15, S16, S17)`) | **50.3%** | Índice agregado de dispositivos |
| **Uso individual de Internet (población $\ge 5$ años)** | Personas de 5 años y más que usaron Internet en los últimos 12 meses (`P1082`) | **78.0%** | **79.3%** (Boletín Técnico ECV 2024)** |

> **\* Aclaración sobre el benchmark de tenencia de computador:** En los microdatos de la ECV 2024, el 40.3% de los hogares reporta tenencia de computador (escritorio o portátil), cifra consistente con la pregunta de control `P5230` (40.42%). Al incorporar tabletas (`P1077S17`: 20.69%), la tenencia combinada alcanza el 50.3%. Por su parte, el boletín técnico de la ENTIC Hogares reporta un 35.7% a nivel nacional, derivado de criterios operacionales específicos sobre equipos plenamente funcionales.
>
> **\*\* Nota técnica sobre la discrepancia de 1.28 pp en uso individual:** La estimación directa en los microdatos arroja 78.0% sobre las personas $\ge 5$ años con respuesta efectiva en el módulo TIC (`P1082`). La diferencia con el 79.3% del boletín oficial obedece a ajustes post-estratificación por no respuesta imputada y factores de calibración demográfica proyectados por el DANE.

---

## Hallazgos empíricos principales

- **La dualidad de la conectividad en Colombia:** Existe una brecha sustantiva entre la *presencia de usuarios* (96.9%) y la *conexión domiciliaria contratada* (65.6%). La telefonía móvil individual brinda conectividad básica ubicua, pero un tercio de los hogares (34.35%) carece de un servicio de conexión en la vivienda apto para teletrabajo o educación formal intensiva.
- **Gradiente económico (H₁):** La contratación del servicio formal de Internet (`P1075`) desciende del **85.4%** en hogares con situación económica "muy fácil" al **45.0%** en "muy difícil" (brecha de 40.4 pp). En tenencia de computador (escritorio/portátil/tableta), la brecha es de 37.8 pp (74.8% vs. 37.0%), manteniéndose estadísticamente significativa en el modelo logístico multivariado (OR ajustado = 0.405, IC 95%: 0.381–0.430, $p < 0.0001$).
- **Capital humano como determinante primario (H₃):** La escolaridad del jefe de hogar es el predictor con mayor fuerza explicativa en el modelo condicional. Contar con educación superior multiplica por **6.71** la probabilidad de tener computador en el hogar (IC 95%: 6.25–7.20), superando el impacto del ingreso relativo y la ubicación geográfica. A nivel individual, la educación superior multiplica por **16.92** la probabilidad de usar Internet frente a no tener escolaridad formal.
- **Contraste con la literatura:** Este resultado corrobora la literatura empírica sobre brecha digital en América Latina (CEPAL, 2021; Galperin, 2017) y evaluaciones previas con la ECV en Colombia (2019 pre-pandemia y 2021 post-pandemia), las cuales demuestran que las habilidades y el capital humano constituyen el cuello de botella estructural de la adopción tecnológica productiva ("brecha de segundo nivel"), una vez resuelta la cobertura móvil elemental.

---

## Modelos econométricos (Resumen de Odds Ratios)

Regresiones logísticas binarias estimadas con errores estándar robustos:

| Variable explicativa | Modelo A: Hogar (Computador)<br>OR [IC 95%] | Modelo B: Persona (Uso Internet)<br>OR [IC 95%] |
|---|---|---|
| **Educación superior** (vs. sin escolaridad) | **6.71** [6.25 – 7.20] | **16.92** [15.50 – 18.47] |
| **Educación media** (vs. sin escolaridad) | **2.13** [2.02 – 2.25] | **5.82** [5.35 – 6.33] |
| **Zona rural** (vs. cabecera urbana) | **0.41** [0.39 – 0.43] | **0.50** [0.49 – 0.52] |
| **Situación económica muy difícil** (vs. fácil) | **0.41** [0.38 – 0.43] | **0.75** [0.72 – 0.78] |
| **Tenencia de celular propio** | — | **4.28** [4.10 – 4.47] |

*Todos los coeficientes con $p < 0.0001$. Tamaño muestral: Hogares $n = 85,387$; Personas $n = 214,607$.*

---

## Disparidades territoriales e intervalos de confianza al 95%

Para blindar el análisis frente a la variabilidad de dominios con menor tamaño muestral, se calcularon los intervalos de confianza al 95% ajustados por el efecto de diseño muestral complejo ($\text{DEFF}$ de Kish específico por departamento):

| Posición | Departamento | Macro-región | Tasa Ponderada (%) | IC 95% Ajustado (DEFF) | Muestra ($n$) | $n$ Efectivo |
|:---:|---|---|:---:|:---:|:---:|:---:|
| 1 | **Casanare** | Orinoquía | **71.3%** | [69.1% – 73.5%] | 2,291 | 1,632 |
| 2 | **Guaviare** | Amazonía | **70.5%** | [68.4% – 72.7%] | 2,304 | 1,774 |
| 3 | **Huila** | Andina | **69.1%** | [67.1% – 71.1%] | 2,717 | 2,104 |
| 4 | **Arauca** | Orinoquía | **68.6%** | [66.4% – 70.8%] | 2,532 | 1,723 |
| 5 | **Meta** | Orinoquía | **68.6%** | [66.4% – 70.8%] | 2,852 | 1,708 |
| ... | ... | ... | ... | ... | ... | ... |
| 29 | **Amazonas** | Amazonía | **31.4%** | [28.2% – 34.6%] | 1,493 | 796 |
| 30 | **La Guajira** | Caribe | **29.9%** | [27.9% – 32.0%] | 2,734 | 1,915 |
| 31 | **Guainía** | Amazonía | **21.6%** | [19.3% – 23.9%] | 1,726 | 1,251 |
| 32 | **Chocó** | Pacífica | **16.9%** | [15.1% – 18.7%] | 2,438 | 1,674 |
| 33 | **Vaupés** | Amazonía | **14.5%** | [12.2% – 16.8%] | 1,452 | 900 |

> **Interpretación metodológica:** Aun en el escenario más conservador (comparando el límite inferior de Casanare [69.1%] con el límite superior de Vaupés [16.8%]), la razón de brecha territorial supera **4.1×** (y **4.9×** en estimación puntual). La brecha geográfica es estructural y estadísticamente irrebatible, aun tras considerar la mayor variabilidad de los dominios periféricos.

---

## Limitaciones metodológicas

1. **Diseño de corte transversal:** Las estimaciones reflejan asociaciones condicionales y disparidades observadas, no efectos causales directos.
2. **Posible endogeneidad en el capital humano:** El coeficiente de educación superior del jefe de hogar ($\text{OR} = 6.71$) no debe asumirse como puramente exógeno. La escolaridad suele correlacionarse con determinantes no observados como el patrimonio intergeneracional, el ingreso permanente o preferencias tecnológicas latentes.
3. **Medición del ingreso:** La ECV no incorpora un módulo de ingresos continuos detallado. Se utiliza la percepción subjetiva de suficiencia de ingresos (`P3353`) y las probabilidades de pobreza multidimensional/monetaria (`PROB_IAMG`, `PROB_IAG`) como variables proxy.
4. **Métrica binaria de conectividad:** La encuesta registra la presencia o ausencia de conexión, pero no captura métricas continuas de calidad de servicio (ancho de banda en Mbps, latencia, estabilidad o límites de consumo de datos).
5. **Efecto de diseño complejo:** Debido al muestreo probabilístico por conglomerados bietápico de la ECV, el factor de inflación de varianza global de Kish es $\text{DEFF} = 3.72$, lo que equivale a un tamaño muestral efectivo de $n_{\text{efectivo}} = 22,942$ hogares.
6. **Nivel de desagregación:** La representatividad estadística de la ECV es departamental y por grandes dominios (cabecera / rural disperso), impidiendo análisis a escala municipal.

---

## Estructura del repositorio

```
├── notebooks/          # 15 cuadernos de análisis secuenciales y reproducibles
├── src/                # Módulos Python reutilizables
│   ├── config.py       # Rutas, metadatos y codificación DANE
│   ├── loader.py       # Carga e importación de microdatos
│   ├── cleaning.py     # Pipeline de estandarización y missing values
│   ├── merging.py      # Enlaces jerárquicos de módulos con auditoría
│   ├── features.py     # Ingeniería de variables analíticas
│   ├── stats.py        # Modelos logit y contraste de hipótesis
│   ├── survey.py       # Ponderación Horvitz-Thompson y DEFF de Kish
│   ├── territory.py    # Disparidades departamentales y regionales
│   └── viz.py          # Visualizaciones estándar de publicación
├── figures/            # 19 gráficos generados (formatos PNG y SVG)
├── reports/            # Informe final ejecutivo (.md y .docx)
├── data/               # Estructura de carpetas de datos
├── CITATION.cff        # Metadatos para citación académica
├── LICENSE             # Licencia MIT
└── requirements.txt    # Dependencias fijadas
```

---

## Fuente de datos y reproducibilidad

Los microdatos originales provienen del **Archivo Nacional de Datos (ANDA)** del DANE y están sujetos a los términos de uso institucionales. Pueden obtenerse gratuitamente en: [microdatos.dane.gov.co](https://microdatos.dane.gov.co).

```bash
# 1. Clonar el repositorio
git clone https://github.com/j0thers/ecv-brecha-digital-colombia.git
cd ecv-brecha-digital-colombia

# 2. Configurar entorno virtual e instalar dependencias
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate       # Linux / macOS
pip install -r requirements.txt

# 3. Ubicar los microdatos en data/raw/ y ejecutar en Jupyter Lab
jupyter lab
```

---

## Cómo citar este trabajo

Si utiliza los códigos o resultados de este análisis, por favor cite:

```bibtex
@misc{j0thers2026brechadigital,
  author = {j0thers},
  title = {Radiografía Socioeconómica y Brecha Digital de Colombia: Análisis de Microdatos ECV 2024 (DANE)},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/j0thers/ecv-brecha-digital-colombia}}
}
```

---

## Licencia

Este proyecto está distribuido bajo la licencia [MIT](LICENSE).
