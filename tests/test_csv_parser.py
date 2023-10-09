import pytest
from csv_parser.csv_parser import CSVParser

# Sample CSV file path
CSV_FILE_PATH = "sample.csv"

@pytest.fixture
def csv_parser():
    return CSVParser(CSV_FILE_PATH)

def test_get_num_rows(csv_parser):
    assert csv_parser.get_num_rows() == 5

def test_sum_column(csv_parser):
    assert csv_parser.sum_column("Price") == 140

def test_min_max_avg(csv_parser):
    minimum, maximum, average = csv_parser.min_max_avg("Playtime")
    assert minimum == 3.8
    assert maximum == 4.8
    assert average == 4.26

def test_shortest_longest_string(csv_parser):
    shortest, longest = csv_parser.shortest_longest_string("Videogame")
    assert shortest == "Pong"
    assert longest == "Space Invaders"
