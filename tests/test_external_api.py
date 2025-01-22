import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import operation_transaction

load_dotenv(".env")

api_key = os.getenv("API_KEY")


@patch("requests.get")
def test_currency_conversion_usd_to_rub(mock_get) -> None:
    mock_get.return_value.json.return_value = {"result": 75.0}
    mock_get.return_value.status_code = 200
    transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}
    result = operation_transaction(transaction)
    assert result, 75.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1", headers={"apikey": api_key}
    )
