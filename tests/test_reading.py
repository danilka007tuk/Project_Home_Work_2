from unittest.mock import mock_open, patch

import pandas as pd

from src.reading import read_csv, read_excel


@patch("builtins.open", new_callable=mock_open, read_data="id,state\n650703,EXECUTED\n3598919,EXECUTED")
def test_read_csv(mocked_open):
    # Вызываем функцию с тестовым файлом
    result = read_csv("test.csv")
    # Проверяем результат
    expected_result = [{"id": "650703", "state": "EXECUTED"}, {"id": "3598919", "state": "EXECUTED"}]
    assert result == expected_result

    mocked_open.assert_called_once_with("test.csv", "r", encoding="utf-8")


@patch("pandas.read_excel")
def test_read_xlsx(mocked_open):
    # Вызываем функцию с тестовым файлом
    read_data = {"id": [65073503, 359568919], "state": ["EXECUTED", "EXECUTED"]}
    mock_data = pd.DataFrame(read_data)
    mocked_open.return_value = mock_data
    result = read_excel("test")
    # Проверяем результат
    expected_result = [{"id": 65073503, "state": "EXECUTED"}, {"id": 359568919, "state": "EXECUTED"}]
    assert result == expected_result
