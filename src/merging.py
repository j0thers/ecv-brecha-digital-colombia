"""
Integración de módulos a nivel de Hogar y Persona.
"""
import pandas as pd

def merge_household_modules(df_hogar: pd.DataFrame, df_diseno: pd.DataFrame) -> pd.DataFrame:
    """
    Integra módulo de Condiciones de Vida con Variables de Diseño Muestral.
    """
    df_dis_h = df_diseno.drop_duplicates(subset=["DIRECTORIO", "SECUENCIA_P"]).copy()
    merged = pd.merge(
        df_hogar,
        df_dis_h,
        left_on=["DIRECTORIO", "SECUENCIA_ENCUESTA"],
        right_on=["DIRECTORIO", "SECUENCIA_P"],
        how="inner"
    )
    return merged

def merge_person_modules(df_tic: pd.DataFrame, df_educ: pd.DataFrame, df_diseno: pd.DataFrame) -> pd.DataFrame:
    """
    Integra módulos a nivel de persona (TIC + Educación + Diseño Muestral).
    """
    p_keys = ["DIRECTORIO", "SECUENCIA_P", "ORDEN"]
    merged = pd.merge(df_tic, df_educ, on=p_keys, how="inner")
    merged = pd.merge(merged, df_diseno, on=p_keys, how="inner")
    return merged
