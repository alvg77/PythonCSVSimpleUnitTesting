import csv
import statistics

def parse_csv(file_path):
    if not file_path.endswith('.csv'):
        raise csv.Error("File is not a CSV file")
    with open(file_path, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        data = list(csvreader)
    return data

class CSVParser:
    def __init__(self, data):
        self.data = data

    def get_num_rows(self):
        return len(self.data)

    def sum_column(self, column_name):
        total = 0
        for row in self.data:
            try:
                total += float(row[column_name])
            except ValueError:
                raise ValueError("Value is not a number")
        return total

    def min_max_avg(self, column_name):
        values = []

        assert values == [], "Values should be empty in the beginning"

        for row in self.data:
            try:
                value = float(row[column_name])
                values.append(value)
            except ValueError:
                raise ValueError("Value is not a number")
        
        minimum = min(values)
        maximum = max(values)
        average = statistics.mean(values)

        assert maximum != None, "Maximum should not be None"
        assert minimum != None, "Minimum should not be None"
        assert average != None, "Average should not be None"

        return minimum, maximum, average

    def shortest_longest_string(self, column_name):
        strings = [row[column_name] for row in self.data if column_name in row]
        
        shortest = min(strings, key=len)
        longest = max(strings, key=len)

        assert shortest != None, "Shortest should not be None"
        assert longest != None, "Longest should not be None"

        return shortest, longest