"""
Configuración global del proyecto: rutas, constantes y metadatos del DANE.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATHS = {
    "raw":        ROOT / "data" / "raw",
    "processed":  ROOT / "data" / "processed",
    "analytical": ROOT / "data" / "analytical",
    "figures":    ROOT / "figures",
    "reports":    ROOT / "reports",
    "docs":       ROOT / "docs",
}

_DANE_ROOT = Path(r"C:\Users\jeanp\Downloads\proyecto estadistica 1")

RAW_SOURCES = {
    "hogar":  _DANE_ROOT / "Condiciones de vida del hogar y tenencia de bienes.CSV",
    "tic":    _DANE_ROOT / "DBF-ENCV-Tecnologías_información_comunicación-2024" / "Tecnologías de información y comunicación.CSV",
    "educ":   _DANE_ROOT / "DBF-ENCV-Educación-2024" / "Educación.CSV",
    "diseno": _DANE_ROOT / "BDF-ENCV-Variables_diseño_muestral-ENCV2024" / "Variables diseño muestral.CSV",
}

RAW_FILES = {
    "hogar":  "Mod_Condiciones_vida_hogar.csv",
    "tic":    "Mod_TIC.csv",
    "educ":   "Mod_Educacion.csv",
    "diseno": "Mod_Disenio_muestral.csv",
}

CSV_PARAMS = {
    "sep": ";",
    "encoding": "latin-1",
    "low_memory": False,
}

ID_VARS = {
    "vivienda": ["DIRECTORIO"],
    "hogar":    ["DIRECTORIO", "SECUENCIA_ENCUESTA"],
    "persona":  ["DIRECTORIO", "SECUENCIA_P", "ORDEN"],
}

SURVEY_PARAMS = {
    "weight_var":       "FEX_C",
    "pop_hogares_est":  18_489_373,
    "pop_personas_est": 51_802_400,
}

VARS = {
    "hogar": {
        "sit_eco":        "P3353",
        "sit_eco_vs_ant": "P3354",
        "prob_pob_mon":   "P1911",
        "prob_pob_mul":   "P1912",
        "pago_internet":  "P804",
        "disp_comp":      "P5230",
        "disp_comp_port": "P5230S1",
        "disp_comp_esc":  "P5230S2",
        "disp_tablet":    "P5230S3",
    },
    "tic": {
        "usa_internet":     "P1070",
        "conexion_fija":    "P1071S1",
        "conexion_movil":   "P1071S2",
        "frecuencia_uso":   "P1072",
        "disp_celular":     "P1073",
        "lugar_uso_hogar":  "P1074S1",
        "lugar_uso_trabajo":"P1074S2",
        "lugar_uso_educ":   "P1074S3",
        "motivo_trabajo":   "P1075S1",
        "motivo_educacion": "P1075S2",
        "motivo_entreten":  "P1075S4",
    },
    "educ": {
        "sabe_leer":    "P8587",
        "asiste_educ":  "P8586",
        "nivel_educ":   "P1083",
        "grado_educ":   "P1083S1",
        "titulo_obt":   "P1084",
    },
    "diseno": {
        "fex_c":       "FEX_C",
        "departamento": "DPTO",
        "municipio":    "MPIO",
        "clase":        "CLASE",
        "estrato":      "ESTRATO",
        "upm":          "UPM",
    },
}

DEPARTAMENTOS_DANE = {
    "05": "Antioquia", "08": "Atlántico", "11": "Bogotá, D.C.", "13": "Bolívar",
    "15": "Boyacá", "17": "Caldas", "18": "Caquetá", "19": "Cauca",
    "20": "Cesar", "23": "Córdoba", "25": "Cundinamarca", "27": "Chocó",
    "41": "Huila", "44": "La Guajira", "47": "Magdalena", "50": "Meta",
    "52": "Nariño", "54": "Norte de Santander", "63": "Quindío", "66": "Risaralda",
    "68": "Santander", "70": "Sucre", "73": "Tolima", "76": "Valle del Cauca",
    "81": "Arauca", "85": "Casanare", "86": "Putumayo", "88": "San Andrés",
    "91": "Amazonas", "94": "Guainía", "95": "Guaviare", "97": "Vaupés", "99": "Vichada",
}

SPECIAL_CODES = [98, 99, 998, 999, "98", "99", "998", "999"]

VIZ = {
    "palette_primary":   "#1a3a5c",
    "palette_secondary": "#2e7d6e",
    "palette_accent":    "#d96b27",
    "palette_neutral":   "#f4f6f8",
    "font_family":       "sans-serif",
    "dpi":               150,
}

RANDOM_STATE = 42
ALPHA = 0.05
