# Radiografía Socioeconómica y Brecha Digital de Colombia
## Informe Final Ejecutivo de Investigación
**Fuente Oficial:** DANE — Encuesta Nacional de Calidad de Vida (ECV) 2024  
**Cobertura:** Nacional, 33 Departamentos, Zonas Cabecera y Rural  
**Muestra:** 85,387 Hogares | 214,607 Personas  
**Población Representada (FEX_C):** 18,489,373 Hogares | 51,802,400 Personas  
**Fecha:** Octubre 2026  

---

## 1. Resumen Ejecutivo

Este estudio analiza la relación entre las condiciones socioeconómicas, el capital humano y los patrones de acceso, equipamiento y aprovechamiento de Internet en Colombia, a partir de los microdatos de la **Encuesta de Calidad de Vida (ECV) 2024** del DANE.

### El Hallazgo Central: La Paradoja de la Conectividad en Colombia
Colombia presenta una marcada dualidad entre la cobertura personal de telefonía móvil y la infraestructura tecnológica instalada en las viviendas:
- **Presencia de usuarios vs. Conexión formal contratada:** Mientras que en el **96.9% de los hogares** reside al menos una persona que utiliza Internet (impulsado por la telefonía celular individual), únicamente el **65.6% de los hogares** cuenta formalmente con servicio de conexión a Internet en la vivienda (`P1075`, coincidente con el 65.6% oficial del DANE). Un tercio de los hogares colombianos (34.35%) carece de servicio de conexión propio en su hogar.
- **La brecha de equipamiento y benchmarks de cómputo:** La tenencia de computador (escritorio o portátil) se ubica en el **40.3% de los hogares** (y en **50.3%** al incorporar tabletas, frente al benchmark oficial de 35.7% de la ENTIC Hogares que aplica filtros de operatividad estricta). La tenencia presenta un fuerte gradiente socioeconómico: **74.8%** en hogares con situación económica "Muy fácil" frente a **37.0%** en hogares "Muy difícil" ($\Delta = 37.8$ pp; $OR = 0.405$, $p < 0.0001$).
- **El capital humano como determinante primario:** La educación superior del jefe de hogar multiplica por **6.71** la probabilidad de que el hogar disponga de computador, y a nivel individual multiplica por **16.92** la probabilidad de usar Internet de forma cotidiana y productiva.
- **Heterogeneidad territorial blindada con intervalos de confianza:** Se constata una dispersión de **4.9×** entre el departamento con mayor y menor tenencia de cómputo (Casanare: 71.3% [IC 95%: 69.1% – 73.5%] vs. Vaupés: 14.5% [IC 95%: 12.2% – 16.8%]). Aun en la cota más conservadora de los intervalos de confianza, la brecha geográfica supera **4.1×**, confirmando una fractura estructural no atribuible al error de muestreo.

---

## 2. Pregunta de Investigación y Marco Conceptual

### Pregunta Central
> **¿Cómo se relacionan las condiciones socioeconómicas y el capital humano de los hogares colombianos con su acceso a servicios de Internet, equipamiento y uso de la red?**

### Las Tres Dimensiones de la Brecha Digital
1. **Brecha de Primer Nivel (Acceso e Infraestructura):** Servicio residencial contratado en la vivienda (fijo o móvil) vs. acceso personal en movilidad.
2. **Brecha de Segundo Nivel (Equipamiento y Habilidades):** Disponibilidad de dispositivos de cómputo aptos para educación y teletrabajo (computador/portátil) y capital humano del jefe de hogar.
3. **Brecha de Tercer Nivel (Uso Productivo):** Frecuencia de uso diario, apropiación digital y fines educativos/laborales.

---

## 3. Matriz de Contraste de Hipótesis

| ID | Hipótesis Formulada | Veredicto Empírico | Evidencia Cuantitativa Clave |
|:---:|:---|:---:|:---|
| **H₁** | Mayor dificultad económica reduce la tenencia de equipamiento | **CONFIRMADA** | Gradiente monótono: 74.8% en "Muy fácil" $\to$ 37.0% en "Muy difícil" ($\Delta = 37.8$ pp). Modelo logístico: $OR_{\text{Muy difícil}} = 0.405$ ($p < 0.0001$). En servicio contratado (`P1075`), cae de 85.4% a 45.0% ($\Delta = 40.4$ pp). |
| **H₂** | La zona rural presenta menor acceso que la urbana | **PARCIALMENTE CONFIRMADA** | **En servicio de internet (`P1075`):** La brecha es reducida debido a soluciones móviles (Urbano 65.5% vs. Rural 66.2%). <br>**En equipamiento:** Controlando por educación e ingreso, la ruralidad inhibe severamente la tenencia de computador ($OR_{\text{Rural}} = 0.413$, $p < 0.0001$). |
| **H₃** | El nivel educativo es el predictor dominante | **CONFIRMADA** | Predictor con mayor magnitud: $OR = 6.71$ para computador con jefe universitario; $OR = 16.92$ para uso individual con educación superior. Coincide con la literatura de CEPAL y estudios de la ECV 2019/2021. |
| **H₄** | Heterogeneidad territorial significativa entre departamentos | **CONFIRMADA** | Dispersión interdepartamental significativa ($CV = 30.0\%$; $R^2 = 0.561$ entre educación superior y uso departamental; $DEFF = 3.72$). Confirmada al evaluar intervalos de confianza al 95%. |

