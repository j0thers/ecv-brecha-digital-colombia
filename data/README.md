# Datos — ECV 2024 DANE

## Fuente

**Encuesta de Calidad de Vida (ECV) 2024**
- Organismo: DANE — Departamento Administrativo Nacional de Estadística
- URL de descarga: https://microdatos.dane.gov.co/index.php/catalog/ECV
- Licencia: Uso académico y de investigación — ver términos del DANE

---

## Instrucciones de descarga

1. Ir a https://microdatos.dane.gov.co
2. Buscar **ECV 2024**
3. Descargar los siguientes módulos (archivos `.csv` o `.sav`):

| Módulo | Archivo esperado | Descripción |
|---|---|---|
| Principal | `Mod_Condiciones_vida_hogar.csv` | Condiciones de vida del hogar y tenencia de bienes |
| TIC | `Mod_TIC.csv` | Acceso y uso de TIC / Internet |
| Educación | `Mod_Educacion.csv` | Nivel educativo por persona |
| Diseño muestral | `Mod_Disenio_muestral.csv` | Factores de expansión (FEX_C) |

4. Colocar los archivos **sin modificar** en `data/raw/`

---

## Estructura jerárquica

```
Vivienda  (ID: DIRECTORIO)
    └── Hogar  (ID: DIRECTORIO + SECUENCIA_P)
            └── Persona  (ID: DIRECTORIO + SECUENCIA_P + ORDEN)
```

> **Importante**: Antes de hacer cualquier merge, confirmar que los identificadores
> del módulo a integrar corresponden al nivel correcto (hogar vs persona).

---

## Variables clave de identificación

| Variable | Nivel | Descripción |
|---|---|---|
| `DIRECTORIO` | Vivienda | Identificador de la vivienda |
| `SECUENCIA_P` | Hogar | Secuencia del hogar dentro de la vivienda |
| `ORDEN` | Persona | Número de orden de la persona en el hogar |
| `FEX_C` | Hogar/Persona | Factor de expansión calibrado |

---

## Tamaños de referencia (ECV 2023 — orientativo)

| Módulo | Hogares aprox. | Personas aprox. |
|---|---|---|
| Condiciones vida | ~85,000 | — |
| TIC | ~85,000 | — |
| Educación | — | ~250,000 |

> Actualizar con los valores reales de la ECV 2024 al momento de la auditoría inicial.

---

## Advertencia sobre los datos

Los microdatos del DANE **no deben subirse a GitHub**. El `.gitignore`
está configurado para excluir automáticamente todos los archivos en `data/raw/`,
`data/processed/` y `data/analytical/`.

Si necesitas compartir el proyecto completo con otra persona, comparte este
`data/README.md` con las instrucciones de descarga.
