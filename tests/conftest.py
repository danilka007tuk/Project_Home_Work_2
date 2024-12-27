from typing import Dict, List, Union

import pytest


@pytest.fixture
def to_mask_card() -> str:
    return "73654108430135874305"


@pytest.fixture
def to_mask() -> str:
    return "7000792289606361"

@pytest.fixture
def expected() -> str:
    return "8675874657756475"

@pytest.fixture
def new_card() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def old_data() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def last_dict() -> List[Dict[str, Union[str, float, int]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sort_list() -> List[Dict[str, Union[str, float, int]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