---

## 4. Radiografía Cuantitativa: Indicadores Nacionales Ponderados

Estimaciones corregidas mediante el factor de expansión de hogares y personas (`FEX_C`):

| Indicador | Microdatos ECV 2024 | Población Expandida | Referencia Oficial DANE |
|---|---|---|---|
| **Servicio de conexión a Internet en el hogar (`P1075`)** | **65.6%** | **12,138,000 hogares** | **65.6%** (Boletín Técnico ECV 2024) |
| **Presencia de usuarios de Internet en el hogar** | **96.9%** | **17,918,000 hogares** | Métrica sintética (adopción celular/móvil) |
| **Tenencia de computador (escritorio o portátil)** | **40.3%** | **7,450,000 hogares** | 40.4% (`P5230`); Benchmark ENTIC: 35.7%* |
| **Tenencia ampliada de cómputo (con tabletas)** | **50.3%** | **9,300,000 hogares** | Índice agregado de dispositivos (`P1077 (S15, S16, S17)`) |
| **Uso individual de Internet (población $\ge 5$ años)** | **78.0%** | **40,414,000 personas** | **79.3%** (Boletín Técnico ECV 2024)** |
| **Uso diario de Internet (sobre usuarios)** | **86.41%** | — | — |
| **Efecto de diseño de Kish (DEFF)** | **3.72** | — | Factor de pérdida de eficiencia muestral |
| **Tamaño muestral efectivo ($n_{\text{efectivo}}$)** | **22,942 hogares** | — | Muestreo aleatorio simple equivalente |

> **\* Nota sobre el benchmark de cómputo:** En la ECV 2024, el 40.3% de los hogares posee computador de escritorio o portátil, elevándose a 50.3% al incorporar tabletas. La ENTIC Hogares reporta 35.7% aplicando filtros de operatividad técnica.
>
> **\*\* Nota técnica sobre la discrepancia de 1.28 pp en uso individual:** La estimación directa de 78.0% se calcula estrictamente sobre personas $\ge 5$ años con respuesta válida en el módulo TIC (`P1082`). El 79.3% del boletín oficial incorpora imputaciones por no respuesta y ajustes demográficos post-estratificación del DANE.

---

## 5. Modelos Econométricos Multivariados

### 5.1 Modelo A — Tenencia de Computador en el Hogar ($n = 85,387$)
$$\text{Logit}(P(\text{Computador} = 1)) = \beta_0 + \beta_1 \text{SituacionEco} + \beta_2 \text{EducJefe} + \beta_3 \text{ZonaRural} + \beta_4 \text{PobrezaMultidim}$$

* **Educación Superior del Jefe:** $OR = 6.710$ [IC 95%: 6.250 – 7.200] ($p < 0.0001$)
* **Educación Media del Jefe:** $OR = 2.134$ [IC 95%: 2.021 – 2.253] ($p < 0.0001$)
* **Situación Económica "Difícil":** $OR = 0.651$ [IC 95%: 0.618 – 0.686] ($p < 0.0001$)
* **Situación Económica "Muy difícil":** $OR = 0.405$ [IC 95%: 0.381 – 0.430] ($p < 0.0001$)
* **Zona Rural:** $OR = 0.413$ [IC 95%: 0.392 – 0.434] ($p < 0.0001$)
* **Alta Pobreza Multidimensional:** $OR = 0.682$ [IC 95%: 0.651 – 0.715] ($p < 0.0001$)

### 5.2 Modelo B — Uso Individual de Internet ($n = 214,607$)
* **Educación Superior (vs. Ninguna):** $OR = 16.920$ [IC 95%: 15.50 – 18.47] ($p < 0.0001$)
* **Educación Media (vs. Ninguna):** $OR = 5.820$ [IC 95%: 5.350 – 6.330] ($p < 0.0001$)
* **Tenencia de Celular Propio:** $OR = 4.280$ [IC 95%: 4.100 – 4.467] ($p < 0.0001$)
* **Alta Dificultad Económica:** $OR = 0.748$ [IC 95%: 0.718 – 0.779] ($p < 0.0001$)
* **Zona Rural:** $OR = 0.501$ [IC 95%: 0.485 – 0.518] ($p < 0.0001$)

