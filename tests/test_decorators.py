from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_log(capsys, last_dict):
    filter_by_state(last_dict, "EXECUTED")
    captured = capsys.readouterr()
    assert captured.out == ("Getting started with the function filter_by_state\n" "Shutting down the function\n")


def test_sort_by_date_log(capsys, sort_list, arg2: bool = True):
    sort_by_date(sort_list, arg2)
    captured = capsys.readouterr()
    assert captured.out == ("Getting started with the function sort_by_date\n" "Shutting down the function\n")
