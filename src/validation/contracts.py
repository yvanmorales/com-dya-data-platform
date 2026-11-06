from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Dict, Any, Tuple
import logging

logger = logging.getLogger(__name__)

class TransactionEventContract(BaseModel):
    """Contrato estricto para eventos transaccionales."""
    transaction_id: str = Field(..., min_length=1)
    client_id: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0.0, description="El monto debe ser estrictamente mayor a 0")
    tax_amount: float = Field(..., ge=0.0)
    created_at: datetime

def validate_payload(raw_data: Dict[str, Any]) -> Tuple[bool, Dict[str, Any], str]:
    """Valida un payload contra el contrato. Retorna (es_valido, datos_o_error)."""
    try:
        validated = TransactionEventContract(**raw_data)
        return True, validated.model_dump(mode='json'), ""
    except ValidationError as e:
        logger.warning(f"Payload rechazado por contrato de datos: {e}")
        return False, raw_data, str(e)