import csv
import statistics

def parse_csv(file_path):
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
                pass
        return total

    def min_max_avg(self, column_name):
        values = []

        assert values == [], "Values should be empty in the beginning"

        for row in self.data:
            try:
                value = float(row[column_name])
                values.append(value)
            except ValueError:
                pass
        
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


# if __name__ == "__main__":
#     file_path = "sample.csv"  # Replace with the path to your CSV file
#     parser = CSVParser(file_path)
    
#     num_rows = parser.get_num_rows()
#     print(f"Line count: {num_rows}")
    
#     column_name = "Grade"  # Replace with the name of the column you want statistics for
    
#     total_sum = parser.sum_column(column_name)
#     print(f"Sum {column_name}: {total_sum}")
    
#     min_val, max_val, avg_val = parser.min_max_avg(column_name)
#     print(f"Min {column_name}: {min_val}")
#     print(f"Max {column_name}: {max_val}")
#     print(f"Average {column_name}: {avg_val}")
    
#     shortest_str, longest_str = parser.shortest_longest_string(column_name)
#     print(f"Shortest {column_name}: {shortest_str}")
#     print(f"Longest {column_name}: {longest_str}")
