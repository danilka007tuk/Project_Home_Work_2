from src.utils import operation


def test_operation(mock_operation_json_file):
    transactions = operation("operations")
    # # Тестируй свою функцию, используя mock_operation_json_file
    assert len(transactions) == 101


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
