import pytest
import csv
from csv_parser.csv_parser import CSVParser, parse_csv

CSV_CONTENT = """Videogame,Price,Playtime
Pong,25,4.5
Space Invaders,30,3.8
"""

@pytest.fixture
def mock_open_csv(mocker):
    mocker.patch('builtins.open', mocker.mock_open(read_data=CSV_CONTENT))

def test_parse_csv_with_fixture(mocker, mock_open_csv):
    data = parse_csv('fake_file_path.csv')

    # Verify the data matches the expected output
    expected_data = [
        {'Videogame': 'Pong', 'Price': '25', 'Playtime': '4.5'},
        {'Videogame': 'Space Invaders', 'Price': '30', 'Playtime': '3.8'}
    ]
    assert data == expected_data


@pytest.fixture
def csv_parser(mocker, mock_open_csv):
    return CSVParser(parse_csv('fake_file_path.csv'))

def test_get_num_rows(csv_parser):
    assert csv_parser.get_num_rows() == 2

def test_sum_column(csv_parser):
    assert csv_parser.sum_column("Price") == 55

def test_min_max_avg(csv_parser):
    minimum, maximum, average = csv_parser.min_max_avg("Playtime")
    assert minimum == 3.8
    assert maximum == 4.5
    assert average == 4.15

def test_shortest_longest_string(csv_parser):
    shortest, longest = csv_parser.shortest_longest_string("Videogame")
    assert shortest == "Pong"
    assert longest == "Space Invaders"

