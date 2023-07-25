#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print(column, end="")
        print()
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]