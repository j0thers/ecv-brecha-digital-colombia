"""
Pipeline de limpieza y estandarización de variables.
"""
import pandas as pd
import numpy as np

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().upper() for c in df.columns]
    return df

def clean_special_missing(series: pd.Series, missing_codes: list = [98, 99, 998, 999]) -> pd.Series:
    s = series.copy()
    s = s.replace(missing_codes, np.nan)
    s = s.replace([str(c) for c in missing_codes], np.nan)
    return s

def clean_binary_dane(series: pd.Series) -> pd.Series:
    """
    Estandariza variables dicotómicas del DANE (1=Sí, 2=No) a (1=Sí, 0=No).
    """
    s = series.copy()
    s = s.replace({2: 0, 2.0: 0, "2": 0, "1": 1, 1.0: 1})
    return s
