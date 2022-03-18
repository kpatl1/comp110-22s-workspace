"""Dictionary related utility functions."""

__author__ = "730477803"

from csv import DictReader


# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row) 
    file_handle.close
    return result


def column_values(input_table: list[dict[str, str]], column_name: "str") -> list[str]:
    result: list[str] = []
    for row in input_table: 
        item: str = row[column_name]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)
    
    return result


def head(data_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in data_table:
        n_values_in_column: list[str] = []
        for i in range(n):
            n_values_in_column.append(data_table[column][i])
        result[column] = n_values_in_column
    return result


def select(data_table: dict[str, list[str]], column_subset_names: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in column_subset_names:
        result[column] = data_table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            for i in range(len(table2[column])):
                item: str = table2[column][i]
                result[column].append(item)
        else: 
            result[column] = table2[column]
    return result 


def count(count_values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in count_values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result