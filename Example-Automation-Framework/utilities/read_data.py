import csv


def get_csv_data(file_name):
    # Create an empty list to store rows
    rows = []

    # Open the CSV file
    data_file = open(file_name, "r")

    # Create a CSV reader from CSV file
    reader = csv.reader(data_file)

    # Skip the headers
    next(reader)

    # Add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
