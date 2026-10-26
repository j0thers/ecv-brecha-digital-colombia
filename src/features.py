"""
Construcción de variables analíticas derivadas para el estudio.
"""
import pandas as pd
import numpy as np

def create_analytical_household_dataset(df_merged_hogar: pd.DataFrame) -> pd.DataFrame:
    df = df_merged_hogar.copy()
    df_out = pd.DataFrame()
    
    df_out["id_hogar"] = df["DIRECTORIO"].astype(str) + "_" + df["SECUENCIA_ENCUESTA"].astype(str)
    df_out["directorio"] = df["DIRECTORIO"]
    df_out["secuencia_p"] = df["SECUENCIA_ENCUESTA"]
    df_out["fex_c"] = df["FEX_C"].astype(float)
    df_out["codigo_dpto"] = df["DPTO"].astype(str).str.zfill(2)
    df_out["zona"] = np.where(df["CLASE"] == 1, "Urbana", "Rural")
    df_out["es_urbano"] = (df["CLASE"] == 1).astype(int)
    
    # Situación económica
    df_out["sit_eco_escala"] = pd.to_numeric(df["P3353"], errors="coerce")
    eco_map = {1: "1. Muy fácil", 2: "2. Fácil", 3: "3. Regular", 4: "4. Difícil", 5: "5. Muy difícil"}
    df_out["sit_eco_label"] = df_out["sit_eco_escala"].map(eco_map)
    df_out["alta_dificultad_eco"] = df_out["sit_eco_escala"].isin([4, 5]).astype(int)
    
    # Pobreza
    df_out["prob_pobreza_multidimensional"] = pd.to_numeric(df["P1912"], errors="coerce")
    df_out["prob_pobreza_monetaria"] = pd.to_numeric(df["P1911"], errors="coerce")
    df_out["pobreza_multidimensional_alta"] = (df_out["prob_pobreza_multidimensional"] >= 0.5).astype(int)
    
    # Dispositivos
    comp = (df["P5230"] == 1) | (df["P5230S1"] == 1) | (df["P5230S2"] == 1)
    df_out["tiene_computador"] = comp.astype(int)
    
    # Conexión hogar
    df_out["pago_internet_hogar"] = (df["P804"] == 1).astype(int)
    
    return df_out
