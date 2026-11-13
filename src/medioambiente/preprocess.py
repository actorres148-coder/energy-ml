"""src/medioambiente/preprocess.py — Etiquetado de episodios de alta contaminación por CO."""

from __future__ import annotations

import pandas as pd

from src.infrastructure.settings.logger import logger

COLUMNA_CO = "CO(GT)"
COLUMNA_ETIQUETA = "episodio"
UMBRAL_EPISODIO_MG_M3 = 2.5  # Umbral pedagógico (mg/m³), no normativo.


def construir_etiqueta(df: pd.DataFrame, umbral: float = UMBRAL_EPISODIO_MG_M3) -> pd.DataFrame:
    """Descarta filas sin CO(GT) y agrega la columna `episodio` (1 si CO >= umbral).

    Las filas descartadas son las que no permiten calcular la etiqueta
    (CO(GT) faltante, es decir -200 convertido a NaN).
    """
    filas_antes = len(df)
    con_co = df.dropna(subset=[COLUMNA_CO]).copy()
    con_co[COLUMNA_ETIQUETA] = (con_co[COLUMNA_CO] >= umbral).astype("int8")
    logger.info(
        "Etiqueta `episodio` construida: %d/%d filas utilizadas "
        "(%d descartadas por CO(GT) faltante), umbral >= %.1f mg/m³",
        len(con_co),
        filas_antes,
        filas_antes - len(con_co),
        umbral,
    )
    return con_co
