"""
Indicadores territoriales y macro-regionales de Colombia.
"""
import pandas as pd
import numpy as np
from .config import DEPARTAMENTOS_DANE

REGION_MAP = {
    "05": "Andina", "15": "Andina", "17": "Andina", "25": "Andina",
    "41": "Andina", "54": "Andina", "63": "Andina", "66": "Andina",
    "68": "Andina", "73": "Andina",
    "11": "Bogotá D.C.",
    "08": "Caribe", "13": "Caribe", "20": "Caribe", "23": "Caribe",
    "44": "Caribe", "47": "Caribe", "70": "Caribe", "88": "Caribe",
    "19": "Pacífica", "27": "Pacífica", "52": "Pacífica", "76": "Pacífica",
    "81": "Orinoquía", "85": "Orinoquía", "50": "Orinoquía", "99": "Orinoquía",
    "18": "Amazonía", "86": "Amazonía", "91": "Amazonía", "94": "Amazonía",
    "95": "Amazonía", "97": "Amazonía",
}

REGION_COLORS = {
    "Bogotá D.C.": "#1f77b4",
    "Andina":      "#2ca02c",
    "Caribe":      "#ff7f0e",
    "Pacífica":    "#d62728",
    "Orinoquía":   "#9467bd",
    "Amazonía":    "#8c564b",
}

def weighted_rate(group: pd.DataFrame, var: str, weight: str = "fex_c") -> float:
    w = group[weight]
    v = group[var]
    mask = w.notna() & v.notna()
    if not mask.any():
        return np.nan
    return float((v[mask] * w[mask]).sum() / w[mask].sum() * 100)

def compute_departmental_indicators(df_h: pd.DataFrame, df_p: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for cod_dpto, dpto_name in DEPARTAMENTOS_DANE.items():
        sub_h = df_h[df_h["codigo_dpto"] == cod_dpto]
        sub_p = df_p[df_p["codigo_dpto"] == cod_dpto]
        if len(sub_h) == 0:
            continue
        region = REGION_MAP.get(cod_dpto, "Otra")
        comp = weighted_rate(sub_h, "tiene_computador")
        fijo = weighted_rate(sub_h, "tiene_internet_fijo")
        movil = weighted_rate(sub_h, "tiene_internet_movil")
        tot = weighted_rate(sub_h, "acceso_internet_hogar")
        pob = weighted_rate(sub_h, "pobreza_multidimensional_alta")
        uso_p = weighted_rate(sub_p, "usa_internet")
        edu_p = weighted_rate(sub_p, "tiene_educacion_superior")
        
        rows.append({
            "codigo_dpto": cod_dpto,
            "departamento": dpto_name,
            "region": region,
            "pct_computador": comp,
            "pct_internet_fijo": fijo,
            "pct_internet_movil": movil,
            "pct_acceso_total_hogar": tot,
            "pct_pobreza_multidimensional": pob,
            "pct_uso_internet_persona": uso_p,
            "pct_educ_superior_persona": edu_p,
            "n_hogares_muestra": len(sub_h),
            "hogares_expandidos": float(sub_h["fex_c"].sum()),
        })
    df_res = pd.DataFrame(rows).sort_values("pct_computador", ascending=False).reset_index(drop=True)
    return df_res

def compute_regional_indicators(df_h: pd.DataFrame, df_p: pd.DataFrame) -> pd.DataFrame:
    df_h_reg = df_h.copy()
    df_h_reg["region"] = df_h_reg["codigo_dpto"].map(REGION_MAP)
    df_p_reg = df_p.copy()
    df_p_reg["region"] = df_p_reg["codigo_dpto"].map(REGION_MAP)
    
    rows = []
    for region in ["Bogotá D.C.", "Andina", "Caribe", "Pacífica", "Orinoquía", "Amazonía"]:
        sub_h = df_h_reg[df_h_reg["region"] == region]
        sub_p = df_p_reg[df_p_reg["region"] == region]
        if len(sub_h) == 0:
            continue
        comp = weighted_rate(sub_h, "tiene_computador")
        fijo = weighted_rate(sub_h, "tiene_internet_fijo")
        movil = weighted_rate(sub_h, "tiene_internet_movil")
        pob = weighted_rate(sub_h, "pobreza_multidimensional_alta")
        uso_p = weighted_rate(sub_p, "usa_internet")
        
        rows.append({
            "region": region,
            "pct_computador": comp,
            "pct_internet_fijo": fijo,
            "pct_internet_movil": movil,
            "pct_pobreza_multidimensional": pob,
            "pct_uso_internet_persona": uso_p,
            "hogares_expandidos": float(sub_h["fex_c"].sum()),
        })
    return pd.DataFrame(rows)
