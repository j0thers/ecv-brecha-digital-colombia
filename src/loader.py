"""
Módulo de carga y validación de microdatos originales DANE.
"""
from pathlib import Path
import pandas as pd
from .config import PATHS, RAW_SOURCES, RAW_FILES, CSV_PARAMS

def load_raw_dane_module(module_name: str, nrows: int = None) -> pd.DataFrame:
    """
    Carga un módulo CSV original del DANE.
    """
    if module_name not in RAW_SOURCES:
        raise ValueError(f"Módulo no reconocido: {module_name}")
    path = RAW_SOURCES[module_name]
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {path}")
    return pd.read_csv(path, nrows=nrows, **CSV_PARAMS)

def copy_raw_data_to_project() -> None:
    """
    Copia los archivos fuente originales hacia data/raw/.
    """
    PATHS["raw"].mkdir(parents=True, exist_ok=True)
    for mod_name, src_path in RAW_SOURCES.items():
        dst_name = RAW_FILES[mod_name]
        dst_path = PATHS["raw"] / dst_name
        if not dst_path.exists() and src_path.exists():
            df = pd.read_csv(src_path, **CSV_PARAMS)
            df.to_parquet(dst_path.with_suffix(".parquet"), index=False)
            print(f"[OK] Módulo guardado en raw: {mod_name}")
