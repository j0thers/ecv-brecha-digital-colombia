"""
Estilos y utilidades de visualización gráfica sin emojis ni solapamientos.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
from .config import PATHS, VIZ

def set_style():
    plt.rcParams.update({
        "font.family":       VIZ["font_family"],
        "font.size":         10,
        "axes.titlesize":    12,
        "axes.titleweight":  "bold",
        "axes.labelsize":    10,
        "axes.labelweight":  "normal",
        "xtick.labelsize":   9,
        "ytick.labelsize":   9,
        "legend.fontsize":   9,
        "figure.titlesize":  14,
        "figure.titleweight":"bold",
        "figure.dpi":        VIZ["dpi"],
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "axes.grid":         True,
        "grid.linestyle":    "--",
        "grid.alpha":        0.5,
        "grid.color":        "#cccccc",
    })

def save_fig(fig: plt.Figure, name: str, formats: list = ["png", "svg"]):
    PATHS["figures"].mkdir(parents=True, exist_ok=True)
    for fmt in formats:
        out = PATHS["figures"] / f"{name}.{fmt}"
        if out.exists():
            try:
                out.unlink()
            except Exception:
                pass
        fig.savefig(out, bbox_inches="tight", dpi=VIZ["dpi"])
    print(f"[OK] Figura guardada: {name}")

def annotate_source(fig, text="Fuente: DANE — ECV 2024. Cálculos propios.", x=0.02, y=-0.02):
    fig.text(x, y, text, fontsize=8, color="#555555", style="italic", ha="left", va="top")
