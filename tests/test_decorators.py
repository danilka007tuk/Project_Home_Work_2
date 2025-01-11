from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_log(capsys, last_dict):
    filter_by_state(last_dict, "EXECUTED")
    captured = capsys.readouterr()
    assert captured.out == (
        "Getting started with the function filter_by_state\n"
        + "[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, "
        + "{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]\n"
        + "Shutting down the function\n"
    )


def test_sort_by_date_log(capsys, sort_list, arg2: bool = True):
    sort_by_date(sort_list, arg2)
    captured = capsys.readouterr()
    assert captured.out == (
        "Getting started with the function sort_by_date\n" +
        "[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, " +
        "{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, " +
        "{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, " +
        "{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]\n" +
        "Shutting down the function\n"
    )



