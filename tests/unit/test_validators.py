import pandas as pd
import pytest
from src.utils.validators import validate_mandatory_columns

def test_validate_mandatory_columns_success():
    df = pd.DataFrame({"transaction_id": [1], "amount": [100.0]})
    assert validate_mandatory_columns(df, ["transaction_id", "amount"]) is True

def test_validate_mandatory_columns_failure():
    df = pd.DataFrame({"transaction_id": [1]})
    with pytest.raises(ValueError, match="Esquema inválido"):
        validate_mandatory_columns(df, ["transaction_id", "amount"])