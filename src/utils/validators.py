import pandas as pd
import logging
from typing import List

logger = logging.getLogger(__name__)

def validate_mandatory_columns(df: pd.DataFrame, required_columns: List[str]) -> bool:
    """Valida que un DataFrame contenga las columnas obligatorias requeridas por el contrato de datos."""
    missing_cols = [col for col in required_columns if col not in df.columns]
    
    if missing_cols:
        logger.error(f"Faltan columnas obligatorias en el esquema: {missing_cols}")
        raise ValueError(f"Esquema inválido. Faltan columnas: {missing_cols}")
    logger.info("Validación de esquema superada con éxito.")
    
    return True