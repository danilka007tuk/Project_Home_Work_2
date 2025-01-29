from src.utils import operation


def test_operation(mock_operation_json_file):
    transactions = operation("operations")
    # # Тестируй свою функцию, используя mock_operation_json_file
    assert len(transactions) == 101


# @patch("builtins.open", new_callable=mock_open, read_data="id,state\n441945886,EXECUTED\n41428829,EXECUTED")
# def test_operation_read(mocked_open):
#     # Вызываем функцию с тестовым файлом
#     result = operation("test.json")
#
#     # Проверяем результат
#     expected_result = [{"id": "441945886", "state": "EXECUTED"}, {"id": "41428829", "state": "EXECUTED"}]
#     assert result == expected_result
#     mocked_open.assert_called_once_with("test.json", "r")

# def test_operation_called_with(mock_operation_json):
#    mock_random = Mock(return_value=mock_operation_json)
#    mock_operation_json = mock_random
#    assert operation() == data

# @patch("json.load")
# def test_operation_list(mock_operation_json_file):
#     mock_operation_json_file.return_value = operation("operations")
#     assert operation("open_file") ==
#     mock_operation_json_file.assert_called_once_with()

# def test_operation_called_with():
#     with patch('builtins.print') as mock_print:
#         data = {"amount":"31957.58"}
#         operation(data)
#         mock_print.assert_called_once_with(data)
#