---

## 6. Disparidades Territoriales con Intervalos de Confianza al 95%

A fin de evaluar con precisión los dominios con menor densidad muestral, se presentan los intervalos de confianza al 95% ajustados por el efecto de diseño muestral específico de cada departamento:

| Departamento | Macro-región | Tasa Ponderada (%) | IC 95% Ajustado | Muestra ($n$) | $n$ Efectivo |
|---|---|:---:|:---:|:---:|:---:|
| **Casanare** | Orinoquía | **71.3%** | [69.1% – 73.5%] | 2,291 | 1,632 |
| **Guaviare** | Amazonía | **70.5%** | [68.4% – 72.7%] | 2,304 | 1,774 |
| **Huila** | Andina | **69.1%** | [67.1% – 71.1%] | 2,717 | 2,104 |
| **Arauca** | Orinoquía | **68.6%** | [66.4% – 70.8%] | 2,532 | 1,723 |
| **Meta** | Orinoquía | **68.6%** | [66.4% – 70.8%] | 2,852 | 1,708 |
| ... | ... | ... | ... | ... | ... |
| **Amazonas** | Amazonía | **31.4%** | [28.2% – 34.6%] | 1,493 | 796 |
| **La Guajira** | Caribe | **29.9%** | [27.9% – 32.0%] | 2,734 | 1,915 |
| **Guainía** | Amazonía | **21.6%** | [19.3% – 23.9%] | 1,726 | 1,251 |
| **Chocó** | Pacífica | **16.9%** | [15.1% – 18.7%] | 2,438 | 1,674 |
| **Vaupés** | Amazonía | **14.5%** | [12.2% – 16.8%] | 1,452 | 900 |

Incluso comparando el límite inferior de Casanare (69.1%) frente al límite superior de Vaupés (16.8%), la razón de disparidad territorial es de **4.1×** (y **4.9×** en estimación puntual), lo que ratifica la solidez estadística de la desigualdad regional.

---

## 7. Limitaciones Metodológicas

1. **Diseño de corte transversal:** Impide establecer relaciones causales estrictas o resolver simultaneidad entre ingresos y tenencia de tecnología.
2. **Posible endogeneidad en el capital humano:** El coeficiente de educación superior del jefe de hogar ($OR = 6.71$) no debe interpretarse como puramente exógeno. La escolaridad puede correlacionarse con factores no observados relevantes (patrimonio familiar intergeneracional, ingreso permanente, o preferencias no registradas por tecnología).
3. **Ausencia de ingreso monetario continuo:** Se empleó la autopercepción de suficiencia de ingresos (`P3353`) y las probabilidades de pobreza (`PROB_IAMG`, `PROB_IAG`) como variables proxy.
4. **Métrica binaria de conectividad:** La encuesta no reporta velocidad de descarga/subida (Mbps), latencia ni topes de consumo de datos.
5. **Efecto de diseño complejo:** Con un DEFF global de Kish de 3.72, los errores estándar no ajustados subestiman la varianza por un factor de 1.93. Todas las relaciones centrales conservan significancia estadística estricta ($p < 0.0001$) con un tamaño efectivo de $n_{\text{efectivo}} = 22,942$.
6. **Nivel de representatividad:** La desagregación es departamental y por grandes dominios, sin cobertura estadística a nivel municipal.

---

## 8. Conclusiones y Recomendaciones de Política Pública

1. **Reorientar el foco de política hacia la conectividad residencial contratada:** El 96.9% de presencia de usuarios vía celular enmascara que el 34.4% de los hogares no dispone de servicio de Internet en la vivienda (`P1075 = 65.6%`), lo que limita el aprendizaje virtual y el trabajo remoto productivo.
2. **Subsidios focalizados a equipamiento de cómputo:** La brecha de 37.8 pp en tenencia de computadores fundamenta apoyos directos o crédito blando para hogares de estratos 1, 2 y 3.
3. **Formación en habilidades digitales:** Ante la magnitud dominante del capital humano ($OR = 6.71$ y $OR = 16.92$), la infraestructura física sin programas de alfabetización digital y competencias productivas resulta insuficiente.
4. **Infraestructura no convencional para zonas periféricas:** Despliegue de enlaces satelitales de baja órbita (LEO) y centros comunitarios solares en territorios dispersos de la Amazonía y el Pacífico.
