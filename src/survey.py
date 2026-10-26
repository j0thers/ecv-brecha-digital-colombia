"""
Estimación bajo diseño muestral complejo y cálculo del DEFF de Kish.
"""
import pandas as pd
import numpy as np

def weighted_mean(series: pd.Series, weights: pd.Series) -> float:
    mask = series.notna() & weights.notna()
    s = series[mask]
    w = weights[mask]
    return float((s * w).sum() / w.sum()) if w.sum() > 0 else np.nan

def weighted_proportion(series: pd.Series, weights: pd.Series, category=1) -> float:
    mask = series.notna() & weights.notna()
    s = series[mask]
    w = weights[mask]
    ind = (s == category).astype(float)
    return float((ind * w).sum() / w.sum() * 100) if w.sum() > 0 else np.nan

def kish_design_effect(weights: pd.Series) -> dict:
    w = weights.dropna()
    n = len(w)
    mean_w = w.mean()
    sd_w = w.std()
    cv_w = sd_w / mean_w if mean_w > 0 else 0.0
    deff = 1 + cv_w**2
    n_eff = n / deff if deff > 0 else 0.0
    return {
        "n_muestra": n,
        "suma_pesos": float(w.sum()),
        "media_peso": float(mean_w),
        "desv_est_peso": float(sd_w),
        "cv_peso": float(cv_w),
        "deff_kish": float(deff),
        "n_efectivo": float(n_eff),
    }
