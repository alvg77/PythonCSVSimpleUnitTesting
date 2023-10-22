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
    mocker.side_effect = csv.Error("File is not a CSV file")

def test_parse_csv_with_fixture(mocker, mock_open_csv):
    data = parse_csv('fake_file_path.csv')

    expected_data = [
        {'Videogame': 'Pong', 'Price': '25', 'Playtime': '4.5'},
        {'Videogame': 'Space Invaders', 'Price': '30', 'Playtime': '3.8'}
    ]

    assert data == expected_data

def test_parse_csv_throws_exception_without_fixture(mocker):
    mocker.side_effect = csv.Error("File is not a CSV file")
    
    with pytest.raises(csv.Error) as e:
        data = parse_csv('fake_file_path')

    assert "File is not a CSV file" in str(e.value)
    

def test_parse_csv_throws_exception_with_fixture():
    with pytest.raises(Exception) as e:
        parse_csv('dudu')

    assert e.type == csv.Error
    assert "File is not a CSV file" in str(e.value)

@pytest.fixture
def csv_parser(mocker, mock_open_csv):
    return CSVParser(parse_csv('fake_file_path.csv'))

def test_sum_column_throws_value_error(csv_parser):
    with pytest.raises(ValueError) as e:
        csv_parser.sum_column("Videogame")

    assert e.type == ValueError
    assert "Value is not a number" in str(e.value)

def test_min_max_avg_throws_value_error(csv_parser):
    with pytest.raises(ValueError) as e:
        csv_parser.min_max_avg("Videogame")

    assert e.type == ValueError
    assert "Value is not a number" in str(e.value)

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
